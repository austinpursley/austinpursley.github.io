
$(document).ready(function() {
	$.getJSON('hiking_data.json', function(data) {
		//var template = $('#hike_index_template').html();
		$.get('templates.html', function(templates) {
		// commented below works only online. uncomment later.
		//$.get('/../hiking/templates.html', function(templates) {
			alert(templates);
			var template = $(templates).find('#hike_index_template').html();
			var html = Mustache.to_html(template, data);
			$('#templateArea').html(html);
		});
	});
});

function get_url(id) {
	return id + "/" + id + ".html";
}