CREATE TABLE  categories (
    category_ID INT NOT NULL,
    category_name VARCHAR(50) NOT NULL,
    CONSTRAINT PK_category PRIMARY KEY (category_ID)
);

CREATE TABLE products (
    product_ID INT NOT NULL,
    category_ID INT NOT NULL,
    product_name VARCHAR(50) NOT NULL,
    product_price INT NOT NULL,
    product_pieces_WH INT NOT NULL,
    card_description VARCHAR(200) NOT NULL,
    short_description VARCHAR(300) NOT NULL,
    long_description VARCHAR(2000) NOT NULL,
    img_url VARCHAR(50),
    CONSTRAINT PK_product PRIMARY KEY (product_ID),
    CONSTRAINT FK_category_ID_products FOREIGN KEY (category_ID)
        REFERENCES categories (category_ID)
        ON DELETE CASCADE
);

CREATE TABLE customers(
    customer_ID INT NOT NULL,
    firstName VARCHAR(20) NOT NULL,
    lastName VARCHAR(30) NOT NULL,
    phone VARCHAR(30) NOT NULL,
    email VARCHAR(50) NOT NULL,
    address_line VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL,

    CONSTRAINT PK_customer PRIMARY KEY (customer_ID)
);

CREATE TABLE orders(
    order_ID INT NOT NULL,
    customer_ID INT NOT NULL,
    date_placed DATETIME NOT NULL,

    CONSTRAINT PK_orders PRIMARY KEY (order_ID),
    CONSTRAINT FK_customer_ID_orders FOREIGN KEY (customer_ID)
        REFERENCES customers (customer_ID)
);

CREATE TABLE order_items(
    order_item_ID INT NOT NULL,
    order_ID INT NOT NULL,
    product_ID INT NOT NULL,
    item_quantity INT NOT NULL,

    CONSTRAINT PK_order_items PRIMARY KEY (order_item_ID),
    CONSTRAINT FK_product_ID_order_items FOREIGN KEY (product_ID)
        REFERENCES products (product_ID),
    CONSTRAINT FK_order_ID_order_items FOREIGN KEY (order_ID)
        REFERENCES orders (order_ID)
        ON DELETE CASCADE
);