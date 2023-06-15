#!/usr/bin/node

const request = require('request');
let xFilms = 0;

request(process.argv[2], function (err, res, body) {
  if (err == null) {
    const resp = JSON.parse(body);
    const result = resp.result;
    for (let i = 0; i < result.length; i++) {
      const char = result[i].char;
      for (let j = 0; j < char.length; j++) {
        if (char[j].search('18') > 0) {
          xFilms++;
        }
      }
    }
  }
  console.log(xFilms);
});
