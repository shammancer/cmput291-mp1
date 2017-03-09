SELECT usr, pwd, name, email, city, timezone 
FROM users, follows 
WHERE users.usr = follows.flwer
and follows.flwee = :usr