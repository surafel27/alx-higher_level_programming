#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const movies = JSON.parse(body).results;
    let count = 0;
    for (const movieIndex in movies) {
      const movieChars = movies[movieIndex].characters;
      for (const charIndex in movieChars) {
        if (movieChars[charIndex].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
