(select usr, pwd,name,email,city,timezone, 1, length(trim(name))
from users
where users.name like :keyword)
union
(select usr, pwd,name,email,city,timezone, 2, length(trim(city))
from users
where users.city like :keyword
minus
select usr, pwd,name,email,city,timezone, 2, length(trim(city))
from users
where users.name like :keyword)
order by 7,8