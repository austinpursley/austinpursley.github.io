<?php
	// PHP Code that gets the images in the directory
	// ------
	
	$imgArr = 'var imgs = Array(';
	
	foreach ($images as $img)
	{
		$imgArr .= " '{$img}',\n"}
	}