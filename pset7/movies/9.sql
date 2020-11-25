SELECT people.name
from people 
where people.id in (
    select distinct stars.person_id
    from stars join movies on stars.movie_id = movies.id
    join people on stars.person_id = people.id
    where movies.year = 2004
    order by people.birth asc
);


