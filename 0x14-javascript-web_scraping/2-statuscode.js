#!/usr/bin/node

const request = require('request');
const args = process.argv;

request(args[2], (error, response, body) => {
  if (error) {
    console.error(error);
  }
  console.log('code: ' + response.statusCode);
});
