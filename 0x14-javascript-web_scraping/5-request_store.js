#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const args = process.argv;

request(args[2], (error, response, body) => {
  if (error) {
    console.error(error);
  }

  fs.writeFile(args[3], body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
