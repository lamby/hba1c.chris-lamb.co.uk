$.feature('f_form_submit', function() {
  $('form').on('submit', function() {
    $('.loading').show();
    return true;
  });
});
