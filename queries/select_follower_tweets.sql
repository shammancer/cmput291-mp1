-- Parameters :flwer
SELECT t.tid, t.writer, t.tdate, t.text
FROM (SELECT DISTINCT t.tid, t.writer, t.tdate, t.text
        FROM tweets t, follows f
        WHERE f.flwer=:flwer AND 
            f.flwee = t.writer 
    UNION 
    SELECT t.tid, t.writer, t.tdate, t.text
        FROM tweets t, follows f, retweets r
        WHERE f.flwer=:flwer AND
            f.flwee=r.usr AND
            t.tid=r.tid) t 
ORDER BY t.tdate desc

