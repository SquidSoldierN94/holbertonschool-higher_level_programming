-- Hotline Miami 2: Wrong Number Soundtrack - Delay
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
