window.onload = function(){
	contain_img();
};

$(document).ready(function() {
	window.addEventListener("resize", contain_img);
	document.body.addEventListener('keydown', imgCycle);
});

// Even listener for hike page click and image cycle buttons.
//This comes from David Walsh's website article "How JavaScript Even Delegation Works"
//https://davidwalsh.name/event-delegate
document.getElementById("hiking_page").addEventListener("click", function(e) {
	if(e.target && e.target.nodeName == "BUTTON") {
		imgCycle(e);
	}
});

//Adapted from David Thomas's code on Stack Exchange 
//https://stackoverflow.com/questions/26443828/press-left-and-right-arrow-to-change-image
function imgCycle(e) { //e is the event.
	left_arrow_key = (e.keyCode == 37);
	right_arrow_key = (e.keyCode == 39);
	pre_button = (e.target.className == 'previous');
	nxt_button = (e.target.className == 'next');
	
	if (left_arrow_key || right_arrow_key || pre_button || nxt_button) {
		var hike_id = document.getElementById('hike_id').innerHTML;
		$.getJSON("hiking_data.json", function(data) {
			$.each(data.hiking_places, function(key, place) {
				
				if (hike_id == place.id) {
					var imgs = place.img_array,
					imgElement = document.getElementById('imgClickAndChange'),
					curImg = imgElement.src.split('/').pop(),
					curIndex = imgs.indexOf(curImg),
					nextIndex;
					
					if (left_arrow_key || pre_button) {
						nextIndex = curIndex === 0 ? (imgs.length - 1) : curIndex - 1;
					}
					else if (right_arrow_key || nxt_button) {
						nextIndex = curIndex + 1 === imgs.length ? 0 : curIndex + 1; 
					}
					else {
						nextIndex = curIndex;
					}
					
					var newImg = new Image();
					newImg.onload = function() {
						imgElement.src = this.src;
						contain_img();
					};
					
					if (nextIndex != curIndex) {
						newImg.src = hike_id + "/" + imgs[nextIndex];
					}
				}
			});	
		});
	}
}

function contain_img() {	
		//document.getElementById('imgClickAndChange').style.visibility = 'hidden';
		//setTimeout(function(){
		//$(document).ready(function() {
		//$(window).on("load", function() {
		var win_w = window.innerWidth;
		var win_h = window.innerHeight;
		var win_ar = win_w / win_h; //aspect ratio
		var thresh = 1.0; //threshold for if aspect ratio is wide or narrow	
		document.getElementById('hiking_page').style.overflow = "hidden";	
		//grab variable values form html elements
		var title_width = document.getElementById('title').offsetWidth;
		var img = document.getElementById('imgClickAndChange');
		var img_w = img.offsetWidth;
		var img_h = img.offsetHeight;
		var img_h_tol = img_h + 150; //tolerance for header and button heights
		var img_ar = img_w / img_h;
		//determine whether win and img are wide / narrow
		wide_window = win_ar > thresh;
		narrow_window = win_ar < thresh;
		wide_img = img_ar > thresh;
		narrow_img = img_ar < thresh;
		//current img style
		var img_style = document.getElementById("img_style").href.split('/').pop();
		//set style based on img and window size
		if (win_ar > thresh) { // wide window
			
			if (img_ar < thresh) { //narrow image
				document.getElementById("img_style").href = "wide_win_img_style.css";
				//console.log('narrow image, wide sytle (1a)');
			}
			else { //wide image
				if ((img_w > win_w) && (img_style == "wide_win_img_style.css")) {
					document.getElementById("img_style").href = "narrow_win_img_style.css";
					//console.log('narrow style (2b)');
				}
				
				else if ( img_h + 150 > win_h && (img_style == "narrow_win_img_style.css")) {
					document.getElementById("img_style").href = "wide_win_img_style.css";
					//console.log('wide sytle (3c)');
				}
			}
		}
		else { // narrow window
			if (img_ar > thresh) { //wide image
				document.getElementById("img_style").href = "narrow_win_img_style.css";
				//console.log('narrow image, wide sytle (1b)');
			}
			else { //narrow image
				if ((img_h + 150 > win_h) && (img_style == "narrow_win_img_style.css")) {
						document.getElementById("img_style").href = "wide_win_img_style.css";
						//console.log('narrow style (2b)');
					}
					
					else if ( img_w > win_w && (img_style == "wide_win_img_style.css")) {
						document.getElementById("img_style").href = "narrow_win_img_style.css";
						//console.log('wide sytle (3b)');
					}
			}
		}
		//hide the title if screen is too narrow
		if (title_width < 600) {
			document.getElementById('title').style.visibility = "hidden";
		}
		//display title if it was hidden but screen is wide
		else if(document.getElementById('title').style.visibility == "hidden") {
			document.getElementById('title').style.visibility = "visible"
		}
		//img.style.visibility = 'visible';
		document.getElementById('hiking_page').style.overflow = "visible";
	//});
	//}, 200);
	return false;
}