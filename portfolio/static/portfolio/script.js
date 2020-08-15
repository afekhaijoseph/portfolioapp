
$('#addskill').click(function(e) {
var skill_idx = $('#id_skill-TOTAL_FORMS').val();
$('#skill_set').append($('#empty_skill_form').html().replace(/__prefix__/g, skill_idx));
$('#id_skill-TOTAL_FORMS').val(parseInt(skill_idx) + 1);
});

$('#addworkexp').click(function(e) {
var workexp_idx = $('#id_workexp-TOTAL_FORMS').val();
$('#workexp_set').append($('#empty_workexp_form').html().replace(/__prefix__/g, workexp_idx));
$('#id_workexp-TOTAL_FORMS').val(parseInt(workexp_idx) + 1);
});


$('#addacadexp').click(function(e) {
  var acadexp_idx = $('#id_acadexp-TOTAL_FORMS').val();
  $('#acadexp_set').append($('#empty_acadexp_form').html().replace(/__prefix__/g, acadexp_idx));
  $('#id_acadexp-TOTAL_FORMS').val(parseInt(acadexp_idx) + 1);
});


$('#update-skill').click(function(e) {
  var update_skill_idx = $('#id_update-skill-TOTAL_FORMS').val();
  $('#update-skill_set').append($('#empty_update-skill_form').html().replace(/__prefix__/g, update_skill_idx));
  $('#id_update-skill-TOTAL_FORMS').val(parseInt(update_skill_idx) + 1);
  });
  
  $('#update-workexp').click(function(e) {
  var update_workexp_idx = $('#id_update-workexp-TOTAL_FORMS').val();
  $('#update-workexp_set').append($('#empty_update-workexp_form').html().replace(/__prefix__/g, update_workexp_idx));
  $('#id_update-workexp-TOTAL_FORMS').val(parseInt(update_workexp_idx) + 1);
  });
  
  
  $('#update-acadexp').click(function(e) {
    var update_acadexp_idx = $('#id_update-acadexp-TOTAL_FORMS').val();
    $('#update-acadexp_set').append($('#empty_update-acadexp_form').html().replace(/__prefix__/g, update_acadexp_idx));
    $('#id_update-acadexp-TOTAL_FORMS').val(parseInt(update_acadexp_idx) + 1);
  });
  
  