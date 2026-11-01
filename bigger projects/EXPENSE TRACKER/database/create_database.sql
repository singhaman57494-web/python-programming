CREATE DATABASE expense_tracker_db;

SELECT datname
FROM pg_database
WHERE datname = 'expense_tracker_db';

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
AND table_name = 'transactions';

SELECT current_database(), current_schema();

SELECT *FROM transactions;