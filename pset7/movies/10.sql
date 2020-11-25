SELECT people.name
from people 
where people.id in (
    select distinct directors.person_id
    from directors join movies on directors.movie_id = movies.id
    join ratings on ratings.movie_id = movies.id
    where ratings.rating >= 9.0
);

