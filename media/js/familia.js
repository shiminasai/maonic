(function($) {	
	$(document).ready(function(){		
		var state = checkURL();
		if(state=='add'){
			hideAll(true);			
		}else{
			hideAll(false);
			var val = $('#id_tipo_org').val();
			doShow(val, false);
		}
		$('#id_tipo_org').change(function(){
			var val = $(this).val();			
			doShow(val, true);
		});
	});
	
	function hideAll(reset){
		$('#id_cooperativa, #id_asociacion').parent().parent().hide();
		if(reset) $('#id_cooperativa, #id_asociacion').val(0);
	}
	function doShow(val, reset){
		if(val==1){
			hideAll(reset);
			$('#id_asociacion').parent().parent().show();
		}else if(val==2){
			hideAll(reset);
			$('#id_cooperativa').parent().parent().show();
		}else{
			hideAll(reset);
		}
	}
	function checkURL(){
		var url = window.location.href.split('/');
		if((url[url.length-2]=="add") && (url.length == 8)){
			return 'add';
		}else if(url.length == 8){
			return 'edit';
		}
	}	
})(jQuery || django.jQuery);

