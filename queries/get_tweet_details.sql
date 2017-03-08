select nvl(rplyt.rplycnt,0) as replies,nvl(rt.rtcnt,0) as retweets
from
        (select t.tid
        from tweets t
        where t.tid =:tid
        group by tid,text
        ) t
        left outer join (select count(*) as rplycnt, tweets.replyto
        from tweets
        group by tweets.replyto
        ) rplyt
on t.tid = rplyt.replyto
        left outer join(select count(*) as rtcnt, rt.tid
        from retweets rt
        group by rt.tid
        ) rt
on rt.tid= t.tid
