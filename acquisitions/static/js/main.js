$(document).ready(function($){
$('select.extra-select').change(function(){
  console.log($(this).val());
  if($(this).val() ==="others"){
    $(this).next('input.extra-input').show();
  } else {
    $(this).next('input.extra-input').hide();
  }
});
});
