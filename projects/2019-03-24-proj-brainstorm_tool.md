---
layout: post
title: "Word Mix Creativity Trick in Python"
tags: project
---



 Unrelated ideas can meet and produce better ideas. I think I got that concept from
 [this TED talk](https://www.ted.com/talks/shimpei_takahashi_play_this_game_to_come_up_with_original_ideas?referrer=playlist-simple_ways_to_spark_your_creativity#t-123642) 
 a long time ago. It must of stuck with me because I was compelled to throw together a Python script to help with that same creative technique.




![image_alt](/assets/images/image_name.jpg)

 caption
 

## Overview



 It starts with a list of words the program can sample from. I defined my own list with a mix of buzzwords and terms related to engineering and science. The program will ask "How many random subjects?", meaning how many words from your list do you want to brainstorm with (I found anything over 3 to be distracting). Then the program will output the set number of words, give an oppurtunity to review the words, and finally let you start typing away ideas. I wanted to add a time limit to encourage entering whatever ideas first come to mind; there is a vestige of one in the program, however it is not a hard time limit and I ran out of patience trying to get it to work.
   

 The ideas entered are written to a text document, an example of mine you can see below.



`Date: 2018-09-12
   

 Subjects: VL camera, armadillo armour, Foot pedal,
   

 17:27:03 A foot pedal for proffesional photographers that can tun settings with. Or maybe like an under shoe sensor where they can tap in a certain way. all hands free
   

 17:27:43 You put a go-pro in some transparent armoured ball and let it go off a mountain side or in the ocean and hope someone finds it or whatever
   

 17:28:25 A foot pedal for a TV. foot remote
   

 17:28:52 foot pedal for gaming, just for extra fun
   

 17:29:13 x-ray of armadillo armour
   

 17:30:18 A smell camera? e-nose array? pugnant photography?`

 I couldn't tell you if this is actually useful or if it's just another ineffective way to
 [force creativity](https://www.youtube.com/watch?v=9C_HReR_McQ) 
 . But it's kinda fun.




 See the
 [GitHub](https://github.com/austinpursley/brainstorm_tool) 
 to try it out.



