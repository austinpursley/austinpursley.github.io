// Index template render
$(document).ready(function() {
	$.getJSON('hiking_data.json', function(data) {
			var template = $('#hike_index_template').html();
			var html = Mustache.to_html(template, data);
			$('#templateArea').html(html);
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
			}
		});
	});
	return false;
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
	var hike_id = document.getElementById('hike_id').innerHTML;
	$.getJSON("hiking_data.json", function(data) {
		$.each(data.hiking_places, function(key, place) {
			if (hike_id == place.id) {
				var imgs = place.img_array;
				// reference to the img element:
				var imgElement = document.getElementById('imgClickAndChange'),
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
				imgElement.src = hike_id + "/" + imgs[nextIndex];
				return false;
			}
		});	
	});
 	/*	if (numImg == 1) {
		return false;
	} */
}

document.body.addEventListener('keydown', imgCycle);


//save this, might need it later.
/* function get_url(id) {
	return id + "/" + id + ".html";
} */
