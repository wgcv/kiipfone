$("#menuresponsive").click(function() {
	if( $("nav ul li").css( "display") =="none" ){
		$("nav ul li").css( "display", "block" );
	}else{
		$("nav ul li").css( "display", "none" );	
	}
});
//login
/*
$("#login").click(function() {
	if( $("#usuario").css( "display") =="none" ){
		$("#usuario").css( "display", "block" );
	}
});*/
//login ocultar
$(document).mouseup(function (e)
{
    var container = $("#usuario");
    var login = $("#login");
    if (login.is(e.target) // if the target of the click isn't the container...
     ) // ... nor a descendant of the container
    {
    	if( $("#usuario").css( "display") =="none" ){
		$("#usuario").css( "display", "block" );
	}else{
    	$("#usuario").css( "display", "none" );
	}
    }else if (!container.is(e.target)&& container.has(e.target).length === 0){
    		
        $("#usuario").css( "display", "none" );	
    }
});
