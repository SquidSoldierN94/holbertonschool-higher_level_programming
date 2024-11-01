-- This script creates the MySQL user 'user_0d_1' with all privileges on the MySQL server.
-- The user's password is set to 'user_0d_1_pwd'.
-- If the user already exists, the script does not fail.

-- The CREATE USER IF NOT EXISTS command creates a new user only if it does not already exist.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- The GRANT ALL PRIVILEGES ON *.* command grants all privileges on the server to the specified user.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
