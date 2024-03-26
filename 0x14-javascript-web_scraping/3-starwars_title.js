#!/usr/bin/node

const request = require('request');
const args = process.argv;
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + args[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const film = JSON.parse(body);
    console.log(film.title);
  }
});
