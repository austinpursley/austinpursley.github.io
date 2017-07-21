
//This comes from David Walsh's website article "How JavaScript Even Delegation Works"
//https://davidwalsh.name/event-delegate
document.getElementById("templateArea").addEventListener("click", function(e) {
	//e.target is the clicked element!
	if(e.target && e.target.nodeName == "A") {
		//List item found!  Output the ID!
		render_page_templ(e.target.id);
	}
	
	if(e.target && e.target.nodeName == "BUTTON") {
		imgCycle(e);
	}
});
//not working because when leave (window.location =...) the evenlistener code goes poof
//put it all onto one html page
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


/* $(document).ready(function() {
	var elem = document.getElementById("loc");
	var hike_loc = elem.innerText;
	$.getJSON("hiking_data.json", function(data) {
		$.each(data.hiking_places, function(key, place) {
			if (hike_loc == place.title2) {
				var template = $('#hiking_page_template').html();
				var html = Mustache.to_html(template, place);
				$('#templateArea').html(html);
			}
		});
	});
}); */