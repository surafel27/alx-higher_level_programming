#!/usr/bin/node
const strNumber = parseInt(process.argv[2]);
if (!strNumber) {
  console.log('Not a number');
}else {
  console.log('My number:' + ' ' + strNumber);
}
