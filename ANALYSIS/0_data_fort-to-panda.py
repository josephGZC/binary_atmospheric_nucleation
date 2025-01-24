# ‼️This .py version can be utilized when .ipynb script constatntly crashes
# ===========================
# Investigated the homogeneous binary nucleation of atmospherically-relevant molecules
# =========================== 

# 🧱 Generate Dataframe: 
#     Conversion of fortran output files to pandas dataframe
# ---------------------------
# Table of Contents
# 1️⃣ Convert fort to panda 💤->🐼
# 2️⃣ Review generated parquets
# ----------------------------

# ===============================
# Convert fort to panda 💤->🐼
# ===============================
# 📆 Date created: October 12, 2024
# 📆 Date updated: October 14, 2024
# - generates parquet files instead of feather

import pandas as pd
import glob
import re
import os
import pyarrow as pa
import pyarrow.parquet as pq

# Initialize variables
data_rows = []
batch_number = 1
files_processed = 0
batch_size = 10  # Number of files to process in each batch
batch_parquet_files = []  # List to keep track of batch Parquet filenames

# Get the list of all fort.9* files and sort them numerically
file_list = sorted(glob.glob('fort.9*'), key=lambda x: int(re.match(r'fort\.(\d+)', x).group(1)))

print(f"Files found: {file_list}")

# Check if any files were found
if not file_list:
    print("No files found matching the pattern 'fort.9*'. Please check the file names and the directory.")
else:
    # Iterate over each file
    for filename in file_list:
        # Extract the number from the filename
        match = re.match(r'fort\.(\d+)', filename)
        if match:
            file_number = int(match.group(1))
        else:
            print(f"Filename {filename} does not match the expected pattern 'fort.<number>'. Skipping this file.")
            continue

        # Set verbose flag based on file number
        verbose = file_number >= 9070

        print(f"\nProcessing file: {filename}")

        with open(filename, 'r') as f:
            lines = f.readlines()

        frame_number = None
        num_lines = len(lines)
        line_index = 0

        # Parse the FRAME Number from the first line
        while line_index < num_lines:
            line = lines[line_index]
            frame_match = re.match(r' *FRAME\s+(\d+)\s+TIME \(ns\)\s+([\d\.]+)', line)
            if frame_match:
                frame_number = int(frame_match.group(1))
                time_ns = float(frame_match.group(2))
                line_index += 1
                break
            else:
                line_index += 1

        if frame_number is None:
            print(f"Could not find FRAME information in file {filename}. Skipping this file.")
            continue  # Skip to next file

        # Skip lines until we reach the '****NUCLEUS' section
        while line_index < num_lines:
            line = lines[line_index].strip()
            if line.startswith('****NUCLEUS'):
                break
            line_index += 1

        # Process each NUCLEUS entry
        nucleus_found = False  # Flag to check if any nucleus entries were found
        while line_index < num_lines:
            line = lines[line_index].strip()
            nucleus_match = re.match(r'\*\*\*\*NUCLEUS\s+(\d+)', line)
            if nucleus_match:
                nucleus_found = True
                nucleus_id = int(nucleus_match.group(1))
                line_index += 1  # Move to the comment line

                # Read the comment line and extract Size and number of atoms
                if line_index >= num_lines:
                    if verbose:
                        print(f"Unexpected end of file after NUCLEUS ID {nucleus_id} in file {filename}.")
                    break
                comment_line = lines[line_index].strip()
                size_line_parts = comment_line.split('|')
                if len(size_line_parts) >= 3:
                    size_part = size_line_parts[0].split()
                    try:
                        size = int(size_part[-1])
                        num_atoms = int(size_line_parts[2].strip())
                    except ValueError as e:
                        if verbose:
                            print(f"Error parsing size or number of atoms for NUCLEUS ID {nucleus_id} in file {filename}: {e}")
                        break
                else:
                    if verbose:
                        print(f"Error parsing comment line in file {filename} at line {line_index}")
                    break
                line_index += 1  # Move to atom data lines

                # Read atom data lines
                for atom_idx in range(num_atoms):
                    if line_index >= num_lines:
                        if verbose:
                            print(f"Unexpected end of file when reading atoms for NUCLEUS ID {nucleus_id} in file {filename}.")
                        break
                    atom_line = lines[line_index].strip()
                    atom_parts = atom_line.split()
                    if len(atom_parts) >= 5:
                        try:
                            molecule_name = atom_parts[0]
                            atom_name = atom_parts[1]
                            molecule_id = atom_parts[2]
                            x = float(atom_parts[3])
                            y = float(atom_parts[4])
                            z = float(atom_parts[5])
                        except ValueError as e:
                            if verbose:
                                print(f"Error parsing atom coordinates for NUCLEUS ID {nucleus_id} in file {filename} at line {line_index}: {e}")
                            break
                    else:
                        if verbose:
                            print(f"Error parsing atom line in file {filename} at line {line_index}: {atom_line}")
                            break

                    # Append data to the list
                    data_rows.append({
                        'frame_number': frame_number,
                        'nucleus_id': nucleus_id,
                        'size': size,
                        'molecule_name': molecule_name,
                        'molecule_id': molecule_id,
                        'atom_name': atom_name,
                        'x_coord': x,
                        'y_coord': y,
                        'z_coord': z,
                    })
                    line_index += 1

                # Skip any blank lines after the atom data
                while line_index < num_lines and lines[line_index].strip() == '':
                    line_index += 1
            else:
                line_index += 1  # Move to the next line if not a NUCLEUS entry

        if nucleus_found:
            print(f"Successfully read data from file {filename}.")
        else:
            print(f"No NUCLEUS entries found in file {filename}.")

        files_processed += 1

        # Check if we've reached the batch size
        if files_processed % batch_size == 0 or filename == file_list[-1]:
            # Create the DataFrame from the collected data
            df = pd.DataFrame(data_rows)

            # Define batch Parquet filename with the requested naming convention
            batch_filename = f'nuc_fort-to-panda_batch_{batch_number}.parquet'
            batch_parquet_files.append(batch_filename)

            # Write the batch to a Parquet file
            df.to_parquet(batch_filename, index=False)
            print(f"\nBatch {batch_number}: Data written to '{batch_filename}'.")

            # Reset data_rows and increment batch number
            data_rows = []
            batch_number += 1

    # Combine all batch Parquet files into a single Parquet file
    output_filename = 'nuc_fort-to-panda_combined.parquet'
    print(f"\nCombining batch files into '{output_filename}'...")

    # Read all batch Parquet files and append to a list
    tables = []
    for batch_file in batch_parquet_files:
        table = pq.read_table(batch_file)
        tables.append(table)
        print(f"Added '{batch_file}' to the combined Parquet file.")

    # Concatenate all tables
    combined_table = pa.concat_tables(tables)

    # Write the combined table to the output Parquet file
    pq.write_table(combined_table, output_filename)
    print(f"\nAll data has been written to '{output_filename}'.")
    print(f"Individual batch Parquet files have been kept.")
