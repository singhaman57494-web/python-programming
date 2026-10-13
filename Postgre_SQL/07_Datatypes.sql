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
