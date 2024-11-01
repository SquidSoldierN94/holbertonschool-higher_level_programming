-- This script creates the database 'hbtn_0d_usa' and the table 'cities' in that database.
-- The 'cities' table has three columns: 'id' (INT, unique, auto-generated, NOT NULL, primary key),
-- 'state_id' (INT, NOT NULL, FOREIGN KEY referencing 'states.id'), and 'name' (VARCHAR(256), NOT NULL).
-- If the database or table already exists, the script does not fail.

-- Create the database 'hbtn_0d_usa' if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the created database
USE hbtn_0d_usa;

-- Create the table 'cities' if it does not exist
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
