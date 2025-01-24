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


<p align="center" width="100%">
    <img width="60%" src="https://github.com/user-attachments/assets/9b94f513-e1b1-44ff-906b-110922236185">
</p>

<p align="center" style="font-size: 30%;">
    <strong>Figure 1</strong>. Time evolution of cluster size and sphericity distribution in `nb`. Left: average cluster size vs. time, with error bars as standard deviation and colors indicating sphericity (Φ). The inset shows smaller clusters early in the simulation. Right: boxplots display sphericity distributions for clusters of sizes 10<sup>1</sup> < n ≤ 10<sup>2</sup>, 10<sup>2</sup> < n ≤ 10<sup>3</sup>, and 10<sup>3</sup> < n ≤ 10<sup>4</sup>.
</p>

<p align="center" width="100%">
    <img width="60%" src="https://github.com/user-attachments/assets/b93a686f-0b3d-42dd-bd60-d59633b3d0a5">
</p>

<p align="center" style="font-size: 30%;">
    <strong>Figure 1</strong>. Time evolution of cluster size and mole fraction distribution in _nb_. Left: average cluster size vs. time, with error bars as standard deviation and colors indicating sphericity (Φ). The inset shows smaller clusters early in the simulation. Right: boxplots display sphericity distributions for clusters of sizes 10<sup>1</sup> < n ≤ 10<sup>2</sup>, 10<sup>2</sup> < n ≤ 10<sup>3</sup>, and 10<sup>3</sup> < n ≤ 10<sup>4</sup>.
</p>

<p align="center" width="100%">
    <img width="60%" src="https://github.com/user-attachments/assets/66d8d02b-cf98-4672-bfad-1b924fd630f2">
</p>

<p align="center" style="font-size: 30%;">
    <strong>Figure 1</strong>. Heatmap showing mole fraction (X<sub>nonane</sub>) across radial layers of the largest cluster over time in *nb*, with lower-value radial layers near the core and higher-value layers near the surface..
</p>


![fig_heatmap_radial_time_NON_BUT](https://github.com/user-attachments/assets/66d8d02b-cf98-4672-bfad-1b924fd630f2)

![fig_heatmap_radial_time_SOL_BUT](https://github.com/user-attachments/assets/305171f9-b47e-4c40-ba40-a005be41b70e)

![fig_fragmentation_SOL_BUT_mol1](https://github.com/user-attachments/assets/5a647968-a4f3-4400-bb2c-4b0944e1398a)

![fig_fragmentation_SOL_BUT_mol1](https://github.com/user-attachments/assets/1731b2f7-c60a-467f-86f8-0737c0bdd194)

![fig_fragmentation_NON_BUT_mol1](https://github.com/user-attachments/assets/9495b02b-0c17-471e-8396-43bdd4e031e7)

![fig_fragmentation_NON_BUT_mol2](https://github.com/user-attachments/assets/db121cc7-c5aa-4f40-b234-73d6b4714392)



## Conclusion
[[back to contents](#contents)]
