---
layout: project
type: project
image: img/STScI-01EVTA34C19C9A91CDPTB70GNS.jpeg
title: "Finding Supernovae"
date: 2023
published: true
labels:
  - Machine Learning
  - Supernovae
  - Python
summary: "My mentor and I trained a convolutional neural network (CNN) to spot supernovae on mock JWST data from Vela
Cosmological Simulations."
---
<img class="img-fluid" src="Screen Shot 2023-04-30 at 11.56.28 AM.png">


Supernovae are luminous explosions of stars that can be seen billions of light years away. 
Scientists study these events to learn more about the history and expansion of the universe. 
The James Webb Space Telescope (JWST) was launched on December 25, 2021 and with its large 6.5-meter 
mirror and ability to measure longer wavelengths of infrared light, we can see farther into the universe 
than ever before. 

Here we trained a convolutional neural network (CNN) to spot supernovae on mock JWST data from Vela Cosmological
Simulations. We generated two nearly identical sets of mock images, with and without noise. For every image in 
each set, we created four copies with different NIRCam bandpass filters (F115W, F150W, F277W, F444W). 
The presence and positions of the planted supernovae were randomly chosen, but consistent between each copy. 
For a sanity check, we use the set without noise as an idealized test. With the noise set, we found that 
the neural network identified planted supernovae with a 0.98 accuracy, identified a supernova when one was 
not planted with a 0.2 accuracy, did not identify a planted supernova with a 0.2 accuracy, and did not identify 
a supernova when one was not planted with a 0.98 accuracy. The results suggest the network is efficient, with 
little inaccuracies. We plan to succeed this project and use the network on real data from the COSMOS survey 
by JWST, to streamline our ability to spot the most distant supernovae.
