#!/usr/bin/node
const strNumber = parseInt(process.argv[2]);
if (strNumber) {
  console.log('My number: ' + strNumber);
} else {
  console.log('Not a number');
}
