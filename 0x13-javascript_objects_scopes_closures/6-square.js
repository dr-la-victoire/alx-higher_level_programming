#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    // check if c is undefined
    let theVar = c;
    if (theVar === undefined) {
      theVar = 'X';
    }
    // the loop to print the square
    for (let i = 0; i < this.height; i++) {
      let newVar = '';
      for (let j = 0; j < this.width; j++) {
        newVar += theVar;
      }
      console.log(newVar);
    }
  }
}

module.exports = Square;
