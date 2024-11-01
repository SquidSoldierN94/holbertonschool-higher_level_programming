-- This script lists all cities in California from the 'cities' table.
-- It retrieves the state_id of California using a subquery and selects cities that match this state_id.
-- Results are sorted in ascending order by cities.id.

SELECT * FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
