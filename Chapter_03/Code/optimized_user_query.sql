
-- Create an index to speed up email lookups
CREATE INDEX idx_users_email ON users(email);

-- Optimized query for retrieving user details efficiently
SELECT user_id, name 
FROM users 
WHERE email LIKE 'example@gmail.com%' 
ORDER BY created_at DESC 
LIMIT 100;
