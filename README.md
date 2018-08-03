# dbSqlApi

	idea :
		when new user register
		Gave one database and username/password to access to controller panel and
		token to access api to write, read,update and delete


	like : 
		you use javascript ,html and css need to access to database 
		you can use the ajax to access database by api  to do the select , insert , update and delete 
		(  not need to write backend  )

### Step 1 : Install libs 

```
pip install install -r requirements.txt
```


### Step 2 : Create Database ' anyname ' AND   Import  ' Users.sql ' to Create tables  
<br>

### Step 3 : Go to DBAPI/settin.py set " defaulte  root user "
```

# DATABASE DRIVER  MYSQl 
DB_HOST   = '127.0.0.1'
DB_USER   = 'root'
DB_PASS   = ''  
NAME_DB   = '' 

```
### Step 4 : Run APP 
```

cd dbpy_api 

python DBAPI/manage.py runserver 

```

## WebSite localhost:8000/: 
	1- create new user { path ' /cuser ' }
	2- login to take token
	3- index info and ref token  [ to 1 day ]

## API : Select Insert Update delete
	headers = {
		'API-TOKEN' : 'Token'
	}

#### GET : /api/<nametable>/<limit> 
	# Select  ALL    

#### VIEW : /api/<nametable> 
	# Select row 
	Json = {
		cols  : 'col1,col2',
		where : 'col1=3',
		limit : 4 # defaulte 100
	}

### POST : /api/<nametable>
	# Insert row
	json = {
		data:{
			col1:'value',
			col2:'value',
			col3:'value'
		}
	}

### PUT : /api/<nametable>
	# update row 
	json = {
		data:{
			col2:'newvalue'
		}
		where:'col1=4'
	}


### DELETE : /api/<nametable>
	# delete  row
	json = {
		where: 'col3=20'
	}

