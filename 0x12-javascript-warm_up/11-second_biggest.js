#!/usr/bin/node

const len = process.argv.length;

// printing 1 if args are 0 or 1
if (len <= 3) {
  console.log(1);
} else {
  // assigning the first and second args as biggest and 2nd biggest
  let biggest = parseInt(process.argv[2]);
  let secondBiggest = parseInt(process.argv[3]);

  // swaping if second biggest is actually bigger than the biggest
  if (secondBiggest > biggest) {
    const a = secondBiggest;
    secondBiggest = biggest;
    biggest = a;
  }

  // going through the rest of the array
  for (let i = 4; i < len; i++) {
    // turning i to a number
    const num = parseInt(process.argv[i]);

    // checking if the current is the biggest
    if (num > biggest) {
      secondBiggest = biggest;
      biggest = num;
    } else if (num > secondBiggest) {
      secondBiggest = num;
    }
  }
  console.log(secondBiggest);
}
