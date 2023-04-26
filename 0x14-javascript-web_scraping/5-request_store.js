#!/usr/bin/node

const request = require('request');
const fs = require('fs');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const writing = fs.createWriteStream(process.argv[3], { encoding: 'UTF-8' });
    writing.write(body);
    writing.on('error', function (error) {
      console.log(error);
    });
  }
});
