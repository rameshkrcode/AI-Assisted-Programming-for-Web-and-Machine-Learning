
-- Add an index to optimize the WHERE clause
CREATE INDEX idx_orders_user_id ON orders(user_id);

-- Optimized query using indexed column
SELECT * FROM orders WHERE user_id = 101;
