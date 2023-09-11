#!/usr/bin/node

const args = process.argv;
const integer = parseInt(args[2]);
const newInteger = Math.floor(integer);

if (isNaN(newInteger)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + args[2]);
}
