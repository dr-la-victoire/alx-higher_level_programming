$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    type: 'GET',
    dataType: 'json',
    success: function(data) {
        const movieList = $('#list_movies');
        $.each(data.results, function(index, movie){
            movieList.append('<li>' + movie.title + '</li>');
        });
    }
});