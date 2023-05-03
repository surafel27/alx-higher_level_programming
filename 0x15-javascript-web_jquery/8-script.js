$(function () {
  fetch('https://swapi-api.alx-tools.com/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
      const films = data.results;
      for (const i in films) {
        $('#list_movies').append('<li>' + films[i].title + '</li>');
      }
    });
});
