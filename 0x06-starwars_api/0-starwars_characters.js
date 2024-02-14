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
    const charactersUrls = filmInfo.characters;

    function getCharacterName (charactersUrl) {
      return new Promise((resolve, reject) => {
        request(charactersUrl, (error, response, body) => {
          if (error) {
            reject(error);
          } else if (response.statusCode !== 200) {
            reject(new Error(`Unexpected status code: ${response.statusCode}`));
          } else {
            const characterData = JSON.parse(body);
            resolve(characterData.name);
          }
        });
      });
    }

    async function displayCharactersInOrder () {
      for (const charactersUrl of charactersUrls) {
        try {
          const characterName = await getCharacterName(charactersUrl);
          console.log(characterName);
        } catch (error) {
          console.log('Error while fetchinf data: ', error);
        }
      }
    }

    displayCharactersInOrder();
  }
});
