---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: Home
---

# My Work

## Medical Image Analysis

### Nuclei Segmentation

<figure>
  <img src="images/ctc-nuclei-segmentation/CTC_challenge_volume_sequence_01.png" alt="Nuclei segmentation" style="max-width:100%; height:auto;">
  <figcaption style="text-align: justify; max-width: 800px; margin: 0 auto;">
    <b>Nuclei instance segmentation on microscopy images of Drosophila embryo.</b> Each row corresponds to a time point frame of a 3D movie of a Drosophila embryo, showing the MIP projection (left) and the corresponding segmentation (right). Each color represents a different cell nuclei. Segmentations were obtained using a methodology based on the U-Net Deep Learning model (<a href="https://doi.org/10.1109/CAI54212.2023.00137">Rojas et al., 2023</a>)
  </figcaption>
</figure>


### Tracking of Human Sperm Samples

### WSI analysis

### Cancer Lesion Segmentation on CT images

<figure style="text-align: center;">
  <video src="images/hitl-medsam-evolution/hitl_medsam_evolution.mp4" width="600" controls loop autoplay muted>
    Your browser does not support the video tag.
  </video>
  <figcaption style="text-align: justify; max-width: 800px; margin: 0 auto;">
    <b>Evolution of the MedSAM performance with annotation cycles</b>. (a) Distribution of Dice scores in terms of lesion size, obtained for the retrained MedSAM after each annotation cycle. Each point represents a bounding box in the testing set. (b) Probability distribution of the Dice after each annotation cycle, estimated using KDE with Gaussian kernels.
  </figcaption>
</figure>

<figure style="text-align: center;">
  <img src="images/hitl-medsam-evolution/medsam_outputs.svg" alt="MedSAM output segmentations" style="width: 100%; max-width: 600px; height: auto; display: block; margin: 0 auto;">
  <figcaption style="text-align: justify; max-width: 800px; margin: 0 auto;">
    <b>Comparison between predicted (orange) and human-expert (yellow) segmentations.</b> Fine-tuned MedSAM model receives an image slice and a bounding box (cyan) to produce an output segmentation mask. Similarity betwenn predicted and human-expert segmentations are measured using the Dice score (DSC). From top to bottom, lung tumors, liver tumors, and adenopathies are shown.
  </figcaption>
</figure>

## Other stuff

## Automation of Parquemet Requests

## Text analysis from Tweets (Use Case: Politics!)

