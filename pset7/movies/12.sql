select movies.title
from movies
join stars on stars.movie_id = movies.id
join people on people.id = stars.person_id
where people.name="Johnny Depp"
intersect
select movies.title
from movies
join stars on stars.movie_id = movies.id
join people on people.id = stars.person_id
where people.name="Helena Bonham Carter";