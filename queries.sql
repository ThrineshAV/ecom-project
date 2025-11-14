-- 1. List all customers
SELECT * FROM customers;

-- 2. List all products and their prices
SELECT product_id, product_name, price FROM products;

-- 3. Total orders placed by each customer
SELECT 
    c.customer_id,
    c.name,
    COUNT(o.order_id) AS total_orders
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id;

-- 4. Join orders with order_items and products
SELECT 
    o.order_id,
    o.order_date,
    p.product_name,
    oi.quantity,
    p.price,
    (oi.quantity * p.price) AS total_amount
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id;

-- 5. Total revenue per payment method
SELECT 
    payment_method,
    SUM(amount) AS total_revenue
FROM payments
GROUP BY payment_method;

-- 6. Full order summary (customer + order + items + payment)
SELECT 
    o.order_id,
    c.name AS customer_name,
    p.product_name,
    oi.quantity,
    py.amount AS payment_amount,
    py.payment_method,
    o.order_date
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
LEFT JOIN payments py ON o.order_id = py.order_id;
