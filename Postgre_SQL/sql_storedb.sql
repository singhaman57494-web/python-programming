--                task- storedb


CREATE TABLE customers(
    cust_id SERIAL PRIMARY KEY,
    cust_name VARCHAR(100) NOT NULL
);

CREATE TABLE orders(
    ord_id SERIAL PRIMARY KEY,
    ord_date DATE NOT NULL,
    cust_id INTEGER NOT NULL,
    FOREIGN KEY (cust_id) REFERENCES customers(cust_id)
);

CREATE TABLE products(
    p_id SERIAL PRIMARY KEY,
    p_name VARCHAR(100) NOT NULL,
    price NUMERIC NOT NULL
);

CREATE TABLE order_items (
    item_id SERIAL PRIMARY KEY,
    ord_id INTEGER NOT NULL,
    p_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (ord_id) REFERENCES orders (ord_id),
    FOREIGN KEY (p_id) REFERENCES products (p_id)
);

INSERT INTO customers (cust_name)
VALUES
    ('Raju'), ('Sham'), ('paul'), ('Alex');

INSERT INTO orders (ord_date, cust_id)
VALUES
    ('2024-01-01', 1),
    ('2024-02-01', 2),
    ('2024-03-01', 3),
    ('2024-04-04', 2);

INSERT INTO products (p_name, price)
VALUES
    ('laptop', 55000.00),
    ('mouse', 500),
    ('keyboard', 800.00),
    ('cable', 250.00);

INSERT INTO order_items (ord_id, p_id, quantity)
VALUES
    (1, 1, 1), 
    (1, 4, 2),
    (2, 1, 1),
    (3, 2, 1),
    (3, 4, 5),
    (4, 3, 1);



SELECT p.p_name FROM order_items oi
    JOIN 
        products p ON oi.p_id = p.p_id;

CREATE VIEW billing_info AS

SELECT
    c.cust_name,
    o.ord_date,
    p.p_name,
    p.price,
    oi.quantity,
    (oi.quantity*p.price) AS total_price
FROM order_items oi
    JOIN 
        products p ON oi.p_id = p.p_id
    JOIN
        orders o ON o.ord_id = oi.ord_id
    JOIN 
        customers c ON o.cust_id = c.cust_id;
    
    -- view

SELECT * FROM billing_info;

select p_name, SUM(total_price) FROM
billing_info
    GROUP BY p_name
    HAVING SUM(total_price) > 1000;

SELECT
    COALESCE (p_name, 'total'),
    SUM(total_price) AS amount
FROM billing_info
    GROUP BY
    ROLLUP (p_name) ORDER BY amount;

TRUNCATE TABLE order_items  RESTART IDENTITY CASCADE;
TRUNCATE TABLE products RESTART IDENTITY CASCADE;