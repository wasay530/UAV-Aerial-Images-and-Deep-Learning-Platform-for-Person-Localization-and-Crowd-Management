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
<img src = "https://github.com/wasay530/-KAU-COVID19-AR-Dataset/blob/acd6c0007e57067e594fd107eac76d515b4ab8ad/mobile_position.png" title= "Dataset (KAU-COVID19-AR-Dataset):each activity" width="800" height="400" alt>
</p>

#### Results ####
Algorithms                 | No of Person (Detected)
-------------------------  | ------------------------------
Haar Cascade               | 1530
You Only Look Once (YOLO)  | 2524
Mask RCNN Algorithm        | 2495
