-- Parameters :usr
SELECT usr, pwd, name, email, city, timezone 
FROM users 
WHERE usr=:usr
