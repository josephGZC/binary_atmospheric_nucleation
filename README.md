<img width="1440" alt="Untitled (1920 x 800 px)" src="https://github.com/user-attachments/assets/40291de3-c3a1-4b13-ba4f-2756237c49a4" />

# Investigated the Binary Nucleation and Growth of Atmospherically-relevant Molecules

Each section includes brief, symbol-marked sentences (ℹ️ for information , 🔎 for procedural summaries, and 💡 for analysis summaries) to help guide readers in understanding the problem variables and the questions being addressed.

### Contents

🔖 **Sections**
- [Overview](#overview)
- [Objectives](#objectives)
- [Simulation Setup](#simulation-setup)
- [Simulation Analysis](#simulation-analysis)
- [Conclusion](#conclusion)
- [Appendix](#appendix)

🐍 **Python Scripts**
- <a href="https://github.com/josephGZC/binary_atmospheric_nucleation/blob/main/ANALYSIS/0_data_fort-to-panda.ipynb" target="_blank">Generate Clusters Dataset</a>
- <a href="https://github.com/josephGZC/binary_atmospheric_nucleation/blob/main/ANALYSIS/1_plot_spatial-heatmap.ipynb" target="_blank">Plot Spatial Heatmap</a>
- <a href="https://github.com/josephGZC/binary_atmospheric_nucleation/blob/main/ANALYSIS/2_data_mole-fraction.ipynb" target="_blank">Generate Mole Fraction Dataset</a>
- <a href="https://github.com/josephGZC/binary_atmospheric_nucleation/blob/main/ANALYSIS/3_plot_growth_mole-fraction_sphericity.ipynb" target="_blank">Plot Cluster Growth</a>
- <a href="https://github.com/josephGZC/binary_atmospheric_nucleation/blob/main/ANALYSIS/4_plot_radial-layers.ipynb" target="_blank">Plot Radial Layers</a>
- <a href="https://github.com/josephGZC/binary_atmospheric_nucleation/blob/main/ANALYSIS/5_data_fragmentation.ipynb" target="_blank">Generate Fragmentation Dataset</a>
- <a href="https://github.com/josephGZC/binary_atmospheric_nucleation/blob/main/ANALYSIS/6_plot_fragmentation.ipynb" target="_blank">Plot Fragmentation</a>

📊 **Graph Preview**

Here’s an early preview of the selected images:

<div style="overflow-x: auto; white-space: nowrap; padding: 10px; background-color: #f8f9fa; border-radius: 5px;">
  <a href="https://github.com/user-attachments/assets/9b94f513-e1b1-44ff-906b-110922236185" style="display: inline-block; margin-right: 10px;">
    <img src="https://github.com/user-attachments/assets/9b94f513-e1b1-44ff-906b-110922236185" width="150" height="100" style="border-radius:10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);" alt="Fig 4">
  </a>
  <a href="https://github.com/user-attachments/assets/b93a686f-0b3d-42dd-bd60-d59633b3d0a5" style="display: inline-block; margin-right: 10px;">
    <img src="https://github.com/user-attachments/assets/b93a686f-0b3d-42dd-bd60-d59633b3d0a5" width="150" height="100" style="border-radius:10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);" alt="Fig 5">
  </a>
  <a href="https://github.com/user-attachments/assets/66d8d02b-cf98-4672-bfad-1b924fd630f2" style="display: inline-block; margin-right: 10px;">
    <img src="https://github.com/user-attachments/assets/66d8d02b-cf98-4672-bfad-1b924fd630f2" width="150" height="100" style="border-radius:10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);" alt="Fig 6">
  </a>
  <a href="https://github.com/user-attachments/assets/305171f9-b47e-4c40-ba40-a005be41b70e" style="display: inline-block; margin-right: 10px;">
    <img src="https://github.com/user-attachments/assets/305171f9-b47e-4c40-ba40-a005be41b70e" width="150" height="100" style="border-radius:10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);" alt="Fig 8">
  </a>
  <a href="https://github.com/user-attachments/assets/53cea23c-d955-41da-a259-61bc761c901d" style="display: inline-block; margin-right: 10px;">
    <img src="https://github.com/user-attachments/assets/53cea23c-d955-41da-a259-61bc761c901d" width="150" height="100" style="border-radius:10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);" alt="Fig 10">
  </a>
  <a href="https://github.com/user-attachments/assets/5a647968-a4f3-4400-bb2c-4b0944e1398a" style="display: inline-block; margin-right: 10px;">
    <img src="https://github.com/user-attachments/assets/5a647968-a4f3-4400-bb2c-4b0944e1398a" width="150" height="100" style="border-radius:10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);" alt="Fig 11">
  </a>
  <a href="https://github.com/user-attachments/assets/99d862a3-4ea6-4b64-b521-6a36e4450400" style="display: inline-block; margin-right: 10px;">
    <img src="https://github.com/user-attachments/assets/99d862a3-4ea6-4b64-b521-6a36e4450400" width="150" height="100" style="border-radius:10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);" alt="Fig S1">
  </a>
  <a href="https://github.com/user-attachments/assets/6c22e4bf-2d9e-4a1e-bb63-2f032f79d033" style="display: inline-block; margin-right: 10px;">
    <img src="https://github.com/user-attachments/assets/6c22e4bf-2d9e-4a1e-bb63-2f032f79d033" width="150" height="100" style="border-radius:10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);" alt="Fig S2">
  </a>
  <a href="https://github.com/user-attachments/assets/7b252d63-c630-47ea-95df-628d015b1df1" style="display: inline-block; margin-right: 10px;">
    <img src="https://github.com/user-attachments/assets/7b252d63-c630-47ea-95df-628d015b1df1" width="150" height="100" style="border-radius:10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);" alt="Fig S3">
  </a>
  <a href="https://github.com/user-attachments/assets/7e6398ad-7a6b-4fe0-bffa-8669b9b2caf6" style="display: inline-block; margin-right: 10px;">
    <img src="https://github.com/user-attachments/assets/7e6398ad-7a6b-4fe0-bffa-8669b9b2caf6" width="150" height="100" style="border-radius:10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);" alt="Fig S4">
  </a>
  <a href="https://github.com/user-attachments/assets/bcc138ad-3b46-411a-a280-11c895e016a9" style="display: inline-block; margin-right: 10px;">
    <img src="https://github.com/user-attachments/assets/bcc138ad-3b46-411a-a280-11c895e016a9" width="150" height="100" style="border-radius:10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);" alt="Fig S5">
  </a>
  <a href="https://github.com/user-attachments/assets/9495b02b-0c17-471e-8396-43bdd4e031e7" style="display: inline-block; margin-right: 10px;">
    <img src="https://github.com/user-attachments/assets/9495b02b-0c17-471e-8396-43bdd4e031e7" width="150" height="100" style="border-radius:10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);" alt="Fig S7">
  </a>
  <a href="https://github.com/user-attachments/assets/db121cc7-c5aa-4f40-b234-73d6b4714392" style="display: inline-block; margin-right: 10px;">
    <img src="https://github.com/user-attachments/assets/db121cc7-c5aa-4f40-b234-73d6b4714392" width="150" height="100" style="border-radius:10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);" alt="Fig S8">
  </a>
</div>
<p>
  <br>
</p>

## Overview
[[back to contents](#contents)]

<p align="justify"> 
Aerosol formation produces tiny particles that act as starting points for cloud formation. These particles can change how clouds reflect sunlight or trap heat, affecting the weather and contributing to climate change. Before aerosols formation, two earlier processes are nucleation and growth. Before aerosol formation, two earlier processes are nucleation and growth. Nucleation occurs at the molecular scale, where a few molecules cluster together to form tiny initial particles, while growth happens at a larger scale as these particles accumulate more molecules and increase in size. There is keen interest in studying the early stages of aerosol formation, especially in multi-component systems, which often begin as binary mixtures. The behavior of these systems is characterized by the shape, composition, and ordering of molecules within the clusters formed during these initial processes. By characterizing these systems, researchers can develop more accurate equations and models to track aerosol formation from its earliest stages, ultimately improving weather prediction and climate models. 
</p>

> ℹ️ **Where do the investigations start?**
> * The shape, structure, and arrangement of clusters depend on the properties of the molecules that make them up, particularly how strongly the molecules attract to each other. 
> * By studying hydrophilic (water-loving), hydrophobic (water-repelling), and amphiphilic (having both water-loving and water-repelling parts) molecules, we can predict how clusters will behave based on these properties.

## Objectives
[[back to contents](#contents)]

<p align="justify"> 
This study investigates nucleation and growth of three binary mixtures of atmospherically relevant gases: water, nonane, 1-butanol. Representing hydrophilic, hydrophobic, and amphiphilic molecules, these systems are explored using molecular dynamics simulations to analyze cluster structures and their evolution over time. By linking molecular properties to emerging cluster configurations, this work advances the understanding of fundamental binary nucleation mechanisms and their relevance to atmospheric aerosol formation. Among the properties to be investigated are sphericity and mole fraction.
</p>

<a name="anchor-F1"></a>
<p align="center">
  <img src="https://github.com/user-attachments/assets/d18c39d2-e33e-4df8-ac6c-583c7d9aa95e" width="70%" alt="Fig 1" style="margin-bottom: 0px;">
  <br>
  <span style="font-size: 80%;"><strong>Figure 1</strong>. Structure of (a) water, (b) nonane, and (c) 1-butanol, shown using stick models (top) and sphere models (bottom). Carbon (C), oxygen (O), and hydrogen (H) atoms are labeled. Some hydrogen atoms are grayed out to emphasize the carbon atoms, which are more relevant to the discussion of hydrophobic properties.</span>
</p>

> ℹ️ **Sphericity**
>   * Often represented by symbol Φ
>       * If Φ = 1.0: perfect sphere
>       * If Φ = 0.0: perfect cylinder

> ℹ️ **Mole Fraction**
> * Often represented by symbol X
>     * In a mixture, if X<sub>water</sub> = 1.0: only water is present
>     * In a mixture, if X<sub>water</sub> = 0.0: no water is present
>     * In a mixture, if X<sub>water</sub> = 0.5: equal amount of water and the other molecule of the mixture
>     * In a mixture, if 0.5 > X<sub>water</sub> > 1.0: majority of mixture is water
>     * In a mixture, if 0.0 > X<sub>water</sub> > 0.5: majority of mixture is not water

## Simulation Setup
[[back to contents](#contents)]

<p align="justify"> 
Three binary mixtures were analyzed: nonane/1-butanol, water/nonane, water/1-butanol (<a href="#anchor-F2">Fig. 2</a>). A cubic simulation box of 40 nm<sup>3</sup> was constructed for each system. The chosen population size for each system was 10,000 molecules, comprising equal amounts of the contained molecule types. The initial structures were copied and randomly inserted several times in the system until the desired total number of molecules was achieved.
</p>

<a name="anchor-F2"></a>
<p align="center">
  <img src="https://github.com/user-attachments/assets/6a3b208d-ce75-4d64-bcc0-83914edabc47" width="90%" alt="Fig 2" style="margin-bottom: 0px;">
  <br>
  <span style="font-size: 80%;"><strong>Figure 2</strong>. Three binary mixtures: nonane/1-butanol, water/nonane, and water/1-butanol.</span>
</p>

> 🔎 **Pairs investigated** 
> * nonane/1-butanol 
>     * hydrophobic/ampiphilic 
>     * minimal miscibility gap, corresponds to excellent mixing 
> * water/nonane 
>     * hydrophilic/hydrophobic 
>     * pronounced miscibility gap, corresponds to poor mixing 
> * water/1-butanol 
>     * hydrophilic/ampiphilic 
>     * partial miscibility gap, corresponds to intermediate mixing

## Simulation Analysis
[[back to contents](#contents)]

<p align="justify"> 
Each system begins as a binary mixture in the vapor state. As the temperature increases during the simulation, molecules start clustering together, coresponding to the onset of condensation (<a href="#anchor-F3">Fig. 3</a>). Over time, nearly all molecules eventually combine to form larger clusters. A partial video of the simulation is showed in <a href="#anchor-F9">Fig. 9</a>.
</p>

<a name="anchor-F3"></a>
<p align="center">
  <img src="https://github.com/user-attachments/assets/0f1c4e59-c1fb-4fe9-b054-24d8ed3c54ac" width="100%" alt="Fig 3" style="margin-bottom: 0px;">
  <br>
  <span style="font-size: 80%;"><strong>Figure 3</strong>. Snapshots of nonane/butanol system at (a) 0, (b) 10, and (c) 100 ns.</span>
</p>

> ℹ️ We can also consider the nucleation and growth process we are investigating as the first steps of condensation (phase change from vapor state to liquid state). 

### A. Shape and Compisition of Clusters

<p align="justify"> 
Throughout the simulation, a distribution of clusters of varying sizes emerged, in which larger clusters comprise higher number of molecules. The generated clusters were analyzed based on their sphericity (<a href="#anchor-F4">Fig. 4</a>, <a href="#anchor-S1">Fig. S1</a>, <a href="#anchor-S2">Fig. S2</a>) and mole fraction (<a href="#anchor-F5">Fig. 5</a>, <a href="#anchor-S3">Fig. S3</a>, <a href="#anchor-S4">Fig. S4</a>). For each property, the median values and their variability (spread) are visualized using boxplots. To facilitate a more convenient comparison, the clusters are categorized into three size ranges: small (10<sup>1</sup> to 10<sup>2</sup> molecules), intermediate (10<sup>2</sup> to 10<sup>3</sup> molecules), and large (10<sup>3</sup> to 10<sup>4</sup> molecules). 
</p>

<p align="justify"> 
For all systems, the sphericity of smaller-sized clusters ranges from 0.2 to 0.9 (<a href="#anchor-F4">Fig. 4</a>, <a href="#anchor-S1">Fig. S1</a>, <a href="#anchor-S2">Fig. S2</a>) with a median between 0.7 to 0.8. This suggests significant structure variability from a spherical configuration in the initial phase of droplet formation. In the case of larger-sized clusters, the median sphericity ranges from 0.8 to 1 across different systems, reflecting their stability in a spherical shape. These observations corroborate and expand upon the research by <a href="https://doi.org/10.1021/jp972278s" target="_blank">Tarek et al. (1997)</a>, which reported increased shape variability in smaller water/ethanol clusters. Although water/nonane clusters are spherical on average, it exhibits a similar microarrangement to the clusters simulated by <a href="https://doi.org/10.1021/jp509919u" target="_blank">Obeidat et al. (2015)</a>, where they define a water/nonane droplet to have a lens-on-sphere structure. This model describes the nonane cluster as a lens shape that wets the spherical shape of the water cluster.
</p>

> 💡 **Is there a trend between cluster size and shape?**
> * Yes, clusters become more spherical with increasing cluster size 
> * This trend is observed for all the pairs investigated.

<a name="anchor-F4"></a>
<p align="center">
  <img src="https://github.com/user-attachments/assets/9b94f513-e1b1-44ff-906b-110922236185" width="90%" alt="Fig 4" style="margin-bottom: 0px;">
  <br>
  <span style="font-size: 80%;"><strong>Figure 4</strong>.Time evolution of cluster size and sphericity distribution in nonane/butanol. Left: average cluster size vs. time, with error bars as standard deviation and colors indicating sphericity (Φ). The inset shows smaller clusters early in the simulation. Right: boxplots display sphericity distributions for clusters of sizes 10<sup>1</sup> < n ≤ 10<sup>2</sup>, 10<sup>2</sup> < n ≤ 10<sup>3</sup>, and 10<sup>3</sup> < n ≤ 10<sup>4</sup></span>
</p>
        
<p align="justify"> 
Among systems with minimal or partial miscibility gap (nonane/butanol and water/butanol), nearly equal amounts of each nucleating vapor were observed (median X~0.5) as shown in <a href="#anchor-F5">Fig. 5</a> and <a href="#anchor-S3">Fig. S3</a>. Furthermore, a trend was observed in which the spread of mole fraction values decreased with increasing cluster size (as indicated by the decreasing area of the boxplots). In contrast, the water/nonane system exhibited a wide spread of mole fraction values in the small clusters, which is likely caused by the pronounced miscibility gap between the involved molecules (<a href="#anchor-S4">Fig. S4</a>). Interestingly, larger clusters in the water/nonane system displayed mole fraction values close to 0.5. While the observed near-equimolar distribution of nucleating vapors in nonane/butanol and water/butanol clusters is likely due to the low miscibility gap in these systems, the similar behavior in water/nonane may be caused by another interaction, such as the clumping of unary clusters without significant mixing.
</p>

> 💡 **What are the observations on mole fraction for each pair?**
> * Mole fraction of clusters move closer to 0.5 with increasing cluster size.
> * For nonane/butanol and water/butanol, this trend is likely because of the low miscibility gap.
> * For water/nonane and water/butanol, this may be caused by clumping of unary clusters without mixing (need additional analysis, see next sections)

<a name="anchor-F5"></a>
<p align="center">
  <img src="https://github.com/user-attachments/assets/b93a686f-0b3d-42dd-bd60-d59633b3d0a5" width="90%" alt="Fig 5" style="margin-bottom: 0px;">
  <br>
  <span style="font-size: 80%;"><strong>Figure 5</strong>.Time evolution of cluster size and mole fraction distribution in nonane/butanol. Left: average cluster size vs. time, with error bars as standard deviation and colors indicating sphericity (Φ). The inset shows smaller clusters early in the simulation. Right: boxplots display mole fraction distributions for clusters of sizes 10<sup>1</sup> < n ≤ 10<sup>2</sup>, 10<sup>2</sup> < n ≤ 10<sup>3</sup>, and 10<sup>3</sup> < n ≤ 10<sup>4</sup></span>
</p>

### B. Binary Ordering of Molecules in Clusters

<p align="justify"> 
To get a better understanding of the cluster shape and composition, a look into the internal ordering within the cluster is necessary. Radial layers are reported for the largest cluster over time, which were accompanied by cluster snapshots (<a href="#anchor-F6">Fig. 6</a>). The lower-value radial layers signify regions closer to the core while the larger-value radial layers are closer to the cluster surface. Snapshots illustrating the radial layers were captured at 1 ns, 10 ns, and 100 ns to provide a visual representation.
</p>
    
<p align="justify"> 
For the nonane/1-butanol system, majority of clusters were well mixed as most radial layers had mole fraction values close to 0.5, indicated by the grayish color in <a href="#anchor-F6">Fig. 6</a>. This is in agreement with the visual inspection of the nuclei snapshots, where nonane (green spheres) and 1-butanol (yellow spheres) are evenly distributed in the cluster surface (<a href="#anchor-F7">Fig. 7a-c</a>) and the interior of the cluster (<a href="#anchor-S4">Fig. 7d-f</a>), indicating homogeneous mixing between the two nucleating species. Additionally, the observed mixing behavior further verifies that the reluctant co-nucleation reported for nonane and alcohol mixtures is minimized in nonane/1-butanol by the relatively long alkyl tail of 1-butanol. 
</p>
    
<p align="justify"> 
Radial analysis of the water/1-butanol system reveals alternating regions of high water and 1-butanol concentration, indicated by the alternating bluish and reddish regions in the heatmap (<a href="#anchor-F8">Fig. 8</a>). The cluster snapshots clarify this observation as it shows that a simple core-shell structure is observed at the initial stages of nucleation, with water (blue spheres) at the core and 1-butanol (yellow spheres) at the surface (<a href="#anchor-F9">Fig. 9</a>). Over time, another layer of butanol and water is configured, resulting in butanol-water-butanol-water layering. At the later stages, another layer of water-butanol is formed again (<a href="#anchor-F9">Fig. 9</a>). 
</p>

<p align="justify"> 
A water/nonane system was previously explored by <a href="https://doi.org/10.1021/jp011460x" target="_blank">Wagner and Strey (2001)</a>. They observed a two-pathway nucleation mechanism, which suggests that both species nucleate independently in a unary manner. This is attributed to the pronounced miscibility gap between the two molecules. It was proposed that, in a system composed of an immiscible pair, it is likely for heterogeneous-like nucleation to occur, whereby the first species to nucleate serves as a substrate for the nucleation of the other. This hypothesis is supported by our observations, with radial analysis showing deep blue and red hue at the heatmap at all time steps (<a href="#anchor-S5">Fig. S5</a>). Visually, a lens-on-sphere structure was observed, consisting of a large central nonane cluster to which are adsorbed several independent water clusters (<a href="#anchor-S6">Fig. S6a-c</a>). The cross-section confirms the radial analysis as no mixing is observed, and each individual structure is either pure nonane or pure water (<a href="#anchor-S6">Fig. S6d-f</a>). 
</p>

> 💡 **What are the binary ordering of the molecules in each cluster?** 
> * nonane/1-butanol: homogenous mixing 
> * water/1-butanol: core-shell ordering 
> * water/nonane: lens-sphere ordering

<a name="anchor-F6"></a>
<p align="center">
  <img src="https://github.com/user-attachments/assets/66d8d02b-cf98-4672-bfad-1b924fd630f2" width="80%" alt="Fig 6" style="margin-bottom: 0px;">
  <br>
  <span style="font-size: 80%;"><strong>Figure 6</strong>. Heatmap showing mole fraction (X<sub>nonane</sub>) across radial layers of the largest cluster over time in nonane/butanol, with lower-value radial layers near the core and higher-value layers near the surface.</span>
</p>

<a name="anchor-F7"></a>
<p align="center">
  <img src="https://github.com/user-attachments/assets/d812696a-f08b-4714-a174-06882a23b269" width="80%" alt="Fig 7" style="margin-bottom: 0px;">
  <br>
  <span style="font-size: 80%;"><strong>Figure 7</strong>. Snapshot of whole nonane/1-butanol clusters at simulation time (a) 1 ns, (b) 10 ns, and (c) 100 ns, and their cross-section at (d) 1 ns, (e) 10 ns, and (f) 100 ns. The green and yellow spheres represent nonane and 1-butanol molecules, respectively.</span>
</p>

<a name="anchor-F8"></a>
<p align="center">
  <img src="https://github.com/user-attachments/assets/305171f9-b47e-4c40-ba40-a005be41b70e" width="80%" alt="Fig 8" style="margin-bottom: 0px;">
  <br>
  <span style="font-size: 80%;"><strong>Figure 8</strong>. Heatmap showing mole fraction (X<sub>water</sub>) across radial layers of the largest cluster over time in water/butanol, with lower-value radial layers near the core and higher-value layers near the surface.</span>
</p>

<a name="anchor-F9"></a>
<p align="center">
  <img src="https://github.com/user-attachments/assets/2a64c8ab-0db6-45d6-8c5f-82dbb2d88543" width="80%" alt="Fig 9" style="margin-bottom: 0px;">
  <br>
  <span style="font-size: 80%;"><strong>Figure 9</strong>. Snapshot of whole water/1-butanol clusters at simulation time (a) 1 ns, (b) 10 ns, and (c) 100 ns, and their cross-section at (d) 1 ns, (e) 10 ns, and (f) 100 ns. The blue and yellow spheres represent water and 1-butanol molecules, respectively.</span>
</p>

### C. Unary Ordering of Molecules in Clusters

<p align="justify">
While water and nonane exhibit clear segregation in water/nonane systems, the presence of microstructures within clusters formed by systems with minimal or partial miscibility gaps (nonane/1-butanol and water/1-butanol) warrants further investigation. Homogeneous mixing was observed in nonane/1-butanol clusters, but questions remain: Is butanol evenly distributed throughout the entire cluster, or are localized structures present? Similarly, for water/1-butanol, is the core-shell structure strictly segregated, or are there instances of localized clumping? Addressing these questions requires identifying unary clusters within the binary clusters.
</p>
<p align="justify">
To explore these microstructures, fragments within the largest clusters were analyzed. Higher fragmentation indicated fewer unary components were networked within the cluster, likely due to localized miscibility gaps. Results were visualized using line plots to depict the total unary components and stacked bar plots to illustrate the degree of fragmentation. In these bar plots, reddish bars represent less fragmentation (a more networked structure), while bluish bars indicate more fragmentation (a less networked structure).
</p>
<p align="justify">
For water/1-butanol, the butanol component displayed strong networking, as evidenced by red-colored bars for the largest cluster over time (<a href="#anchor-F10">Fig. 10</a>). In contrast, significant fragmentation was observed in the water component, reflected by a wide range of colors from blue to light red (<a href="#anchor-F11">Fig. 11</a>). A 3D representation of the water/1-butanol system, shown in <a href="#anchor-F12">Fig. 12</a>, visually highlights this fragmentation. Conversely, systems with smaller miscibility gaps, such as nonane/1-butanol, exhibited minimal fragmentation. The 1-butanol component showed only a small degree of fragmentation, as demonstrated in supplementary figures (<a href="#anchor-S7">Fig. S7</a> and <a href="#anchor-S8">Fig. S8</a>). These findings suggest that fragmentation is less pronounced in systems with better miscibility, reinforcing the relationship between miscibility gaps and cluster microstructure.
</p>

> 💡 **What are the unary ordering of the molecules in each cluster?** 
> * water/1-butanol
>     - water: high fragmentation
>     - 1-butanol: no fragmentation 
> * nonane/1-butanol 
>     - nonane: no fragmentation 
>     - 1-butanol: low fragmentation


<a name="anchor-F10"></a>
<p align="center">
  <img src="https://github.com/user-attachments/assets/53cea23c-d955-41da-a259-61bc761c901d" width="80%" alt="Fig 10" style="margin-bottom: 0px;">
  <br>
  <span style="font-size: 80%;"><strong>Figure 10</strong>. Fragmentation of 1-butanol within water/butanol clusters over time. Molecules are fragmented when clustering criteria are met. Higher fragmentation indicates fewer unary components forming a network. The gray line shows the total number of molecules in the largest cluster, while stacked bars represent fragment sizes. Bar colors range from red (less fragmentation; more networked unary components) to blue (more fragmentation; fewer networked unary components).</span>
</p>


<a name="anchor-F11"></a>
<p align="center">
  <img src="https://github.com/user-attachments/assets/5a647968-a4f3-4400-bb2c-4b0944e1398a" width="80%" alt="Fig 11" style="margin-bottom: 0px;">
  <br>
  <span style="font-size: 80%;"><strong>Figure 11</strong>. Fragmentation of water within water/butanol clusters over time. Molecules are fragmented when clustering criteria are met. Higher fragmentation indicates fewer unary components forming a network. The gray line shows the total number of molecules in the largest cluster, while stacked bars represent fragment sizes. Bar colors range from red (less fragmentation; more networked unary components) to blue (more fragmentation; fewer networked unary components).</span>
</p>

<a name="anchor-F12"></a>
<p align="center">
  <img src="https://github.com/user-attachments/assets/4cabc819-5983-43a2-8ece-0b60cce42f5f" width="80%" alt="Fig 12" style="margin-bottom: 0px;">
  <br>
  <span style="font-size: 80%;"><strong>Figure 12</strong>. Fragmentation of water molecules in largest water/1-butanol cluster at the last time step, wherein the three largest fragments are colored light blue, blue, orange (in increasing order of fragmentation size).</span>
</p>

## Conclusion
[[back to contents](#contents)]

<p align="justify">
A broad overview is first extracted from the clusters based on sphericity and mole fraction. In this stage of the analysis, clusters were found to be more spherical with increasing cluster size regardless of miscibility. While more miscible species had less mole fraction variability from an equimolar composition. Substructural features were also observed in terms of orientational ordering in each cluster. Diverse clustering structures of three binary combinations from the water/nonane/1-butanol pool were revealed using molecular dynamics. To summarize: nonane/1-butanol resulted in homogeneously-mixed clusters due to their minimal miscibility gap. Meanwhile, water/1-butanol portrayed more distinct core-shell structures. Finally, water/nonane assumed a lens-on-sphere configuration composed of a large central nonane cluster to which several smaller water clusters were adsorbed, without any observed mixing.
</p>
<p align="justify">
From these findings, we observe that (a) highly miscible pairs form homogeneously-mixed clusters, (b) partially miscible pairs can form component-enriched regions as a means to maximize favorable interactions, and (c) completely immiscible pairs exhibit heterogeneous-like nucleation, wherein each component nucleates independently, and the first cluster serves as the substrate for the nucleation of the other. In partially miscible pairs, network-like microstructures and fragmented pockets can occur within seemingly uniform clusters. Taken together, the findings in this work have a direct impact on nucleation calculations, as we have shown that binary mixtures exhibit microheterogeneity and non-sphericity, and thus do not necessarily obey classical theories. Current theory has been shown to make nonphysical predictions, and the structural information that we have presented in this study should be considered in the development of future models.
</p>

## Appendix
[[back to contents](#contents)]

<a name="anchor-S1"></a>
<p align="center">
  <img src="https://github.com/user-attachments/assets/99d862a3-4ea6-4b64-b521-6a36e4450400" width="90%" alt="Fig S1" style="margin-bottom: 0px;">
  <br>
  <span style="font-size: 80%;"><strong>Figure S1</strong>. Time evolution of cluster size and sphericity distribution in <i>wn</i>. Left: average cluster size vs. time, with error bars as standard deviation and colors indicating sphericity (Φ). The inset shows smaller clusters early in the simulation. Right: boxplots display sphericity distributions for clusters of sizes 10<sup>1</sup> < n ≤ 10<sup>2</sup>, 10<sup>2</sup> < n ≤ 10<sup>3</sup>, and 10<sup>3</sup> < n ≤ 10<sup>4</sup>.</span>
</p>

<a name="anchor-S2"></a>
<p align="center">
  <img src="https://github.com/user-attachments/assets/6c22e4bf-2d9e-4a1e-bb63-2f032f79d033" width="90%" alt="Fig S2" style="margin-bottom: 0px;">
  <br>
  <span style="font-size: 80%;"><strong>Figure S2</strong>. Time evolution of cluster size and sphericity distribution in <i>wb</i>. Left: average cluster size vs. time, with error bars as standard deviation and colors indicating sphericity (Φ). The inset shows smaller clusters early in the simulation. Right: boxplots display sphericity distributions for clusters of sizes 10<sup>1</sup> < n ≤ 10<sup>2</sup>, 10<sup>2</sup> < n ≤ 10<sup>3</sup>, and 10<sup>3</sup> < n ≤ 10<sup>4</sup>.</span>
</p>

<a name="anchor-S3"></a>
<p align="center">
  <img src="https://github.com/user-attachments/assets/7b252d63-c630-47ea-95df-628d015b1df1" width="90%" alt="Fig S3" style="margin-bottom: 0px;">
  <br>
  <span style="font-size: 80%;"><strong>Figure S3</strong>. Time evolution of cluster size and mole fraction distribution in <i>wn</i>. Left: average cluster size vs. time, with error bars as standard deviation and colors indicating sphericity (Φ). The inset shows smaller clusters early in the simulation. Right: boxplots display mole fraction distributions for clusters of sizes 10<sup>1</sup> < n ≤ 10<sup>2</sup>, 10<sup>2</sup> < n ≤ 10<sup>3</sup>, and 10<sup>3</sup> < n ≤ 10<sup>4</sup>.</span>
</p>

<a name="anchor-S4"></a>
<p align="center">
  <img src="https://github.com/user-attachments/assets/7e6398ad-7a6b-4fe0-bffa-8669b9b2caf6" width="90%" alt="Fig S4" style="margin-bottom: 0px;">
  <br>
  <span style="font-size: 80%;"><strong>Figure S4</strong>. Time evolution of cluster size and mole fraction distribution in <i>wb</i>. Left: average cluster size vs. time, with error bars as standard deviation and colors indicating sphericity (Φ). The inset shows smaller clusters early in the simulation. Right: boxplots display mole fraction distributions for clusters of sizes 10<sup>1</sup> < n ≤ 10<sup>2</sup>, 10<sup>2</sup> < n ≤ 10<sup>3</sup>, and 10<sup>3</sup> < n ≤ 10<sup>4</sup>.</span>
</p>

<a name="anchor-S5"></a>
<p align="center">
  <img src="https://github.com/user-attachments/assets/bcc138ad-3b46-411a-a280-11c895e016a9" width="80%" alt="Fig S5" style="margin-bottom: 0px;">
  <br>
  <span style="font-size: 80%;"><strong>Figure S5</strong>. Heatmap showing mole fraction (X<sub>water</sub>) across radial layers of the largest cluster over time in water/nonane, with lower-value radial layers near the core and higher-value layers near the surface.</span>
</p>

<a name="anchor-S6"></a>
<p align="center">
  <img src="https://github.com/user-attachments/assets/b3ac3960-cdf2-4cee-8b40-4d87847fb304" width="80%" alt="Fig S6" style="margin-bottom: 0px;">
  <br>
  <span style="font-size: 80%;"><strong>Figure S6</strong>. Snapshot of whole water/nonane clusters at simulation time (a) 1 ns, (b) 10 ns, and (c) 100 ns, and their cross-section at (d) 1 ns, (e) 10 ns, and (f) 100 ns. The blue and green spheres represent water and nonane molecules, respectively.</span>
</p>

<a name="anchor-S7"></a>
<p align="center">
  <img src="https://github.com/user-attachments/assets/9495b02b-0c17-471e-8396-43bdd4e031e7" width="80%" alt="Fig S7" style="margin-bottom: 0px;">
  <br>
  <span style="font-size: 80%;"><strong>Figure S7</strong>. Fragmentation of nonane within nonane/butanol clusters over time. Molecules are fragmented when clustering criteria are met. Higher fragmentation indicates fewer unary components forming a network. The gray line shows the total number of molecules in the largest cluster, while stacked bars represent fragment sizes. Bar colors range from red (less fragmentation; more networked unary components) to blue (more fragmentation; fewer networked unary components).</span>
</p>

<a name="anchor-S8"></a>
<p align="center">
  <img src="https://github.com/user-attachments/assets/db121cc7-c5aa-4f40-b234-73d6b4714392" width="80%" alt="Fig S8" style="margin-bottom: 0px;">
  <br>
  <span style="font-size: 80%;"><strong>Figure S8</strong>. Fragmentation of butanol within nonane/butanol clusters over time. Molecules are fragmented when clustering criteria are met. Higher fragmentation indicates fewer unary components forming a network. The gray line shows the total number of molecules in the largest cluster, while stacked bars represent fragment sizes. Bar colors range from red (less fragmentation; more networked unary components) to blue (more fragmentation; fewer networked unary components).</span>
</p>

<a name="anchor-S9"></a>

https://github.com/user-attachments/assets/1c8655a1-e64f-4edd-a22f-f7d815077f75

<video width="640" height="360" controls>
  <source src="https://github.com/user-attachments/assets/1c8655a1-e64f-4edd-a22f-f7d815077f75" type="video/mp4">
  Your browser does not support the video tag.
</video>
<p align="left" style="font-size: 80%;">
    <strong>Figure S9</strong>. Video of nonane/1-butanol simulation.
</p>
