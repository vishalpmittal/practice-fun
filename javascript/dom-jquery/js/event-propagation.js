var $btn = $('.btn');
var $big = $('.big');

$btn.on('click', function (e) {
  e.preventDefault();
  var bigStars = $btn.attr('href');
  $big.css('background-image', 'url(' + bigStars + ')');
});
