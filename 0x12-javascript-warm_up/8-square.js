#!/usr/bin/node
const args = process.argv;
const integer = parseInt(args[2]);

if (isNaN(integer) || integer === undefined) {
  console.log('Missing size');
} else {
  for (let col = 0; col < integer; col++) {
    let x = '';
    for (let row = 0; row < integer; row++) {
      x += 'X';
    }
    console.log(x);
  }
}
