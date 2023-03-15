#!/usr/bin/node

const exSquare = require('./5-square.js');

module.exports = class Square extends exSquare {
  charPrint (c) {
    super.print(c);
  }
};
