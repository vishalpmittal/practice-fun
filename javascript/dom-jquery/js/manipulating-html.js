var $add = $('.add');
var $list = $('.list');
var $addStart = $('.add-start');
var $after = $('.after');
var $before = $('.before');
var $prime = $('.prime');
var $remove = $('.remove');
var $html = $('.html');

$add.on('click', function () {
  $list.append('<li>Appended List Item</li>');
});

$addStart.on('click', function () {
  $list.prepend('<li>Add to beginning</li>');
});

$after.on('click', function () {
  $prime.after('<li>Added after</li>');
});

$before.on('click', function () {
  $prime.before('<li>Added before</li>');
});

$remove.on('click', function () {
  $prime.remove();
});

$html.on('click', function () {
  $list.html('<li>New Item</li><li>Another New Item!</li>');
});
