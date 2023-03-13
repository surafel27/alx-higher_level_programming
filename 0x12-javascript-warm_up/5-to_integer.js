#!/usr/bin/node
t strNumber = Number(process.argv[2]);
if (!strNumber) {
  console.log('Not a number');
}else {
  console.log('My number:' + ' ' + strNumber);
}
