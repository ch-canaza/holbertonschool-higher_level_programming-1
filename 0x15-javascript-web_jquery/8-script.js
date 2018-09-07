// fetches and lists all movie titles using a url
$.get('https://swapi.co/api/people/5/?format=json', function (data, status) {
  if (status === 'success') {
    for (let i in data.results) {
      $('ul#list_movies').append('<li>' + data.results[i].title + '</li>');
    }
  }
});
