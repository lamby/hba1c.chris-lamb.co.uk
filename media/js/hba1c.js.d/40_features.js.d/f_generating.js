$.feature('f_generating', function() {
  var poll = function () {
    $.post(window.location.pathname, {}, function (data) {
      if (data.redirect !== undefined) {
        window.location.replace(data.redirect);
      }
    }).always(function() {
      setTimeout(poll, 1000);
    });
  };

  poll();
});
