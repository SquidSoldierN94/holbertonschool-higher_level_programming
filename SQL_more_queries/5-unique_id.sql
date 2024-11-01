-- This script creates the table 'unique_id' in the specified database.
-- The table has two columns: 'id' (INT with default value 1 and UNIQUE constraint) 
-- and 'name' (VARCHAR(256)).
-- If the table already exists, the script does not fail.

-- The CREATE TABLE IF NOT EXISTS command creates a new table only if it does not already exist.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
