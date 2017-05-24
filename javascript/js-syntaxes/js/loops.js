var counter;

for (counter = 0; counter < 10; counter++) {
  document.write('Hello.');
}

var name = '';

while (!name) {
  name = prompt('What is your name?')
}

document.write(name);
