var iguanodon = {
  name: 'Iguanodon',
  height: '13m',
  weight: '3t'
};

console.log(iguanodon.name);
console.log(iguanodon.weight);

iguanodon.diet = 'Herbivore';
console.log(iguanodon);

var spinosaurus = {
  name: 'Spinosaurus',
  height: '15m',
  weight: '6t',
  diet: 'Carnivore'
};

var microraptor = {
  name: 'Microraptor',
  height: '80cm',
  weight: '1kg',
  diet: 'Carnivore'
};

var writeDinos = function (dinos) {
  dinos.forEach(function (item) {
    document.write('<h2>' + item.name + '</h2>');
    document.write('<dl>');
    document.write('<dt>Height:</dt><dd>' + item.height + '</dd>');
    document.write('<dt>Weight:</dt><dd>' + item.weight + '</dd>');
    document.write('<dt>Diet:</dt><dd>' + item.diet + '</dd>');
    document.write('</dl>');
  });
};

writeDinos([iguanodon, spinosaurus, microraptor]);
