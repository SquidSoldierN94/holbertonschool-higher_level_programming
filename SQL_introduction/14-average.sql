-- This script selects the average score from 'second_table'.
-- Save this file as 14-select_avg_score.sql

-- The SELECT AVG function calculates the average value of the specified column.
SELECT AVG(score) AS average 
FROM second_table;
