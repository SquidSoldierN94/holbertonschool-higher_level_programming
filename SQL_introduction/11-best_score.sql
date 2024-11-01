-- This script selects the score and name from 'second_table' where score is greater than or equal to 10 and orders the results by score in descending order.
-- Save this file as 11-select_where_score_ge_10_order_by_score_desc.sql

-- The SELECT command retrieves specified columns from the specified table where the condition is met and orders the results.
SELECT score, name 
FROM second_table 
WHERE score >= 10 
ORDER BY score DESC;
