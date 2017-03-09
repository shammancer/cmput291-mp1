select u.usr, u.name, nvl(tweets.tweet_count,0) as tweet_count, nvl(follower.follower_count,0) as follower_count, nvl(following.following_count,0) as following_count
from 
	(select u.usr,u.name
	from users u
	where u.usr = :usr) u
	left outer join (select count(*) as follower_count, follows.flwee
	from follows
	group by follows.flwee) follower
on u.usr = follower.flwee
	left outer join (select count(*) as following_count, follows.flwer
	from follows
	group by follows.flwer) following
on u.usr = following.flwer
	left outer join (select count(*) as tweet_count, tweets.writer
	from tweets
	group by tweets.writer) tweets
on u.usr = tweets.writer