document.body.overflow = "hidden";

window.onload = function(){
	contain_img();
	hide_title();
	
	$(document).ready(function() {
		//listen for event of a windows resize and keyboard input
		window.addEventListener("resize", function() {
			contain_img();
			hide_title();
		});
		document.body.addEventListener('keydown', imgCycle);
		//hide the scrollbar
		document.body.style.overflow = "hidden";
		//display image now that it should be modified by
		document.getElementById('img_click_change').style.visibility = 'visible';
	});
};

// Even listener for image cycle buttons.
//This comes from David Walsh's website article "How JavaScript Even Delegation Works"
//https://davidwalsh.name/event-delegate
document.body.addEventListener("click", function(e) {
	if(e.target && e.target.nodeName == "BUTTON") {
		imgCycle(e);
	}
});

//Adapted from David Thomas's code on Stack Exchange 
//https://stackoverflow.com/questions/26443828/press-left-and-right-arrow-to-change-image
function imgCycle(e) { //e is the event.
	left_arrow_key = (e.keyCode == 37); //left arrow key
	right_arrow_key = (e.keyCode == 39); //right arrow key
	pre_button = (e.target.className == 'previous');
	nxt_button = (e.target.className == 'next');
	
	if (left_arrow_key || right_arrow_key || pre_button || nxt_button) {
		var id = document.getElementById('id').innerHTML;
		$.getJSON("data.json", function(data) {
			$.each(data.image_set, function(key, item) {
				if (id == item.id) {
					var imgs = item.img_array,
					imgElement = document.getElementById('img_click_change'),
					curImg = imgElement.src.split('/').pop(),
					curIndex = imgs.indexOf(curImg),
					nextIndex;
					console.log(imgElement, curImg, curIndex, nextIndex);
					if (left_arrow_key || pre_button) {
						nextIndex = curIndex === 0 ? (imgs.length - 1) : curIndex - 1;
					}
					else if (right_arrow_key || nxt_button) {
						nextIndex = curIndex + 1 === imgs.length ? 0 : curIndex + 1; 
					}
					else {
						nextIndex = curIndex;
					}
					
					imgElement.style.visibility = 'hidden';
					
					//http://blog.teamtreehouse.com/learn-asynchronous-image-loading-javascript
					//https://stackoverflow.com/questions/2342132/waiting-for-image-to-load-in-javascript
					var newImg = new Image();
					newImg.onload = function() {
						imgElement.src = this.src;
						contain_img();
						document.getElementById('img_click_change').style.visibility = 'visible';
					};
					
					if (nextIndex != curIndex) {
						console.log(nextIndex);
						newImg.src = id + "/" + imgs[nextIndex];
						
					}
				}
			});	
		});
	}
}

function contain_img() {	
	//get info on current image dimenstions
	var img = document.getElementById('img_click_change');
	var img_w = img.offsetWidth;
	var img_h = img.offsetHeight;
	var img_ar = img_w / img_h;  //aspect ratio
	//get info on window dimensions
	var win_w = window.innerWidth;
	var win_h = window.innerHeight;
	var win_ar = win_w / win_h; 
	//threshold for if aspect ratio is wide or narrow	
	var thresh = 1.0; 	
	//tolerance for header and button heights
	var img_h_tol = img_h + 150; 
	//css settings for img currently in use
	var img_style = document.getElementById("img_style").href.split('/').pop();
	//set style based on img and window size
	if (win_ar > thresh) { // wide window
		if (img_ar < thresh) { //narrow image
			document.getElementById("img_style").href = "../wide_win_img_style.css";
		}
		else { //wide image
			if ((img_w > win_w) && (img_style == "wide_win_img_style.css")) {
				document.getElementById("img_style").href = "../narrow_win_img_style.css";
			}
			else if ( img_h_tol > win_h && (img_style == "narrow_win_img_style.css")) {
				document.getElementById("img_style").href = "../wide_win_img_style.css";
			}
		}
	}
	else { // narrow window
		if (img_ar > thresh) { //wide image
			document.getElementById("img_style").href = "../narrow_win_img_style.css";
		}
		else { //narrow image
			if ( img_w > win_w && (img_style == "wide_win_img_style.css")) {
				document.getElementById("img_style").href = "../narrow_win_img_style.css";
			}
			else if ((img_h_tol > win_h) && (img_style == "narrow_win_img_style.css")) {
					document.getElementById("img_style").href = "../wide_win_img_style.css";
			}
		}
	}
	return false;
}

function hide_title() {
	if (document.getElementById('title') != null) {
		//hide the title if screen is too narrow
		var title_width = document.getElementById('title').offsetWidth;
		if (title_width < 600) {
			document.getElementById('title').style.visibility = "hidden";
		}
		//display title if it was hidden and screen is wide enough
		else if(document.getElementById('title').style.visibility == "hidden") {
			document.getElementById('title').style.visibility = "visible"
		}
	}
}