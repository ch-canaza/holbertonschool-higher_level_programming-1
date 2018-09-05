#!/usr/bin/node
let request = require('request');
let url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let filmList = JSON.parse(body).results;
    let count = 0;
    for (let film in filmList) {
      let charList = filmList[film].charList;
      for (let character in charList) {
        if (charList[character].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('Wrong status code');
  }
});
