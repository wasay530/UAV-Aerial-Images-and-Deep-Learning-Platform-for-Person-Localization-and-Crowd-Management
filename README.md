## Person Localization and Crowd Counting using Deep Learning (Aerial images) 

* Person localization and crowd sourcing in aerial images as many applications including crowd safety and security management, people management in disasters, and person movement in an epidemic disease situation. 
* Ariel images have an issue of cluttered background, low-resolution quality, and various environment and lighting conditions, which increase complexity levels of localization and recognition. 
* Deep learning and a UAV Raspberry Pi-based platform for the acquisition and localization of crowds considering the different orientations of the UAV and heterogeneous environmental factors. 
* The proposed system consists of: the transfer of the image from the UAV to the processing system, image enhancement, features extraction for object detection and
recognition, and performance comparison of different detection and recognition algorithms. 
* We collect a large local environment dataset for better accuracy. 
* We compare the performance of Haar-Cascade, template matching, YOLO, and Mask-Region Based Convolutional Neural Networks. 
* The aforementioned results show that YOLO performs better for crowd detection and localization.

## Proposed Platform for Person Localization and Crowd Sourcing
<p align="center">
<img src = "https://github.com/wasay530/UAV-Aerial-Images-and-Deep-Learning-Platform-for-Person-Localization-and-Crowd-Management/blob/6dfa0b6e17a358774832b734cbcf185bf1354680/block_diagram.png" title= "Proposed Architecture of Deep Learning Platform for Person Localization and Crowd Management in UAV Aerial Images" width="700" height="300" alt>
</p>
<p align="center">
  <em>Fig. 1: Proposed Architecture of Deep Learning Platform for Person Localization and Crowd Management in UAV Aerial Images</em>  
</p>

<p align="center">
<img src = "https://github.com/wasay530/UAV-Aerial-Images-and-Deep-Learning-Platform-for-Person-Localization-and-Crowd-Management/blob/6dfa0b6e17a358774832b734cbcf185bf1354680/gui.png" title= "GUI (Graphic User Interface) of Person Localization and Crowd Sourcing in Aerial Images" width="700" height="300" alt>
</p>
</p>
<p align="center">
  <em>Fig. 2: GUI (Graphic User Interface) of Person Localization and Crowd Sourcing in Aerial Images</em>  
</p>

#### Results ####
Algorithms                 | No of Person (Detected)
-------------------------  | ------------------------------
Haar Cascade               | 1530
You Only Look Once (YOLO)  | 2524
Mask RCNN Algorithm        | 2495

<p align="center">
<img src = "https://github.com/wasay530/UAV-Aerial-Images-and-Deep-Learning-Platform-for-Person-Localization-and-Crowd-Management/blob/6dfa0b6e17a358774832b734cbcf185bf1354680/Results%20(1).PNG" title= "Results of Person Detection and Crowd Sourcing" width="700" height="350" alt>
</p>
</p>
<p align="center">
  <em>Fig. 3: Results of Person Detection and Crowd Sourcing</em>  
</p>

<p align="center">
<img src = "https://github.com/wasay530/UAV-Aerial-Images-and-Deep-Learning-Platform-for-Person-Localization-and-Crowd-Management/blob/6dfa0b6e17a358774832b734cbcf185bf1354680/combine_person_localization_crowd_sourcing%202%20(1).PNG" title= "Graph of actual persons, and haar-cascade, YOLO, mask RCNN algorithm detected persons" width="700" height="350" alt>
</p>
</p>
<p align="center">
  <em>Fig. 4: Graph of actual persons, and haar-cascade, YOLO, mask RCNN algorithm detected persons</em>  
</p>
