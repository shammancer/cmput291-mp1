-- Data prepared by Harley Vanselow, vanselow@ualberta.ca, and published on 4/2/2017
-- Expansion pack 1: 291 TAs
insert into users values (100,'pwd','Ehsan Kamalloo','ehsan@aol.ca','Edmonton',-7);
insert into users values (101,'pwd','Esha','Esha@mail.com','Edmonton',-7);
insert into users values (102,'pwd','Curtis Malainey','cujo@aol.com','Cochrane',-7);
insert into users values (103,'pwd','Saeed Sarabchi','saeed@aol.com','Edmonton',-7);
insert into users values (104,'pwd','Ehsaner Kamallooer','looer@send.ca','Edmonton',-7);
insert into users values (105,'pwd','Sara Farazi','sara@gmail.com','Edmonton',-7);

insert into users values (200,'pwd','Genji','g@ow.com','Edmonton',-7);
insert into users values (201,'pwd','McCree','mcree@ow.com','Edmonton',-7);
insert into users values (202,'pwd','Pharah','phar@ow.com','Edmonton',-7);
insert into users values (203,'pwd','Reaper','reap@ow.com','Edmonton',-7);
insert into users values (204,'pwd','Soldier76','76@ow.com','Edmonton',-7);
insert into users values (205,'pwd','Sombra','sombra@ow.com','Edmonton',-7);
insert into users values (206,'pwd','Tracer','trace@ow.com','Edmonton',-7);
insert into users values (207,'pwd','Bastion','bastion@ow.com','Edmonton',-7);
insert into users values (208,'pwd','Hanzo','hanzo@ow.com','Edmonton',-7);
insert into users values (209,'pwd','Junkrat','junk@ow.com','Edmonton',-7);
insert into users values (210,'pwd','Mei','mei@ow.com','Edmonton',-7);
insert into users values (211,'pwd','Torbjorn','torb@ow.com','Edmonton',-7);
insert into users values (212,'pwd','Widowmaker','widow@ow.com','Edmonton',-7);
insert into users values (213,'pwd','DVa','dva@ow.com','Edmonton',-7);
insert into users values (214,'pwd','Reinhardt','rien@ow.com','Edmonton',-7);
insert into users values (215,'pwd','Roadhog','hog@ow.com','Edmonton',-7);
insert into users values (216,'pwd','Winston','win@ow.com','Edmonton',-7);
insert into users values (217,'pwd','Zarya','zarya@ow.com','Edmonton',-7);
insert into users values (218,'pwd','Ana','ana@ow.com','Edmonton',-7);
insert into users values (219,'pwd','Lucio','lucio@ow.com','Edmonton',-7);
insert into users values (220,'pwd','Mercy','mercy@ow.com','Edmonton',-7);
insert into users values (221,'pwd','Symmetra','symm@ow.com','Edmonton',-7);
insert into users values (222,'pwd','Zenyatta','zen@ow.com','Edmonton',-7);
insert into users values (223,'pwd','Doomfist','df@ow.com','Edmonton',-7);

insert into users values(300,'pwd','john doe','jd@ua.com','Edmonton',-7);

insert into follows values (100,102,'15-JAN-2017');
insert into follows values (105,102,'20-SEP-2014');
insert into follows values (102,101,'15-OCT-2016');
insert into follows values (103,105,'11-NOV-2016');
insert into follows values (103,100,'05-JUN-2016');
insert into follows values (100,105,'02-FEB-2017');
insert into follows values (102,105,'14-SEP-2016');
insert into follows values (101,102,'15-OCT-2016');
insert into follows values (101,103,'15-OCT-2010');
insert into follows values (101,105,'15-OCT-2010');


insert into follows values (200,222,'15-OCT-2010');
insert into follows values (200,220,'15-NOV-2010');
insert into follows values (208,200,'15-OCT-2010');

insert into follows values (205,200,'15-DEC-2010');
insert into follows values (205,201,'15-OCT-2010');
insert into follows values (205,202,'15-AUG-2016');
insert into follows values (205,203,'15-OCT-2010');
insert into follows values (205,204,'11-SEP-2016');
insert into follows values (205,206,'16-OCT-2010');
insert into follows values (205,207,'17-JUN-2010');
insert into follows values (205,208,'15-JUL-2015');
insert into follows values (205,209,'13-OCT-2010');
insert into follows values (205,210,'15-MAR-2010');
insert into follows values (205,211,'16-APR-2010');
insert into follows values (205,212,'25-OCT-2015');
insert into follows values (205,213,'15-OCT-2010');
insert into follows values (205,214,'25-APR-2014');
insert into follows values (205,215,'15-OCT-2014');
insert into follows values (205,216,'16-FEB-2010');
insert into follows values (205,217,'15-OCT-2016');
insert into follows values (205,218,'15-DEC-2014');
insert into follows values (205,219,'13-DEC-2016');
insert into follows values (205,220,'05-OCT-2010');
insert into follows values (205,221,'03-OCT-2013');
insert into follows values (205,222,'09-OCT-2012');

insert into follows values (203,212,'25-JAN-2016');
insert into follows values (203,205,'03-JAN-2010');
insert into follows values (212,205,'07-OCT-2016');
insert into follows values (213,219,'13-MAR-2010');
insert into follows values (218,214,'15-OCT-2012');
insert into follows values (214,218,'15-AUG-2016');
insert into follows values (209,202,'14-AUG-2016');
insert into follows values (209,201,'15-OCT-2016');
insert into follows values (209,214,'12-OCT-2015');
insert into follows values (209,210,'15-SEP-2014');
insert into follows values (218,220,'12-OCT-2016');

insert into follows values (216,102,'12-OCT-2016');
insert into follows values (216,105,'12-OCT-2016');
insert into follows values (216,210,'12-OCT-2016');
insert into follows values (216,200,'12-OCT-2016');

insert into follows values(300,105,'13-MAR-2010');
insert into follows values(300,210,'01-FEB-2017');
insert into follows values(300,200,'01-FEB-2017');

insert into follows values(205,300,'01-FEB-2017');
insert into follows values(209,300,'01-FEB-2017');
insert into follows values(212,300,'01-FEB-2017');
insert into follows values(223,300,'01-FEB-2017');



insert into tweets values (1,101,'22-NOV-2015','291 lab sections are so much fun.',null);
insert into tweets values (0,102,'25-DEC-2016','Hate to say it but #edgyidea.',null);
insert into tweets values (2,102,'10-JAN-2017','Computer Engineering>Computer Science.',null);
insert into tweets values (3,103,'10-JAN-2015','Testing my tweets.',null);
insert into tweets values (4,104,'11-MAY-2016','I think bad things are bad #Agreeable',null);
insert into tweets values (5,104,'12-MAY-2016','Good things should happend more #Agreeable',null);
insert into tweets values (6,105,'12-APR-2015','#Dolphins are neat.',null);
insert into tweets values (7,105,'24-APR-2015','#Dolphins my favorite sea dwelling mammal.',null);
insert into tweets values (8,211,'01-JAN-2016','Aardvark pays off', null);
insert into tweets values (9,201,'01-JAN-2016','Im the quick', null);
insert into tweets values (10,212,'01-JAN-2016','*French sounds* #Talon',  null);
insert into tweets values (11,208,'01-JAN-2016','Super sad about killing bro',  null);
insert into tweets values (12,220,'01-JAN-2016','Heros never die!', null);
insert into tweets values (13,221,'01-JAN-2016','Why does everyone melt? #BeamSniper',  null);
insert into tweets values (14,209,'01-JAN-2016','Robbing banks and whatnot', null);
insert into tweets values (15,203,'01-JAN-2016','*Edge sounds* #Talon', null);
insert into tweets values (16,216,'01-JAN-2016','Taser is better than fists.', null);
insert into tweets values (17,205,'01-JAN-2016','Be right back', null);
insert into tweets values (18,213,'01-JAN-2016','Is this easy mode?',  null);
insert into tweets values (19,104,'12-AUG-2015','(1)They will look up and shout "Save us!" #edmonton',null);
insert into tweets values (20,104,'13-AUG-2015','(2)and Ill whisper "no."#edmonton',null);
insert into tweets values (21,203,'12-JUN-2012','Hate dolphins #edgyidea #Dolphins',null);
insert into tweets values (22,215,'13-JUN-2012','Dolphins are food #edgyidea #Dolphins',null);

insert into tweets values (23,100,'26-DEC-2016','How could you say that #Outrage.',0);
insert into tweets values (24,101,'26-DEC-2016','Unbelievable #Outrage.',0);
insert into tweets values (25,103,'26-DEC-2016','Cool ideas, tell me more.',0);
insert into tweets values (26,104,'26-DEC-2016','Im indifferent to this issue.',0);

insert into tweets values (27,102,'27-DEC-2016','Thats just like,your opinion man...',24);

insert into tweets values (28,100,'01-JAN-2016','Hello World', 3);
insert into tweets values (29,217,'01-FEB-2016','Not for long', 18);

--edgyidea retweets
insert into retweets values (105,0,'25-DEC-2017');
insert into retweets values (101,0,'25-DEC-2017');
insert into retweets values (100,0,'25-DEC-2017');

--Test tweet retweets
insert into retweets values (100,3,'25-JUN-2017');
insert into retweets values (101,3,'25-JUN-2017');
insert into retweets values (102,3,'25-JUN-2017');
insert into retweets values (103,3,'25-JUN-2017');

--Dolphins are cool retweets
insert into retweets values (100,6,'21-MAY-2016');
insert into retweets values (101,6,'25-JUN-2017');
insert into retweets values (102,6,'18-JUL-2016');
insert into retweets values (103,6,'10-AUG-2017');
insert into retweets values (104,6,'26-SEP-2016');
insert into retweets values (219,6,'28-DEC-2016');

--Heroes never die retweets
insert into retweets values (200,12,'01-JAN-2016');
insert into retweets values (201,12,'01-JAN-2016');
insert into retweets values (202,12,'01-JAN-2016');

insert into retweets values (219,27,'28-DEC-2016');


insert into hashtags values ('edgyidea');
insert into hashtags values ('Agreeable');
insert into hashtags values ('Dolphins');
insert into hashtags values ('Outrage');
insert into hashtags values ('edmonton');

insert into mentions values (0, 'edgyidea');
insert into mentions values (21, 'edgyidea');
insert into mentions values(22,'edgyidea');
insert into mentions values (4, 'Agreeable');
insert into mentions values (5, 'Agreeable');

insert into mentions values (23, 'Outrage');
insert into mentions values (24, 'Outrage');
insert into mentions values (6,'Dolphins');
insert into mentions values (7,'Dolphins');
insert into mentions values (21,'Dolphins');
insert into mentions values(22,'Dolphins');



insert into mentions values(5,'edmonton');
insert into mentions values(20,'edmonton');



insert into lists values ('tas',100);
insert into lists values ('engineers',105);
insert into lists values ('overwatch',216);
insert into lists values ('talon',203);

insert into includes values ('engineers',102);

insert into includes values ('tas',100);
insert into includes values ('tas',101);
insert into includes values ('tas',102);
insert into includes values ('tas',103);
insert into includes values ('tas',104);
insert into includes values ('tas',105);
insert into includes values ('tas',216);

insert into includes values ('overwatch',200);
insert into includes values ('overwatch',201);
insert into includes values ('overwatch',202);
insert into includes values ('overwatch',204);
insert into includes values ('overwatch',206);
insert into includes values ('overwatch',207);
insert into includes values ('overwatch',208);
insert into includes values ('overwatch',210);
insert into includes values ('overwatch',211);
insert into includes values ('overwatch',213);
insert into includes values ('overwatch',214);
insert into includes values ('overwatch',216);
insert into includes values ('overwatch',217);
insert into includes values ('overwatch',218);
insert into includes values ('overwatch',219);
insert into includes values ('overwatch',220);
insert into includes values ('overwatch',221);
insert into includes values ('overwatch',222);

insert into includes values ('talon',102);
insert into includes values ('talon',203);
insert into includes values ('talon',205);
insert into includes values ('talon',209);
insert into includes values ('talon',212);
insert into includes values ('talon',215);
insert into includes values ('talon',223);
commit;




