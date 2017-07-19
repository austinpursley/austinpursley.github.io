(function() {

var img = document.getElementById('slideshow').firstChild;
img.onload = function() {
	alert('test 2')
    if(img.height > img.width) {
        img.height = '100%';
        img.width = 'auto';
    }
};

}());