---
layout: post
title: "Image Processing Part 1: Skin Temperature From Thermal Images"
tags: project
---



 The senior design project I have been working on in school is a "smart mirror". 
 Equipped with a thermal and RGB camera, its primary goal is to analyze a user's face and give health feedback. 
 The subsystem I was responsible for was image processing and
 my goal was to analyze the images to obtain health metrics.
 Here I go over getting a skin tempeprature metric from thermal images.




![fever](/assets/images/fever.png)

 Ever wanted your mirror to tell you if you're catching a fever? No? Okay, well...
 

## Skin Temperature



 Skin temperature was an interesting health metric to try and capture because it could perhaps approximate internal body temperatures. 
 Changes in body temperature may be a health concern such as a fever so it seemed important to measure and track.



## Process



![flow diagram](/assets/images/thermal.png)

 Diagram for the process of getting skin temperature.
 


 The thermal images come from a
 [FLiR Lepton](http://www.flir.com/cores/lepton/) 
 and have dimensions of 80x60 pixels. 
 Each pixel has a value and the higher the value means the hotter the temperature.
 I used these images to try and approximate skin temperature value.




 Altough it may be intuitive to just take the highest value as the skin temperature, it is not guaranteed that a person will be the warmest thing in the image. 
 There may be a light bulb, a candle, or a cup of coffee in the background. 
 Therefore some simple image processing techniques are needed to remove these "hot spots".




 The first step is to find the median of the thermal image and use it as the value for a
 [threshold](https://docs.opencv.org/3.3.1/d7/d4d/tutorial_py_thresholding.html) 
 . 
 There are several other threshold values to choose from e.g. the average pixel value or using Otsu's method.
 I use the median because it is less affected by very hot or cold objects caught in the image. 
 With a threshold, any pixel with a value over that value will be white and any under will be black. Here I refer to the white part as the "mask".




![skin temperature process images](/assets/images/thermal_img_process.png)

 Visualized Process: Original, Thresholded, Open+Close, and Orginal Masked
 


 The mask needs to be 'adjusted', so the second step is to apply some
 [morphological transformations](https://docs.opencv.org/trunk/d9/d61/tutorial_py_morphological_ops.html) 
 . 
 The first is called an open and it will remove smaller white areas caused by warm background objects.
 The second transformation is called a close and it does exactley what it sounds like; 
 any holes in the mask caused by colder objects like glasses or thick beards will be closed up.




 Now the mask approximately covers the person in the image. 
 The final step is to use this to "mask" the original image and only look for the highest pixel value in that area. 
 This highest value will then be our skin temperature metric and the process is complete.



## Corner Cases



 My assumption is that the there is one person in the image and that they are the prominent figure in the image. 
 Any object hotter than skin that is in front or on the edge of that person will not be removed from the mask and cause an error. 
 The person should also consistently either wear or not-wear glasses. 
 This is because the glass blocks one of the warmest areas of the face from the view of the thermal camera and therefore one reading without glasses may be higher than without.




[Github](https://github.com/austinpursley/ECEN-403-Smart-Mirror-Image-Analysis/tree/master/thermal) 
 , for C++, OpenCV code.



  

