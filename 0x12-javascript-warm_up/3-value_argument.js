#!/usr/bin/node

const args = process.argv;
let length = 0;
let i;

for (i in args) {
  if (args.hasOwnProperty(i)) {
    length++;
  }
}

if (length < 3) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
