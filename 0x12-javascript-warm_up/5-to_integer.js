#!/usr/bin/node
const num = process.argv[2];
const newNum = parseInt(num);

if (isNaN(newNum)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + newNum);
}
