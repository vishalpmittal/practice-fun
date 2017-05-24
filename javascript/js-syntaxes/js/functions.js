var writeMyName = function () {
  document.write('Thomas');
};

writeMyName();
writeMyName();
writeMyName();

var writeAName = function (name) {
  document.write(name);
};

writeAName('Jennifer');
writeAName('Stegosaurus');

var writeNameManyTimes = function (name, times) {
  var i;

  for (i = 0; i < times; i++) {
    document.write(name + '<br>');
  }
};

writeNameManyTimes('T-Rex', 5);
writeNameManyTimes('Apatosaurus', 25);
