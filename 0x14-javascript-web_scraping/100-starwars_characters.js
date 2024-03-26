#!/usr/bin/node

const request = require('request');
const args = process.argv;
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + args[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const people = data.characters;
    for (const chars of people) {
      request(chars, (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          const peopleData = JSON.parse(body);
          console.log(peopleData.name);
        }
      });
    }
  }
});
