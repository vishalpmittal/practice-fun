var $heading = $('.heading');

$heading.on('click', function () {
  $heading.addClass('js-make-red').toggleClass('js-add-stars');
});
