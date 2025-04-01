---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: Home
---

# My Work

## Medical Image Analysis

### Nuclei Segmentation

### Tracking of Human Sperm Samples

### WSI analysis

### Cancer Lesion Segmentation on CT images

<figure>
  <video src="images/hitl_medsam_evolution.mp4" width="600" controls loop autoplay muted>
    Your browser does not support the video tag.
  </video>
  <figcaption>
    <b>Evolution of the MedSAM performance with annotation cycles</b>. (a) Distribution of Dice scores in terms of lesion size, obtained for the retrained MedSAM after each annotation cycle. Each point represents a bounding box in the testing set. (b) Probability distribution of the Dice after each annotation cycle, estimated using KDE with Gaussian kernels.
  </figcaption>
</figure>

__Evolution of the MedSAM performance with annotation cycles__. (a) Distribution of Dice scores in terms of lesion size, obtained for the retrained MedSAM after each annotation cycle. Each point represents a bounding box in the testing set. (b) Probability distribution of the Dice after each annotation cycle, estimated using KDE with Gaussian kernels.

![MedSAM output examples](images/medsam_outputs.svg)

__Comparison between predicted (orange) and human-expert (yellow) segmentations.__ Fine-tuned MedSAM model receives an image slice and a bounding box (cyan) to produce an output segmentation mask. Similarity betwenn predicted and human-expert segmentations are measured using the Dice score (DSC). From top to bottom, lung tumors, liver tumors, and adenopathies are shown.


## Other stuff

## Automation of Parquemet Requests

## Text analysis from Tweets (Use Case: Politics!)

