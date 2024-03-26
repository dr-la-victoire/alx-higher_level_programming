#!/usr/bin/node

const request = require('request');
const args = process.argv;
let count = 0;

request(args[2], (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    // getting the results and looping over each film
    data.results.forEach((film) => {
      // looping over each char id and checking when == 18
      film.characters.forEach((character) => {
        if (character.includes('18')) {
          count = count + 1;
        }
      });
    });
    console.log(count);
  }
});
