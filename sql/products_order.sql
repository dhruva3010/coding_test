create schema products_order;
use products_order;
CREATE TABLE Customers (
  customer_id INTEGER NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  phone VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(255) NOT NULL,
  state VARCHAR(255) NOT NULL,
  zipcode VARCHAR(255) NOT NULL,
  PRIMARY KEY (customer_id)
);

CREATE TABLE Orders (
  order_id INTEGER NOT NULL AUTO_INCREMENT,
  customer_id INTEGER NOT NULL,
  order_date DATETIME NOT NULL,
  total_amount DECIMAL(10,2) NOT NULL,
  status VARCHAR(255) NOT NULL,
  PRIMARY KEY (order_id),
  FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE OrderItems (
  order_item_id INTEGER NOT NULL AUTO_INCREMENT,
  order_id INTEGER NOT NULL,
  product_id INTEGER NOT NULL,
  quantity INTEGER NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (order_item_id),
  FOREIGN KEY (order_id) REFERENCES Orders(order_id),
  FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

CREATE TABLE Products (
  product_id INTEGER NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  category VARCHAR(255) NOT NULL,
  PRIMARY KEY (product_id)
);
