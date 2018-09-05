#!/usr/bin/node
let request = require('request');
let url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let done = {};
    let tasks = JSON.parse(body);
    for (let i in tasks) {
      let current = tasks[i];
      if (current.completed === true) {
        if (done[current.userId] === undefined) {
          done[current.userId] = 1;
        } else {
          done[current.userId]++;
        }
      }
    }
    console.log(done);
  } else {
    console.log('Wrong status code');
  }
});
