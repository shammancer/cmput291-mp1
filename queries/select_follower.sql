SELECT * 
FROM follows 
WHERE follows.flwee = :usr
and follows.flwer = :flwer
