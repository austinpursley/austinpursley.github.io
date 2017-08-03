// Index template render
$(document).ready(function() {
	$.getJSON('hiking_data.json', function(data) {
			var template = $('#hike_index_template').html();
			var html = Mustache.to_html(template, data);
			$('#templateArea').html(html);
			history.replaceState( { 
					id: "index"
			}, null, ("hikes.html"));
	});
});

//Function for hiking page render, called when url for hiking page is clicked.
function render_page_templ(id) {
	$.getJSON("hiking_data.json", function(data) {
		$.each(data.hiking_places, function(key, place) {
			if (id == place.id) {
				var template = $('#hiking_page_template').html();
				var html = Mustache.to_html(template, place);
				$('#templateArea').html(html);
				contain_img();
				history.replaceState( { 
					id: place.id
				}, null, "/hikes/#" + place.id);
				window.addEventListener("resize", contain_img);
				document.body.addEventListener('keydown', imgCycle);
			}
		});
	});
	//contain_img();
	return false;
}



window.onpopstate = function (event) { 
  if (event.state && event.state.id == "index"){
	window.location.href = "hikes.html";
  }
}

// Even listener for hike page click and imgage cycle buttons.
//This comes from David Walsh's website article "How JavaScript Even Delegation Works"
//https://davidwalsh.name/event-delegate
document.getElementById("templateArea").addEventListener("click", function(e) {
	if(e.target && e.target.nodeName == "A") {
		render_page_templ(e.target.id);
		
	}
	
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
					if (nextIndex != curIndex) {
						imgElement.src = hike_id + "/" + imgs[nextIndex];
						contain_img();
					}
				}
			});	
		});
	}
}



function contain_img() {
	//To-Do: hide image when loading, maybe hide scrollbars, fix button on bottom of screen,
	//style variable, set document.getElementById("img_style").href at end
	
	
	var win_w = window.innerWidth;
	var win_h = window.innerHeight;
	var win_ar = win_w / win_h;
	
	var thresh = 1.0;
	setTimeout(function(){
		var title_width = document.getElementById('title').offsetWidth;
		var img = document.getElementById('imgClickAndChange');
		var img_w = img.offsetWidth;
		var img_h = img.offsetHeight;
		var img_ar = img_w / img_h;
		console.log("img_ar", img_ar);
		console.log("win_ar", win_ar);
	//save_img_display = img.style.display;
	//img.style.display = 'none';
		var img_style = document.getElementById("img_style").href.split('/').pop();
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
		if (title_width < 550) {
			document.getElementById('title').style.visibility = "hidden";
		}
		else if(document.getElementById('title').style.visibility == "hidden") {
			document.getElementById('title').style.visibility = "visible"
		}
	}, 200);
	return false;
}


