$.feature('f_write', function() {
  $('#id_content').autosize({append: "\n\n\n"}).focus();

  $('.js-signature-thumbnail').on('click', function(e) {
    e.preventDefault();

    $('#id_signature').click();
  });

  $('.js-show-signature a').on('click', function (e) {
    e.preventDefault();

    $(this).parents('.js-show-signature').hide();
    $('.js-signature-fields').removeClass('hide');
  });

});
