# Investigated the homogeneous binary nucleation of atmospherically-relevant molecules

### Contents

🔖 **Sections**
- [Overview](#overview)
- [Objectives](#objectives)
- [Simulation Setup](#simulation-setup)
- [Simulation Analysis](#simulation-analysis)
- [Conclusion](#conclusion)

🐍 **Python Scripts**
* [Generate Clusters Dataset](ANALYSIS/0_data_fort-to-panda.ipynb)
* [Plot Spatial Heatmap](ANALYSIS/1_plot_spatial-heatmap.ipynb)
* [Generate Mole Fraction Dataset](ANALYSIS/2_data_mole-fraction.ipynb)
* [Plot Cluster Growth](ANALYSIS/3_plot_growth_mole-fraction_sphericity.ipynb)
* [Plot Radial Layers](ANALYSIS/4_plot_radial-layers.ipynb)
* [Generate Fragmentation Dataset](ANALYSIS/5_data_fragmentation.ipynb)
* [Plot Fragmentation](ANALYSIS/6_plot_fragmentation.ipynb)

## Overview
[[back to contents](#contents)]

Aerosol formation from atmospheric gases is vital to atmospheric science, particularly in cloud condensation processes. The first stage, nucleation, involves the emergence of critical nuclei from supersaturated vapor, a stochastic process described by Classical Nucleation Theory (CNT) as governed by competing surface and bulk free energy terms. While single-component nucleation is well-described by CNT, multi-component nucleation introduces complexity, with cluster composition and interactions significantly influencing nucleation and growth behaviors. Experimental techniques like the cloud chamber method have provided nucleation rate data, yet mapping the internal ordering of critical nuclei remains challenging.

Computational methods such as Monte Carlo (MC) simulations and molecular dynamics (MD) have offered insights into nucleation. MC simulations excel at calculating critical nucleus size and structure but are computationally expensive for multi-component systems. In contrast, MD simulations enable larger-scale studies of nucleation and growth dynamics, albeit requiring high supersaturation or long simulation times to overcome the low probability of nucleation. Studies of binary systems, like water/ethanol, reveal core-shell motifs and mutual enhancement of nucleation rates due to hydrogen bonding, while water/$n$-nonane systems demonstrate two-pathway mechanisms driven by immiscibility.

## Objectives
[[back to contents](#contents)]

This study investigates homogeneous vapor-liquid nucleation in six binary mixtures of atmospherically relevant gases: water, $n$-nonane, 1-butanol, and methanol. Representing hydrophilic, hydrophobic, large amphiphilic, and small amphiphilic molecules, these systems are explored using MD simulations to analyze cluster structures and their evolution over time. By linking molecular properties to emerging cluster configurations, this work advances the understanding of fundamental binary nucleation mechanisms and their relevance to atmospheric aerosol formation.

## Simulation Setup
[[back to contents](#contents)]

Six systems were prepared, each containing a binary combination from the quaternary pool of water/$n$-nonane/1-butanol/methanol. The systems were abbreviated as $nb$, $wm$, $wb$, $bm$, $wn$, and $nm$ for $n$-nonane/1-butanol, water/methanol, water/1-butanol, 1-butanol/methanol, water/$n$-nonane, and $n$-nonane/methanol, respectively.

A cubic simulation box of 40 nm$^3$ was constructed for each system, and a three-dimensional periodic boundary condition was set. The chosen population size for each system was 10,000 molecules, comprising equal amounts of the contained molecule types, as shown in Table \ref{tab:sys_components}. The initial structures were copied and randomly inserted several times in the system until the desired total number of molecules was achieved using the \textit{gmx insert-molecules} module of the Groningen Machine for Chemical Simulations (GROMACS) software package.\cite{van2005gromacs}

## Simulation Analysis
[[back to contents](#contents)]

![fig_sphericity_combined_BUT_MET](https://github.com/user-attachments/assets/cc44fd12-3eba-48da-b2d3-962182e9067a)

![fig_mole_fraction_combined_BUT_MET](https://github.com/user-attachments/assets/deb42273-35c2-4161-9a72-ad9aae5d8a8c)

![mole_fraction_time_radial_heatmap_filtered_BUT_MET](https://github.com/user-attachments/assets/3396d829-128c-461d-8096-7d1633568b61)

![combined_plot_BUT_MET](https://github.com/user-attachments/assets/ea952f39-5ec7-4d85-a016-f409dff5193f)



## Conclusion
[[back to contents](#contents)]
