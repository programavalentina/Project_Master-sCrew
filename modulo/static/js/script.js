$(document).ready(function() {
	$("#btn-menu").click(function() {
		$(this).toggleClass("open");
			$("nav").fadeToggle();
	});

	$("#options-home").click(function() {
		$(".options-sign").fadeOut();
		$(".options-log").fadeOut();	
	});

	$("#options-about").click(function() {
		$(".options-sign").fadeOut();
		$(".options-log").fadeOut();	
	});

	$("#options-sign").click(function() {
		$(".options-sign").fadeToggle();
		$(".options-log").fadeOut();	
	});

	$("#options-log").click(function() {
		$(".options-log").fadeToggle();
		$(".options-sign").fadeOut();	
	});
});