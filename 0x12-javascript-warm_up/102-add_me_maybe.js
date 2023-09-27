#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number); // increment and call
};

// exports.addMeMaybe exports the function to another file
