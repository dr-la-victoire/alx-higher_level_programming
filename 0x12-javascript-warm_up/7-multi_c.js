#!/usr/bin/node
const num = process.argv[2];
const newNum = parseInt(num);

if (isNaN(newNum)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < newNum; i++) {
    console.log('C is fun');
  }
}
