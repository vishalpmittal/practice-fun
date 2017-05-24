var name = 'Thomas';
var age = 32;
var isHuman = false;
var isDinosaur = false;

if (isHuman && !isDinosaur) {
  // If the logic is true, true path
  // alert('True path was taken!');
} else {
  // If the logic is false, false path
  // alert('False path was taken.');
}

if (isHuman || isDinosaur) {
  // alert('Creature!');
} else {
  // alert('Not a cool creature.');
}

if (age >= 32) {
  // alert('Over 25');
} else {
  // alert('Under 25');
}

if (age >= 32 && (isHuman || isDinosaur)) {
  // alert('Woot!');
}

var newName = prompt('What is your name?');

if (newName == 'Thomas') {
  alert('Names are the same!');
} else {
  alert('Names are different.');
}
