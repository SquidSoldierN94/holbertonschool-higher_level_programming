-- This script creates a table named 'second_table' if it does not already exist and inserts multiple records into it.
-- Save this file as 9-create_second_table.sql

-- The CREATE TABLE IF NOT EXISTS command creates a new table only if it does not already exist.
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- The INSERT INTO command inserts multiple records into the specified table.
INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
