-- This script creates the database 'hbtn_0d_usa' and the table 'states' in that database.
-- The 'states' table has two columns: 'id' (INT, unique, auto-generated, NOT NULL, primary key)
-- and 'name' (VARCHAR(256), NOT NULL).
-- If the database or table already exists, the script does not fail.

-- Create the database 'hbtn_0d_usa' if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the created database
USE hbtn_0d_usa;

-- Create the table 'states' if it does not exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
