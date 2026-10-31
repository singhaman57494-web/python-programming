CREATE DATABASE expense_tracker_db;

SELECT datname
FROM pg_database
WHERE datname = 'expense_tracker_db';