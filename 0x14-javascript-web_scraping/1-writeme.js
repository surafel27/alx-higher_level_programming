#!/usr/bin/node
const fs = require('fs');
const process = require('process');
const filename = process.argv[2];
const content = process.argv[3];
const writing = fs.createWriteStream(filename, { flags: 'w', encoding: 'UTF-8' });
writing.write(content);
writing.on('error', function (error) {
  console.log(error);
});
