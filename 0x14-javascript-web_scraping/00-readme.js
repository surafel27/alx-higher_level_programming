#!/usr/bin/node
const fs = require('fs');
const process = require('process');
const argv = process.argv
fs.readFile(argv[2], (err, data) => {
    if (err) throw err;

    console.log(data.toString());
});
