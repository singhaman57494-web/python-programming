--                     DATA TYPES

-- INT
age INT,

--   BIGINT
population BIGINT

--   DECIMAL
price DECIMAL(6, 2)

--    SMALLINT
quantity SMALLINT

--    NUMERIC
price NUMERIC(10, 2)

--     REAL
rating REAL

-- DOUBLE PRECISION
measurement DOUBLE PRECISION

--                 practice variable :- INT , SMALLINT, NUMERIC, REAL, DOUBLE PRECISION


CREATE TABLE products (
    id INT,
    quantity SMALLINT,
    price NUMERIC(10, 2),
    rating REAL,
    measurement DOUBLE PRECISION
);


--   CHAR
code CHAR(5)

--  VARCHAR
name VARCHAR(50)

--   TEXT
description TEXT

--                   practice variable:- CHAR, VARCHAR, TEXT

CREATE TABLE text_demo (
    code CHAR(5),
    name VARCHAR(50),
    description TEXT
);

INSERT INTO text_demo (code, name, description)
VALUES
('AB', 'Rahul', 'learning SQL'),
('ABCDE', 'Priya', 'Learning PostgreSQL data types');

SELECT * FROM text_demo;

--               check length

SELECT 
    code, 
    LENGTH(code) AS code_length,
    name, 
    LENGTH(name) AS name_length
FROM text_demo;

INSERT INTO text_demo (code, name, description)
VALUES (
    'XYZ',
    'Aman',
    'I am learning postgreSQL. today I learned CHAR, VARCHAR AND TEXT data types.'
);

SELECT name, description FROM text_demo;


--               DATE AND TIME

ALTER TABLE text_demo
ADD COLUMN event_date DATE,
ADD COLUMN event_time TIME,
ADD COLUMN event_at TIMESTAMP,
ADD COLUMN online_class_at TIMESTAMPTZ;

UPDATE text_demo
SET
    event_date = '2026-10-13',
    event_time = '18:30:00',
    event_at = '2026-10-13 18:30:00',
    online_class_at = '2026-10-13 18:30:00+05:30'
WHERE name = 'Aman';

--              current date , current time

UPDATE text_demo
SET
    event_date = CURRENT_DATE,
    event_time = CURRENT_TIME,
    event_at = LOCALTIMESTAMP,
    online_class_at = NOW()
WHERE name = 'Priya';


--                            BOOLEAN -true , false

ALTER TABLE text_demo
ADD COLUMN is_active BOOLEAN;

UPDATE text_demo
SET is_active = TRUE
WHERE name = 'Rahul';

SELECT name, is_active FROM text_demo;

--                          UUID - UNIQUE ID

ALTER TABLE text_demo
ADD COLUMN unique_id UUID;

UPDATE text_demo
set unique_id = gen_random_uuid()
WHERE name = 'Aman';

SELECT name, unique_id FROM text_demo;

--                       JSON / JSONB

ALTER TABLE text_demo
ADD COLUMN extre_info JSONB;

UPDATE text_demo
SET extre_info = '{
    "course": "SQL",
    "level": "biginner",
    "completed" : true
}' ::JSONB
WHERE name = 'Aman';

SELECT name, extre_info
FROM text_demo
WHERE name = 'Aman';

--                                     ARRAY

ALTER TABLE text_demo
ADD COLUMN subjects TEXT[];

UPDATE text_demo
SET subjects = ARRAY['math', 'English', 'science']
WHERE name = 'Rahul';

SELECT name, subjects
FROM text_demo
WHERE name = 'Rahul';