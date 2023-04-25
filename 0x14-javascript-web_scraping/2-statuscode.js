#!/usr/bin/node
const request = require('request');
const process = require('process');
const url = process.argv[2];
const res = request.get(url);
res.on('error', function (error) {
  console.log(error);
});
res.on('response', function (response) {
  console.log('code: ', response.statusCode);
});
