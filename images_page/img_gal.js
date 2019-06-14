// Index template render
$(document).ready(function() {
	$.getJSON('data.json', function(data) {
			var template = $('#lightbox_temp').html();
			var html = Mustache.to_html(template, data);
			$('#lightbox_temp_area').html(html);
	});
});

$('a[href^="#"]').click(function(e) {
		e.preventDefault();
});