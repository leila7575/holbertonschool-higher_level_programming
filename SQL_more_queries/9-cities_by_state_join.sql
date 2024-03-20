-- lists all cities contained in the database hbtn_0d_usa
-- in ascending order by cities.id
SELECT cities.id, cities.name, states.name
FROM cities
NATURAL JOIN states
ORDER BY cities.id ASC;
