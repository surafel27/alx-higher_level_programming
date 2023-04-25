#!/usr/bin/node
const fs = require('fs');
const process = require('process');
const argv = process.argv;
const reader = fs.createReadStream(argv[2], { encoding: 'UTF-8' });
reader.on('error', function (error) {
  console.log(error);
});
reader.on('data', function (chunk) {
  console.log(chunk.toString());
});
