-- Create an index on the product_id column
CREATE INDEX idx_orders_product_id ON orders(product_id);
-- Query to get top 5 best-selling products
SELECT product_id, SUM(quantity) AS total_sold
FROM orders
GROUP BY product_id
ORDER BY total_sold DESC
LIMIT 5;