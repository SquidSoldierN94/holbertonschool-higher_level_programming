-- Hotline Miami 2: Wrong Number Soundtrack - Delay
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
