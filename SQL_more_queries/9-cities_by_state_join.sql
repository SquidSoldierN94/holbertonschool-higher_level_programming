-- Hotline Miami 2: Wrong Number Soundtrack - Richard (2)
SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states
ON cities.state_id = states.id;
