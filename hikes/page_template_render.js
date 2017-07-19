
$(document).ready(function() {
	var elem = document.getElementById("loc");
	var hike_loc = elem.innerText;
	
	// /../hikes/hiking_data.json only works offline
	$.getJSON("/../hikes/hiking_data.json", function(data) {
	//$.getJSON("hiking_data.json", function(data) {
		$.each(data.hiking_places, function(key, value) {
			if (hike_loc == value.title2) {
				$.get('/../hikes/hike_page_template.html', function(templates) {
				//$.get('templates.html', function(templates) {
				// /../hikes/hiking_data.json only works offline
					var template = $(templates).find('#hiking_page_template').html();
					var html = Mustache.to_html(template, value);
					$('#templateArea').html(html);
					return
				});
			}
		});
	});
});