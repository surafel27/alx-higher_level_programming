#!/usr/bin/node

//write class called Rectangle

module.exports = class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    let string = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j <this.width; j++) {
        string += 'X';
      }
      if (i === this.height - 1) {
        break;
      }
      string += '\n';
    }
    console.log(string);
  }
};
