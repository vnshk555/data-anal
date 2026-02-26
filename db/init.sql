CREATE DATABASE analytics;

\connect analytics;

CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price NUMERIC(10,2),
    quantity INTEGER,
    city VARCHAR(100),
    total_amount NUMERIC(10,2)
);
