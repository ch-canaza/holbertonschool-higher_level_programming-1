#!/usr/bin/node
let request = require('request');
let url = 'http://swapi.co/api/people/';
let episodeNumber = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let allChars = JSON.parse(body).results;
    for (let c in allChars) {
      let filmList = allChars[c].films;
      for (let i in filmList) {
        if (filmList[i].includes(episodeNumber)) {
          console.log(allChars[c].name);
        }
      }
    }
  } else {
    console.log('Wrong status code');
  }
});
