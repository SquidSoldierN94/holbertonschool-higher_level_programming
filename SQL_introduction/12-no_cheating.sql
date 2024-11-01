-- This script updates the score to 10 in 'second_table' where the name is 'Bob'.
-- Save this file as 12-update_score_set_to_10_where_name_is_Bob.sql

-- The UPDATE command updates specified columns in the specified table where the condition is met.
UPDATE second_table 
SET score = 10 
WHERE name = 'Bob';
