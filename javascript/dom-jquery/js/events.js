var $btn = $('.btn');
var $box = $('.box');
var $html = $('html');

var btnClickHandler = function () {
  var currentLeft = $box.offset().left;
  $box.css('left', currentLeft + 10);
};

$btn.on('click', function () {
  btnClickHandler();
});

$html.on('keydown', function (e) {
  if (e.keyCode == 39) {
    btnClickHandler();
  }
});
