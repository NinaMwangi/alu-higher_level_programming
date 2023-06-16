#!/usr/bin/node

$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    type: 'GET',
    dataType: 'json'
  }).done((json) => {
    json.results.forEach((title) => {
      $('ul#list_movies').append(`<li>${title}</li>`);
    });
  });
