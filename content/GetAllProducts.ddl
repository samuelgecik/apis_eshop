SELECT products.*, categories.category_name FROM products
INNER JOIN categories  
ON products.category_ID = categories.category_ID