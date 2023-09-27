#!/usr/bin/node
const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  let big = parseInt(args[2]);
  let second = parseInt(args[3]);
  if (second > big) {
    const a = second;
    second = big;
    big = a;
  }
  if (args.length === 4) {
    console.log(second);
  } else if (args.length > 4) {
    for (let i = 4; i < args.length; i++) {
      let integer = parseInt(args[i]);
      if (integer > second) {
        const b = integer;
        integer = second;
        second = b;
        if (second > big) {
          const c = second;
          second = big;
          big = c;
        }
      }
    }
    console.log(second);
  }
}
