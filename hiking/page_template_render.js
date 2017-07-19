
$(document).ready(function() {
	var elem = document.getElementById("loc");
	var hike_loc = elem.innerText;
	
	// commented below works only online. uncomment later.
	// $.getJSON("/../hiking/hiking_data.json", function(data) {
	$.getJSON("hiking_data.json", function(data) {
		$.each(data.hiking_places, function(key, value){
			if (hike_loc == value.title2) {
				$.get('templates.html', function(templates) {
				// commented below works onllu onlline. uncomment later.
				//$.get('/../hiking/templates.html', function(templates) {
					var template = $(templates).find('#hiking_page_template').html();
					var html = Mustache.to_html(template, value);
					$('#templateArea').html(html);
					return
				});
			}
		});
	});
});