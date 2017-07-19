$(document).ready(function() {
	var elem = document.getElementById("loc");
	var hike_loc = elem.innerText;
		
	// $.getJSON("/../hiking/hiking_data.json", function(data) {
	$.getJSON("hiking_data.json", function(data) {
		$.each(data.hiking_places, function(key, value1){
			$.each(value1.place, function(key, value2){
				if (hike_loc == value2.title2) {
					$.get('templates.html', function(templates) {
						var template = $(templates).find('#hiking_page_template').html();
						var html = Mustache.to_html(template, value2);
						$('#templateArea').html(html);
						return
					});
					
				}
			});
		});
	});
});