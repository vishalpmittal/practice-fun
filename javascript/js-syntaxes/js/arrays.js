var meatEaters = ['T-Rex', 'Spinosaurus', 'Velociraptor'];

meatEaters[0];
meatEaters[2];

console.log(meatEaters[1]);

meatEaters.push('Allosaurus');
console.log(meatEaters);

meatEaters.pop();
console.log(meatEaters);

meatEaters.shift();
console.log(meatEaters);

meatEaters.unshift('Pteranodon');
console.log(meatEaters);
console.log(meatEaters[2]);

document.write('<ul>');
meatEaters.forEach(function (item) {
  document.write('<li>' + item + '</li>');
});
document.write('</ul>');
