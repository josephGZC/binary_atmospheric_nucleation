# Investigated the binary nucleation and growth of atmospherically-relevant molecules

The following repository contains some of the jupyter lab python scripts I used in the simulation of atmospherically-relevant molecules. </br>
> Each section includes brief, symbol-marked sentences (ℹ️ for information and 🔎 for procedural summaries) to help guide readers in understanding the problem variables and the questions being addressed.

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

Aerosol formation produces tiny particles that act as starting points for cloud formation. These particles can change how clouds reflect sunlight or trap heat, affecting the weather and contributing to climate change. Before aerosols formation, two earlier processes are nucleation and growth. Before aerosol formation, two earlier processes are nucleation and growth. Nucleation occurs at the molecular scale, where a few molecules cluster together to form tiny initial particles, while growth happens at a larger scale as these particles accumulate more molecules and increase in size. There is keen interest in studying the early stages of aerosol formation, especially in multi-component systems, which often begin as binary mixtures. The behavior of these systems is characterized by the shape, composition, and ordering of molecules within the clusters formed during these initial processes. By characterizing these systems, researchers can develop more accurate equations and models to track aerosol formation from its earliest stages, ultimately improving weather prediction and climate models.

> ℹ️ Where do the investigations start? </br>
> * The shape, structure, and arrangement of clusters depend on the properties of the molecules that make them up, particularly how strongly the molecules attract to each other. </br>
> * By studying hydrophilic (water-loving), hydrophobic (water-repelling), and amphiphilic (having both water-loving and water-repelling parts) molecules, we can predict how clusters will behave based on these properties.

## Objectives
[[back to contents](#contents)]

This study investigates nucleation and growth of three binary mixtures of atmospherically relevant gases: water, nonane, 1-butanol.  Representing hydrophilic, hydrophobic, and amphiphilic molecules, these systems are explored using MD simulations to analyze cluster structures and their evolution over time. By linking molecular properties to emerging cluster configurations, this work advances the understanding of fundamental binary nucleation mechanisms and their relevance to atmospheric aerosol formation.

<p align="center" width="100%">
    <img width="60%" src="https://github.com/user-attachments/assets/d18c39d2-e33e-4df8-ac6c-583c7d9aa95e">
</p>
<p align="center" style="font-size: 30%;">
    <strong>Figure 1</strong>. Structure of (a) water, (b) nonane, and (c) 1-butanol, shown using stick models (top) and sphere models (bottom). Carbon (C), oxygen (O), and hydrogen (H) atoms are labeled. Some hydrogen atoms are grayed out to emphasize the carbon atoms, which are more relevant to the discussion of hydrophobic properties.
</p>
      
## Simulation Setup
[[back to contents](#contents)]

Three binary mixtures were analyzed: nonane/1-butanol, water/nonane, water/1-butanol (Fig. [2](#anchor-F2)). A cubic simulation box of 40 nm<sup>3</sup> was constructed for each system. The chosen population size for each system was 10,000 molecules, comprising equal amounts of the contained molecule types. The initial structures were copied and randomly inserted several times in the system until the desired total number of molecules was achieved.

<a name="anchor-F2"></a>
<p align="center" width="100%">
    <img width="60%" src="https://github.com/user-attachments/assets/89b39247-b85e-432a-945a-dddec8be6320">
</p>
<p align="center" style="font-size: 30%;">
    <strong>Figure 2</strong>. Three binary mixtures: nonane/1-butanol, water/nonane, and water/1-butanol.
</p>

> 🔎 **Pairs investigated** </br>
> * nonane/1-butanol (hydrophobic/ampiphilic; minimal miscibility gap, corresponds to excellent mixing) </br>
> * water/nonane (hydrophilic/hydrophobic; pronounced miscibility gap, corresponds to poor mixing)  </br>
> * water/1-butanol (hydrophilic/ampiphilic; partial miscibility gap, corresponds  to intermediate mixing) 

## Simulation Analysis
[[back to contents](#contents)]

Each system, starting with binary mixtures in the vapor state, shows molecules beginning to cluster together as the temperature increases during the simulation, marking the onset of condensation (Fig. [3](#anchor-F3)). As the simulation progresses, nearly all molecules eventually form clusters.

<a name="anchor-F3"></a>
<p align="center" width="100%">
    <img width="60%" src="https://github.com/user-attachments/assets/d5383489-7c82-4ad1-b36f-09f489eb6f49">
</p>
<p align="center" style="font-size: 30%;">
    <strong>Figure 3</strong>. Snapshots of nonane/butanol system at (a) 0, (b) 10, and (c) 50 ns.
</p

Throughout the simulation, a distribution of clusters of varying sizes emerged, in which larger clusters comprise higher number of molecules. The generated clusters were analyzed based on their sphericity (Fig. [4](#anchor-F4), [S1](#anchor-S1), [S2](#anchor-S2)) and mole fraction (Fig. [5](#anchor-F5), [S3](#anchor-S3), [S4](#anchor-S4)). For each property, the median values and their variability (spread) are visualized using boxplots. To facilitate a more convenient comparison, the clusters are categorized into three size ranges: small (10<sup>1</sup> to 10<sup>2</sup> molecules), intermediate (10<sup>2</sup> to 10<sup>3</sup> molecules), and large (10<sup>3</sup> to 10<sup>4</sup> molecules). 

For all systems, the sphericity of smaller-sized clusters ranges from 0.2 to 0.9 (Fig. [4](#anchor-F4), [S1](#anchor-S1), [S2](#anchor-S2)) with a median between 0.7 to 0.8. This suggests significant structure variability from a spherical configuration in the initial phase of droplet formation. In the case of larger-sized clusters, the median sphericity ranges from 0.8 to 1 across different systems, reflecting their stability in a spherical shape. These observations corroborate and expand upon the research by [Tarek et al. (1997)](https://doi.org/10.1021/jp972278s), which reported increased shape variability in smaller water/ethanol clusters. Although water/nonane clusters are spherical on average, it exhibits a similar microarrangement to the clusters simulated by [Obeidat et al. (2015)](https://doi.org/10.1021/jp509919u), where they define a water/nonane droplet to have a lens-on-sphere structure. This model describes the nonane cluster as a lens shape that wets the spherical shape of the water cluster.

<a name="anchor-F4"></a>
<p align="center" width="100%">
    <img width="60%" src="https://github.com/user-attachments/assets/9b94f513-e1b1-44ff-906b-110922236185">
</p>
<p align="center" style="font-size: 30%;">
    <strong>Figure 4</strong>. Time evolution of cluster size and sphericity distribution in nonane/butanol. Left: average cluster size vs. time, with error bars as standard deviation and colors indicating sphericity (Φ). The inset shows smaller clusters early in the simulation. Right: boxplots display sphericity distributions for clusters of sizes 10<sup>1</sup> < n ≤ 10<sup>2</sup>, 10<sup>2</sup> < n ≤ 10<sup>3</sup>, and 10<sup>3</sup> < n ≤ 10<sup>4</sup>.
</p>

Among systems with minimal or partial miscibility gap (nonane/butanol and water/butanol), nearly equal amounts of each nucleating vapor were observed (median X~0.5) as shown in Fig. [5](#anchor-F5), [S3](#anchor-S3). Furthermore, a trend was observed in which the spread of mole fraction values decreased with increasing cluster size (as indicated by the decreasing area of the boxplots). In contrast, the water/nonane system exhibited a wide spread of mole fraction values in the small clusters, which is likely caused by the pronounced miscibility gap between the involved molecules (Fig. [S4](#anchor-S4)). Interestingly, larger clusters in the water/nonane system displayed mole fraction values close to 0.5. While the observed near-equimolar distribution of nucleating vapors in nonane/butanol and water/butanol clusters is likely due to the low miscibility gap in these systems, the similar behavior in water/nonane may be caused by another interaction, such as the clumping of unary clusters without significant mixing.

<a name="anchor-F5"></a>
<p align="center" width="100%">
    <img width="60%" src="https://github.com/user-attachments/assets/b93a686f-0b3d-42dd-bd60-d59633b3d0a5">
</p>
<p align="center" style="font-size: 30%;">
    <strong>Figure 5</strong>. Time evolution of cluster size and mole fraction distribution in nonane/butanol. Left: average cluster size vs. time, with error bars as standard deviation and colors indicating sphericity (Φ). The inset shows smaller clusters early in the simulation. Right: boxplots display sphericity distributions for clusters of sizes 10<sup>1</sup> < n ≤ 10<sup>2</sup>, 10<sup>2</sup> < n ≤ 10<sup>3</sup>, and 10<sup>3</sup> < n ≤ 10<sup>4</sup>.
</p>

To get a better understanding of the cluster shape and composition, a look into the internal ordering within the cluster is necessary. Radial layers are reported for the largest cluster over time, which were accompanied by cluster snapshots (Fig. [6](#anchor-F6)). The lower-value radial layers signify regions closer to the core while the larger-value radial layers are closer to the cluster surface. Snapshots illustrating the radial layers were captured at 1 ns, 10 ns, and 100 ns to provide a visual representation.

<a name="anchor-F6"></a>
<p align="center" width="100%">
    <img width="60%" src="https://github.com/user-attachments/assets/66d8d02b-cf98-4672-bfad-1b924fd630f2">
</p>
<p align="center" style="font-size: 30%;">
    <strong>Figure 6</strong>. Heatmap showing mole fraction (X<sub>nonane</sub>) across radial layers of the largest cluster over time in nonane/butanol, with lower-value radial layers near the core and higher-value layers near the surface.
</p>

<a name="anchor-F7"></a>
<p align="center" width="100%">
    <img width="60%" src="https://github.com/user-attachments/assets/305171f9-b47e-4c40-ba40-a005be41b70e">
</p>
<p align="center" style="font-size: 30%;">
    <strong>Figure 7</strong>. Heatmap showing mole fraction (X<sub>water</sub>) across radial layers of the largest cluster over time in water/butanol, with lower-value radial layers near the core and higher-value layers near the surface.
</p>

<a name="anchor-F8"></a>
<p align="center" width="100%">
    <img width="60%" src="https://github.com/user-attachments/assets/9495b02b-0c17-471e-8396-43bdd4e031e7">
</p>
<p align="center" style="font-size: 30%;">
    <strong>Figure 8</strong>. Fragmentation of nonane within nonane/butanol clusters over time. Molecules are fragmented when clustering criteria are met. Higher fragmentation indicates fewer unary components forming a network. The gray line shows the total number of molecules in the largest cluster, while stacked bars represent fragment sizes. Bar colors range from red (less fragmentation; more networked unary components) to blue (more fragmentation; fewer networked unary components).
</p>

<a name="anchor-F9"></a>
<p align="center" width="100%">
    <img width="60%" src="https://github.com/user-attachments/assets/db121cc7-c5aa-4f40-b234-73d6b4714392">
</p>
<p align="center" style="font-size: 30%;">
    <strong>Figure 9</strong>. Fragmentation of butanol within nonane/butanol clusters over time. Molecules are fragmented when clustering criteria are met. Higher fragmentation indicates fewer unary components forming a network. The gray line shows the total number of molecules in the largest cluster, while stacked bars represent fragment sizes. Bar colors range from red (less fragmentation; more networked unary components) to blue (more fragmentation; fewer networked unary components).
</p>

<a name="anchor-F10"></a>
<p align="center" width="100%">
    <img width="60%" src="https://github.com/user-attachments/assets/5a647968-a4f3-4400-bb2c-4b0944e1398a">
</p>
<p align="center" style="font-size: 30%;">
    <strong>Figure 10</strong>. Fragmentation of water within water/butanol clusters over time. Molecules are fragmented when clustering criteria are met. Higher fragmentation indicates fewer unary components forming a network. The gray line shows the total number of molecules in the largest cluster, while stacked bars represent fragment sizes. Bar colors range from red (less fragmentation; more networked unary components) to blue (more fragmentation; fewer networked unary components).
</p>

<a name="anchor-F11"></a>
<p align="center" width="100%">
    <img width="60%" src="https://github.com/user-attachments/assets/53cea23c-d955-41da-a259-61bc761c901d">
</p>
<p align="center" style="font-size: 30%;">
    <strong>Figure 11</strong>. Fragmentation of butanol within water/butanol clusters over time. Molecules are fragmented when clustering criteria are met. Higher fragmentation indicates fewer unary components forming a network. The gray line shows the total number of molecules in the largest cluster, while stacked bars represent fragment sizes. Bar colors range from red (less fragmentation; more networked unary components) to blue (more fragmentation; fewer networked unary components).
</p>

## Conclusion
[[back to contents](#contents)]

## Appendix
<a name="anchor-S1"></a>
<p align="center" width="100%">
    <img width="60%" src="https://github.com/user-attachments/assets/99d862a3-4ea6-4b64-b521-6a36e4450400">
</p>
<p align="center" style="font-size: 30%;">
    <strong>Figure S1</strong>. Time evolution of cluster size and sphericity distribution in <i>wn</i>. Left: average cluster size vs. time, with error bars as standard deviation and colors indicating sphericity (Φ). The inset shows smaller clusters early in the simulation. Right: boxplots display sphericity distributions for clusters of sizes 10<sup>1</sup> < n ≤ 10<sup>2</sup>, 10<sup>2</sup> < n ≤ 10<sup>3</sup>, and 10<sup>3</sup> < n ≤ 10<sup>4</sup>.
</p>

<a name="anchor-S2"></a>
<p align="center" width="100%">
    <img width="60%" src="https://github.com/user-attachments/assets/6c22e4bf-2d9e-4a1e-bb63-2f032f79d033">
</p>
<p align="center" style="font-size: 30%;">
    <strong>Figure S2</strong>. Time evolution of cluster size and sphericity distribution in <i>wb</i>. Left: average cluster size vs. time, with error bars as standard deviation and colors indicating sphericity (Φ). The inset shows smaller clusters early in the simulation. Right: boxplots display sphericity distributions for clusters of sizes 10<sup>1</sup> < n ≤ 10<sup>2</sup>, 10<sup>2</sup> < n ≤ 10<sup>3</sup>, and 10<sup>3</sup> < n ≤ 10<sup>4</sup>.
</p>

<a name="anchor-S3"></a>
<p align="center" width="100%">
    <img width="60%" src="https://github.com/user-attachments/assets/7b252d63-c630-47ea-95df-628d015b1df1">
</p>
<p align="center" style="font-size: 30%;">
    <strong>Figure S3</strong>. Time evolution of cluster size and mole fraction distribution in <i>wn</i>. Left: average cluster size vs. time, with error bars as standard deviation and colors indicating sphericity (Φ). The inset shows smaller clusters early in the simulation. Right: boxplots display mole fraction distributions for clusters of sizes 10<sup>1</sup> < n ≤ 10<sup>2</sup>, 10<sup>2</sup> < n ≤ 10<sup>3</sup>, and 10<sup>3</sup> < n ≤ 10<sup>4</sup>.
</p>

<a name="anchor-S4"></a>
<p align="center" width="100%">
    <img width="60%" src="https://github.com/user-attachments/assets/7e6398ad-7a6b-4fe0-bffa-8669b9b2caf6">
</p>
<p align="center" style="font-size: 30%;">
    <strong>Figure S3</strong>. Time evolution of cluster size and mole fraction distribution in <i>wb</i>. Left: average cluster size vs. time, with error bars as standard deviation and colors indicating sphericity (Φ). The inset shows smaller clusters early in the simulation. Right: boxplots display mole fraction distributions for clusters of sizes 10<sup>1</sup> < n ≤ 10<sup>2</sup>, 10<sup>2</sup> < n ≤ 10<sup>3</sup>, and 10<sup>3</sup> < n ≤ 10<sup>4</sup>.
</p>

<a name="anchor-S5"></a>
<p align="center" width="100%">
    <img width="60%" src="https://github.com/user-attachments/assets/bcc138ad-3b46-411a-a280-11c895e016a9">
</p>
<p align="center" style="font-size: 30%;">
    <strong>Figure S5</strong>. Heatmap showing mole fraction (X<sub>water</sub>) across radial layers of the largest cluster over time in water/nonane, with lower-value radial layers near the core and higher-value layers near the surface.)
</p>


https://github.com/user-attachments/assets/e5001b82-71dc-437e-826a-9f5c0203d5a5




