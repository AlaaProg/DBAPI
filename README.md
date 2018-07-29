# dbSqlApi

__Take Database for user !__
__Take User/password for Cpanel db 'phpmyadmin' !__
__Take token to  Controller by databases from anyapplication !__
__and Thx !__



###Step 1 : Install libs 

```
pip install install -r requirements.txt
```


###Step 2 : Create Database ' anyname ' AND   Import  ' Users.sql ' to Create tables  
<br>

###Step 3 : Go to DBAPI/settin.py set " defaulte  root user "
```

# DATABASE DRIVER  MYSQl 
DB_HOST   = '127.0.0.1'
DB_USER   = 'root'
DB_PASS   = ''  
NAME_DB   = '' 

```
###Step 4 : Run APP 
```

cd dbpy_api 

python DBAPI/manage.py runserver 

```

## Site : 
	1- create new user { path ' /cuser ' }
	2- login to take token
	3- index info and ref token  [ to 1 day ]

## API : Select Insert Update delete
	headers = {
		'API-TOKEN' : 'Token'
	}

#### GET : /api/<nametable>/<limit> 
	Select  ALL    

#### VIEW : /api/<nametable> 
	# Select 
	Json = {
		cols  : 'col1,col2',
		where : 'col1=3',
		limit : 4 # defaulte 100
	}

### POST : /api/<nametable>
	json = {
		data:{
			col1:'value',
			col2:'value',
			col3:'value'
		}
	}

### PUT : /api/<nametable>
	json = {
		data:{
			col2:'newvalue'
		}
		where:'col1=4'
	}


### DELETE : /api/<nametable>
	json = {
		where: 'col3=20'
	}

