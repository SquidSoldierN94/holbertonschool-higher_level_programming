-- Script to manage MySQL users and their privileges.

-- Create user 'user_0d_1' if it does not already exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';

-- Create user 'user_0d_2' if it does not already exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Show grants for 'user_0d_1'
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Show grants for 'user_0d_2'
SHOW GRANTS FOR 'user_0d_2'@'localhost';
