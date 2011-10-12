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
		$('#id_union, #id_central').parent().parent().hide();
		if(reset) $('#id_union, #id_central').val(0);
	}
	function doShow(val, reset){
		if(val==3){
			hideAll(reset);
			$('#id_union').parent().parent().show();
		}else if(val==4){
			hideAll(reset);
			$('#id_central').parent().parent().show();
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