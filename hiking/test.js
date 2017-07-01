/* var hike_image = document.querySelector('#hiking_image');

//1

var handleClick = function (event) {
	//do something!
};

var button = document.querySelector('#big_button');

button.addEventListener('click', handleClick);

//2

var req = new XMLHttpRequest();
req.onload = function (event) {...};
req.open('get', 'some-file.txt', true);
req.send(); */

alert('Hello World');

//from: https://stackoverflow.com/questions/26443828/press-left-and-right-arrow-to-change-image
/* var imgs = ["images/20140621.jpg", "images/20140621_150846.jpg"];

function changeImage(dir) {
    var img = document.getElementById("imgClickAndChange");
    img.src = imgs[imgs.indexOf(img.src) + (dir || 1)] || imgs[dir ? imgs.length - 1 : 0];
}

document.onkeydown = function(e) {
    e = e || window.event;
    if (e.keyCode == '37') {
        changeImage(-1) //left <- show Prev image
    } else if (e.keyCode == '39') {
        // right -> show next image
        changeImage()
	}
} */


//from: Adapted from David Thomas at Stack Exchange 
//https://stackoverflow.com/questions/26443828/press-left-and-right-arrow-to-change-image
function imgCycle(e) {
    // obviously use your own images here:
    var imgs = ["20140621.jpg", "20140621_150846.jpg"],
        // reference to the img element:
        imgElement = document.getElementById('imgClickAndChange'),
        // finding the string of the src after the last '/' character:
        curImg = imgElement.src.split('/').pop(),
        // finding that string from the array of images:
        curIndex = imgs.indexOf(curImg),
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
        }
        // if we don't have a keyCode, we check if the event-type (in lowercase)
        // is a mousedown:
    } else if (e.type.toLowerCase() === 'mousedown') {
        // I'm assuming you'd like to advance to the next image, rather
        // than regress to the previous (same check as above):
        nextIndex = curIndex + 1 === imgs.length ? 0 : curIndex + 1;
    } else {
		nextIndex = curIndex;
	}
    // setting the src of the image to the relevant URL + the string from the array
    // at the 'nextIndex':
    imgElement.src = 'images/' + imgs[nextIndex];
}

// binding a mousedown event-handler to the 'img' element:
document.getElementById('imgClickAndChange').addEventListener('mousedown', imgCycle);
// binding the keydown event-handler to the 'body' element:
document.body.addEventListener('keydown', imgCycle);
       