---
layout: post
title: "Plant Drought Stress Image Processing Summer Project"
tags: project
---



 Over the summer I did some work with a research project exploring the use of drones equipped with cameras to analyze plants for agriculture. Altough I didn't get to play with drones, I did do some data collection and image processing. My goal was to use images of plants to determine if they were “thirsty” i.e. drought stressed.




![image capture](/assets/images/srp_img_capture.jpg)

 Image capturing set-up in the greenhouse.
 

## Overview



 The first thing I had to do was gather some image data of plants, half of which would be drought-stressed. For this task I was given a Raspberry Pi with thermal (IR) and color (VL) cameras.
 [This setup
 was used as a prototype for something small and portable that could be attached to a drone. I visited the plants at a greenhouse multple times a day to capture the images. Throughout the week I developed and improved a
 [Python script](https://github.com/austinpursley/Summer-Research-Plant-Drought-Stress-Image-Processing/blob/master/capture_imgs/capture_imgs.py) 
 for streamlining the image capturing with the Raspberry Pi. A white background was placed behind the plants to help the future image processing.](/assets/images/pi_and_cameras.jpg)




![plant image collection](/assets/images/srp_img_collection.png)

 Collection of plant images captured.
 


 With the plant images collected, the "region of interest" (ROIs) could be determined. In this case the ROI was simply the plant and the challenge was to determine the set of pixels that corresponded to it. Using a
 [familiar technique](image_processing_thermal.html) 
 , I almost completely automated this by applying simple threshold and morphological operations (with Python + OpenCV). However, a set of threshold values didn't work for all images so there was a manual element in changing the values in order to get correct ROIs for all the images.




![region of interest](/assets/images/srp_roi.png)

 Examples of finding ROIs.
 


 With the ROIs I could find image features. I chose the hue color value for VL images and plant surface temperature for IR images. After plotting those feature's mean and variance over time I determined there wasn't any strong correlation between those values and the amount of time it had been since the plant had been watered. Therefore the results were inconclusive.




![plant image feature plots](/assets/images/srp_plots.png)

 Sample plots of image features (see GitHub for more).
 

## Conclusion



 Altough not very advanced, this was a fun project where I had to do all the data collection and analysis myself. That meant I had to consider the quality of the data I was collecting and how to make it good for processing. Presenting the data/results was also a challenge and I found Python's
 [matplotlib](https://matplotlib.org/) 
 to be a great tool for making neat plots and figures.




 The
 [Github](https://github.com/austinpursley/Summer-Research-Plant-Drought-Stress-Image-Processing) 
 includes all the data, code, and a report with more details.



  

