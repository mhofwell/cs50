select name from people join stars where people.id = stars.person_id AND stars.movie_id = (select stars.movie_id from stars join movies where stars.movie_id = movies.id and movies.title="Toy Story");