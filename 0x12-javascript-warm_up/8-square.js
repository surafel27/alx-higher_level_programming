#!/usr/bin/node

const strNumber = parseInt(process.argv[2]);
let string = '';
if (strNumber) {
  for (let i = 0; i < strNumber; i++) {
    for (let j = 0; j < strNumber; j++) {
     string += 'X';
    }
    if ( i == strNumber - 1) {
     break;
      }
    string += '\n';
}
console.log(string);
} else {
  console.log('Missing size');
} 
