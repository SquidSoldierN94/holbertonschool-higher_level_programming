-- This script deletes records from 'second_table' where the score is less than or equal to 5.
-- Save this file as 13-delete_where_score_le_5.sql

-- The DELETE command deletes records from the specified table where the condition is met.
DELETE FROM second_table 
WHERE score <= 5;
