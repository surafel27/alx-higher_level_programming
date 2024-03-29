#!/usr/bin/node

// write class called Rectangle

module.exports = class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (c = 'X') {
    let string = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        string += c;
      }
      if (i === this.height - 1) {
        break;
      }
      string += '\n';
    }
    console.log(string);
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
