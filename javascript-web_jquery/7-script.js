#!/usr/bin/node

$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    type: 'GET',
    success: (result) => {
        $('#character').text('result.name');
    }
});
