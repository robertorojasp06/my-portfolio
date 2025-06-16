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
  <img src="images/ctc-nuclei-segmentation/CTC_challenge_volume_sequence_01_short.png" alt="Nuclei segmentation" style="max-width:100%; height:auto;">
  <figcaption style="text-align: justify; max-width: 800px; margin: 0 auto;">
    <b>Nuclei instance segmentation on microscopy images of Drosophila embryo.</b> First time point frame of a 3D movie of a Drosophila embryo, showing the MIP projection (left) and the corresponding segmentation (right). Each color represents a different cell nuclei. Segmentations were obtained using a methodology based on the U-Net Deep Learning model (<a href="https://doi.org/10.1109/CAI54212.2023.00137">Rojas et al., 2023</a>)
  </figcaption>
</figure>


### Tracking of Sperm Samples

<figure style="text-align: center;">
  <video src="images/pymotility/fish/results/fish_video.mp4" style="max-width: 100%; height: auto;" controls loop autoplay muted>
    Your browser does not support the video tag.
  </video>
  <figcaption style="text-align: justify; max-width: 800px; margin: 0 auto;">
    <b>Tracking of fish sperm samples</b>. Sperm heads are segmented using the AI U-net architecture and Sperm tracks are constructed according to the minimum distance criteria between heads in time. Tracks are then classified according to its speed into Progressive (green, VCL >= 26.4 um/s) and Immotile (red, VCL < 26.4 um/s, VSL <= 26.4 um/s) classes. 
  </figcaption>
</figure>


### WSI analysis

### Cancer Lesion Segmentation on CT images

<figure style="text-align: center;">
  <video src="images/hitl-medsam-evolution/hitl_medsam_evolution.mp4" style="max-width: 100%; height: auto;" controls loop autoplay muted>
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


<figure style="text-align: center;">
  <img src="images/ct-tumor-segmentation/nnunet_segmentations.png" alt="Nuclei segmentation" style="width: 600px; max-width:100%; height:auto; display: block; margin: 0 auto;">
  <figcaption style="text-align: justify; max-width: 800px; margin: 0 auto;">
    <b>Lung and Liver tumors identified using AI.</b> Segmentations were obtained using the nnUNet model fine-tuned on CT images from the Clinical Hospital of the University of Chile (HCUCH). Tumors are overlaid in yellow for lung (a,d) and liver (b,c,e,f). 
  </figcaption>
</figure>


## Other projects

### Automation of Parquemet Requests

<figure style="text-align: center;">
  <img src="images/parquemet-requests/demo.gif" alt="Parquemet requests" style="width: 600px; max-width:100%; height:auto; display: block; margin: 0 auto;">
  <figcaption style="text-align: justify; max-width: 800px; margin: 0 auto;">
    <b>Automation of Parquemet request to apply for the use of soccer fields.</b> This script is scheduled to run every monday at 7 AM to make the request automatically. Selenium was used to automate the use of the web browser.
  </figcaption>
</figure>

### Text analysis from Political Tweets

<figure style="text-align: center;">
  <img src="images/twitter-analysis/wordclouds_boric_kast.png" alt="Twitter analysis" style="width: 600px; max-width:100%; height:auto; display: block; margin: 0 auto;">
  <figcaption style="text-align: justify; max-width: 800px; margin: 0 auto;">
    <b>Wordcloud analysis.</b> Wordclouds computed from the 3200 most recent tweets from the accounts of <a href="https://es.wikipedia.org/wiki/Gabriel_Boric">Gabriel Boric</a> and <a href="https://es.wikipedia.org/wiki/Jos%C3%A9_Antonio_Kast">Jose Antonio Kast</a>  (obtained on 2022-08-15).
  </figcaption>
</figure>

<figure style="text-align: center;">
  <img src="images/twitter-analysis/tweets_count_boric_kast.png" alt="Twitter analysis" style="width: 600px; max-width:100%; height:auto; display: block; margin: 0 auto;">
  <figcaption style="text-align: justify; max-width: 800px; margin: 0 auto;">
    <b>Timeseries analysis.</b> Timeseries of tweets count, showing the number of tweets posted each day from the accounts of Gabriel Boric and Jose Antonio Kast (obtained on 2022-10-05).
  </figcaption>
</figure>

<figure style="text-align: center;">
  <img src="images/twitter-analysis/sentiment_distributions.png" alt="Twitter analysis" style="width: 600px; max-width:100%; height:auto; display: block; margin: 0 auto;">
  <figcaption style="text-align: justify; max-width: 800px; margin: 0 auto;">
    <b>Sentiment analysis.</b> Distribution of sentiment scores (between 0 and 1) obtained for each tweet using the <a href="https://github.com/cjhutto/vaderSentiment">VADER</a> algorithm (obtained on 2022-10-05). As this tool only supports english text, we use the <a href="https://es.wikipedia.org/wiki/Jos%C3%A9_Antonio_Kast">googletrans</a> python library (makes requests to the Google Translate API) to translate tweets from spanish to english.
  </figcaption>
</figure>

<figure style="text-align: center;">
  <img src="images/twitter-analysis/tweets_count_izkia.png" alt="Twitter analysis" style="width: 600px; max-width:100%; height:auto; display: block; margin: 0 auto;">
  <figcaption style="text-align: justify; max-width: 800px; margin: 0 auto;">
    <b>Timeseries analysis.</b> Timeseries of tweets count, showing the number of tweets posted each day from the accounts of <a href="https://es.wikipedia.org/wiki/Izkia_Siches">Izkia Siches</a> (obtained on 2022-10-05).
  </figcaption>
</figure>