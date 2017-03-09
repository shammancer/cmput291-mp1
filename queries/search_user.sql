select usr, pwd,name,email,city,timezone
from users
where users.name like :keyword