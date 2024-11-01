-- This script selects the score and name from 'second_table' where the name is not NULL and orders the results by score in descending order.
-- Save this file as 16-select_where_name_not_null_order_by_score_desc.sql

-- The SELECT command retrieves specified columns from the specified table where the condition is met and orders the results.
SELECT score, name 
FROM second_table 
WHERE name IS NOT NULL 
ORDER BY score DESC;
