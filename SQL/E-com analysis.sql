-- SELECT * FROM customers;
-- SELECT * FROM order_items;
-- SELECT * FROM orders;
-- SELECT * FROM products;

-- SELECT SUM(amount) AS total_revenue
-- FROM payments;

-- SELECT p.product_name,
--        SUM(oi.quantity * p.price) AS revenue
-- FROM order_items oi
-- JOIN products p ON oi.product_id = p.product_id
-- JOIN orders o ON oi.order_id = o.order_id
-- WHERE o.order_status = 'Delivered'
-- GROUP BY p.product_name
-- ORDER BY revenue DESC;

-- SELECT COUNT(*) AS cancelled
-- FROM orders
-- WHERE order_status = 'Cancelled';

-- SELECT c.name,
--        SUM(p.amount) AS total_spent
-- FROM customers c
-- JOIN orders o ON c.customer_id = o.customer_id
-- JOIN payments p ON o.order_id = p.order_id
-- GROUP BY c.name
-- ORDER BY total_spent DESC;

SELECT p.product_name,
       SUM(oi.quantity) AS total_sold
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC;
