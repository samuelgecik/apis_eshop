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

INSERT INTO categories
VALUES (1,'buggy');
INSERT INTO categories
VALUES (2,'monster');
INSERT INTO categories
VALUES (3,'rallye');
INSERT INTO categories
VALUES (4,' accessory');

INSERT INTO products
VALUES (1,1,'RC auto Traxxas Bandit 1:10 RTR, modročierna',265,10,'RC model auta Traxxas Bandit je výkonná 2WD buggy s vodoodolnou elektronikou. 
Modifikovaný motor Titan 550 12T má vysoký výkon, prakticky bezúdržbovú prevádzku a dlhodobý výkon. Vodoodolný regulátor XL-5 LVD, RC súprava TQ 2,4 GHz, rýchlonabíjačka',
);
INSERT INTO products
VALUES (2,2,'zelene auto',40,120);
INSERT INTO products
VALUES (3,3,'modre auto',50,100);
INSERT INTO products
VALUES (4,2,'cervene auto',40,120);
INSERT INTO products
VALUES (5,4,'bateria',40,120);

INSERT INTO customers
VALUES (1,'John','Monday','0911654899','johnMonday@gmail.com','Hlavná5','Kosice','Slovakia');
INSERT INTO customers
VALUES (2,'Jack','Erst','0915234877','jackRersty@gmail.com','Hlavná18','Kosice','Slovakia');
INSERT INTO customers
VALUES (3,'Daniel','White','0910234852','danielWhite@gmail.com','Dlhá4','Kosice','Slovakia');
INSERT INTO customers
VALUES (4,'Ivana','Grey','0911865447','ivanaGrey@gmail.com','Krátka45','Kosice','Slovakia');
INSERT INTO customers
VALUES (5,'Sofia','Swift','0910897523','sofiaSwift@gmail.com','Hlavná125','Kosice','Slovakia');

INSERT INTO orders
VALUES (1,1,'2021-11-26 14:29:36');
INSERT INTO orders
VALUES (2,2,'2021-11-26 11:12:45');
INSERT INTO orders
VALUES (3,3,'2021-11-26 09:55:21');
INSERT INTO orders
VALUES (4,3,'2021-11-26 09:57:25');

INSERT INTO order_items
VALUES (1,1,1,1);
INSERT INTO order_items
VALUES (2,1,2,1);
INSERT INTO order_items
VALUES (3,1,3,1);

INSERT INTO order_items
VALUES (4,2,1,1);
INSERT INTO order_items
VALUES (5,2,4,1);

INSERT INTO order_items
VALUES (6,3,3,1);
INSERT INTO order_items
VALUES (7,4,1,1);
