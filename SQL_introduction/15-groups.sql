-- This script selects the score and the count of records for each score from 'second_table', groups the results by score, and orders them by the count in descending order.
-- Save this file as 15-select_group_by_score_order_by_number_desc.sql

-- The SELECT COUNT(*) and GROUP BY commands count the number of records for each group and the ORDER BY command orders the results.
SELECT score, COUNT(*) AS number 
FROM second_table 
GROUP BY score 
ORDER BY number DESC;
