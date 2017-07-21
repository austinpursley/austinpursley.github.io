$(document).ready(function() {
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
});