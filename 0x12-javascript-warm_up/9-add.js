#!/usr/bin/node
function add(a, b) {
  let c = a + b;
  console.log(c);
}

const args = process.argv;
add(parseInt(args[2]), parseInt(args[3]));