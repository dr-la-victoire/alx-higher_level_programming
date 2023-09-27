#!/usr/bin/node

// importing the rectangle class
const Rectangle = require('./4-rectangle');
// extending with extends
class Square extends Rectangle {
// using the constructor
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
