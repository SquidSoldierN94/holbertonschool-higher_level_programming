-- This script creates a table named 'first_table' if it does not already exist.
-- Save this file as 4-create_first_table.sql

-- The CREATE TABLE IF NOT EXISTS command creates a new table only if it does not already exist.
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
