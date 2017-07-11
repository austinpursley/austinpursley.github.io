
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
		alert("this far 1");
		$.each(data, function(key, value){
			alert("this far 2");
			$.each(value, function(key, value){
				alert("this far 3");
				if (loc == key) {
					alert("holt shit");
				}
			});
		});
		
		var template = $('#hiking_page_template').html();
		var html = Mustache.to_html(template, data);
		$('#templateArea').html(html);
	});
	
});