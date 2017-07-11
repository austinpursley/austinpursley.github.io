
/* $(document).ready(function() {

	$.getJSON('hiking_data.json', function(data) {
		var template = $('#hiking_page_template').html();
		var html = Mustache.to_html(template, data);
		$('#templateArea').html(html);
	});

}); */

$(document).ready(function() {
	
	var elem = document.getElementById("location");
	var loc = elem.innerText;
	alert("this far 0");
	$.getJSON("/../hiking_data.json", function(data) {
		$.each(data, function(key, value){
			$.each(value, function(key, value){
				if (loc == key) {
				}
			});
		});
		
		var template = $('#hiking_page_template').html();
		var html = Mustache.to_html(template, data);
		$('#templateArea').html(html);
	});
	
});