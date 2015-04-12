inicio();
function inicio () {
	
	$( "#reparar" ).mouseover(function() {
		$( "#crashiphone" ).animate({
			opacity: 0.2,

		},
		500, function() {
			$("#crashiphone").attr("src","/static/img/iphonenocracked.png");
			$( "#crashiphone" ).animate({
			opacity: 1,

		},
		500);
			//$( "#crashiphone" ).css( "display", "inline-block" );

		});
		
	})

	.mouseout(function() {

		$("#crashiphone").attr("src","/static/img/iphonecracked.png");
	});
}

