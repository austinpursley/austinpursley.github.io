//from: Adapted from David Thomas's code on Stack Exchange 
//https://stackoverflow.com/questions/26443828/press-left-and-right-arrow-to-change-image

function imgCycle(e) { //e is the event.
	var elem = document.getElementById('numImg');
	var numImg = parseInt(elem.innerText);
	if (numImg == 1) {
		return false;
	}
	var hike_id = document.getElementById('hike_id').innerHTML;
	var imgs = [];
	//var imgs = ["1.jpg", "2.jpg",...]
	for (i = 0; i < numImg; i++) {
		imgs.push(hike_id + "/" + i.toString() + ".jpg");
	}
	// reference to the img element:
	var imgElement = document.getElementById('imgClickAndChange'),
	// finding the string of the src after the last '/' character:
	curImg = imgElement.src.split('/').pop(),
	// finding that string from the array of images:
	curIndex = imgs.indexOf(hike_id + "/" + curImg),
	// initialising the nextIndex variable:
    nextIndex;

    // if we have a keyCode (therefore we have a keydown or keyup event:
    if (e.keyCode) {
        // we do different things based on which key was pressed:
        switch (e.keyCode) {
            // keyCode 37 is the left arrow key:
            case 37:
                // if the current index is 0 (the first element in the array)
                // we next show the last image in the array, at position 'imgs.length - 1'
                // otherwise we show the image at the previous index:
                nextIndex = curIndex === 0 ? (imgs.length - 1) : curIndex - 1;
                break;
                // keyCode 39 is the right arrow key:
            case 39:
                // if curIndex + 1 is equal to the length of the images array,
                // we show the first element from the array, otherwise we use the next:
                nextIndex = curIndex + 1 === imgs.length ? 0 : curIndex + 1; 
                break;
			default:
				nextIndex = curIndex; 
				break;
        }
    } 
	else if (e.target.className == 'round previous') {
		nextIndex = curIndex === 0 ? (imgs.length - 1) : curIndex - 1; 
	} 
	else if (e.target.className == 'round next') {
		nextIndex = curIndex + 1 === imgs.length ? 0 : curIndex + 1; 
	}
	else {
		nextIndex = curIndex;
	}
    imgElement.src = imgs[nextIndex];
}

//  for pressing a key on keyboard
document.body.addEventListener('keydown', imgCycle);
//  for clicking the next and previous buttons
/* document.getElementById("templateArea").addEventListener("click", imgCycle(e) {
	//e.target is the clicked element!
	if(e.target && e.target.class == "next") {
		//List item found!  Output the ID!
		alert('smell beans');
	}
}); */
// document.querySelector(".next").addEventListener('click', imgCycle);
// document.querySelector(".previous").addEventListener('click', imgCycle);
