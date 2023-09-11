#!/usr/bin/node
const args = process.argv;
const integer = parseInt(args[2]);

if (integer.isNaN) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < integer; i++) {
    console.log('C is fun');
  }
}
