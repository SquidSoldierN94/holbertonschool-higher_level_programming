-- This script creates the database 'hbtn_0d_2' and the user 'user_0d_2'.
-- The user 'user_0d_2' is granted only SELECT privilege on the 'hbtn_0d_2' database.
-- The user's password is set to 'user_0d_2_pwd'.
-- If the database or user already exists, the script does not fail.

-- The CREATE DATABASE IF NOT EXISTS command creates a new database only if it does not already exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- The CREATE USER IF NOT EXISTS command creates a new user only if it does not already exist.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- The GRANT SELECT ON database.* command grants the SELECT privilege on all tables in the specified database to the specified user.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
