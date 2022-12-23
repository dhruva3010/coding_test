create schema products_order;

create table products_order.product (
    product_id CHAR(10) PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    product_description VARCHAR(500),
    quantity numeric(10),
    price numeric(10,4),
    manufacture_date DATE,
    product_added_on TIMESTAMP
)

create table products_order.customers (
    customer_id CHAR(50) PRIMARY KEY,
    username VARCHAR(250) NOT NULL UNIQUE,
    name VARCHAR(500),
    join_date TIMESTAMP,
    email VARCHAR(100),
    phone CHAR(15)
)

create table products_order.orders (
    product_id CHAR(10) FOREIGN KEY ON products_order.product.product_id,
    order_id CHAR(50) PRIMARY KEY,
    order_date TIMESTAMP,
    quantity_ordered numeric(10),
    customer_id CHAR(50) FOREIGN KEY ON products_order.customers.customer_id,
    total_price numeric(10,4),
    payment_mode VARCHAR(100),
    salesman_id CHAR(50) FOREIGN KEY ON products_order.salesman.salesman_id,
    locations_id CHAR(50) FOREIGN KEY ON products_order.locations.locations_id
)

create table products_order.locations (
    locations_id CHAR(50) PRIMARY KEY,
    location VARCHAR(100)
)

create table products_order.salesman (
    salesman_id CHAR(50) PRIMARY KEY,
    name VARCHAR(500),
    address VARCHAR(1000),
    GSTIN CHAR(20),
    contact CHAR(15),
    join_date DATE
)