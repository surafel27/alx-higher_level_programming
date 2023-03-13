#!/usr/bin/node

const strNumber = parseInt(process.argv[2]);
if (!strNumber) {
  console.log('Missing number of occurrences');
} else {
 for (let i = 0; i < strNumber; ++i) {
     console.log('C is fun');
}
