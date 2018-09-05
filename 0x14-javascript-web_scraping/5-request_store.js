#!/usr/bin/node
let fs = require('fs');
let request = require('request');
let url = process.argv[2];
let file = process.argv[3];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    fs.writeFile(file, body, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  } else {
    console.log('Wrong status code');
  }
});
