$.extend({
  feature: function(body_class,callback) {
    if ($('body').hasClass(body_class)) {
      $(callback);
    }
  }
});

$.fn.extend({
  focus_first_of: function () {
    return this.each(function() {
      if (this.value.length === 0) {
        this.focus();
        return false;
      }
    });
  }
});
