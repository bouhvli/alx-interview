#!/usr/bin/node
const request = require('request');

const filmsId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${filmsId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log('Error: ', error);
  } else if (response.statusCode !== 200) {
    console.log('Unexpected status code: ', response.statusCode);
  } else {
    const filmInfo = JSON.parse(body);
    filmInfo.characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.log('Error: ', error);
        } else if (response.statusCode !== 200) {
          console.log('Unexpected status code: ', response.statusCode);
        } else {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    });
  }
});
