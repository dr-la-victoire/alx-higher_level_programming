#!/usr/bin/node

const request = require('request');
const args = process.argv;

request(args[2], (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const todos = JSON.parse(body);
    const completedTodos = {};
    todos.forEach((todos) => {
      if (todos.completed) {
        if (!completedTodos[todos.userId]) {
          completedTodos[todos.userId] = 1;
        } else {
          completedTodos[todos.userId] += 1;
        }
      }
    });
    console.log(completedTodos);
  }
});
