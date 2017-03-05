-- Parameters :flwee
SELECT DISTINCT t.tid, t.writer, t.tdate, t.text
FROM (SELECT t.tid, t.writer, t.tdate, t.text
        FROM tweets t, follows f
        WHERE f.flwee=:flwee AND 
            f.flwer=t.writer 
    UNION 
    SELECT t.tid, t.writer, t.tdate, t.text
        FROM tweets t, follows f, retweets r
        WHERE f.flwee=:flwee AND
            f.flwer=r.usr AND
            t.tid=r.tid) t 
ORDER BY t.tdate

