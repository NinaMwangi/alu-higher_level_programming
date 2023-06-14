#!/usr/bin/node

var fs = require('fs')

fs.readfile('process.argv[2]','utf8', function(error, data) {
  if (error) {
    console.error(error);
    return;    
  }
  console.log(data);
});
