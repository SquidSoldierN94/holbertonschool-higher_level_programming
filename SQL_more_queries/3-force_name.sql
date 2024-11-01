-- This script creates the table 'force_name' in the specified database.
-- The table has two columns: 'id' (INT) and 'name' (VARCHAR(256) NOT NULL).
-- If the table already exists, the script does not fail.

-- The CREATE TABLE IF NOT EXISTS command creates a new table only if it does not already exist.
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
