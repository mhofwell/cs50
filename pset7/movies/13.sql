select distinct name
from people
where name != "Kevin Bacon" 
and id in (
    select person_id from stars where movie_id in
        (select movie_id from stars where person_id in
            (select id from people 
            where name is "Kevin Bacon" 
            and birth = 1958
        )
    )
)
order by name; 

-- join stars on people.id = stars.person_id
-- where stars.movie_id in (
--     select stars.movie_id
--     from stars
--     join people on stars.person_id = people.id 
--     where people.name = "Kevin Bacon" and people.birth = 1958
--     ) 
-- and people.name != ("Kevin Bacon");