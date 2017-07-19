
$(document).ready(function() {
	$.getJSON('hiking_data.json', function(data) {
			var template = $('#hike_index_template').html();
			var html = Mustache.to_html(template, data);
			$('#templateArea').html(html);
	});
});

function get_url(id) {
	return id + "/" + id + ".html";
}