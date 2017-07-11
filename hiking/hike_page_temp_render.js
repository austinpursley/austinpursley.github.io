$(document).ready(function() {

	$.getJSON('hiking_data.json', function(data) {
		var template = $('#hike_page_template').html();
		var html = Mustache.to_html(template, data);
		$('#templateArea').html(html);
	});

});