import jwt,datetime,re
from   flask  import request,redirect,session,render_template
from  .model  import MySQL
from  application import app

# @ ADMIN DB 
sql = MySQL(
		host    = app.config['DB_HOST'], 
		user    = app.config['DB_USER'],
		db      = app.config['NAME_DB'],
		password= app.config['DB_PASS'],
	)

def index():

	if not session.get('login'): return redirect('luser')



	if request.method == 'POST' and session.get('login'):
		
		db = sql.select('DBT.Users',where="`email`='%s'"%(session.get('login')))[0]

		payload = {
		    'exp'     : datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=0),
		    'iat'     : datetime.datetime.utcnow(),
		    'user'    : db['user'],
		    'pass'    : db['password'],
		    "db_user" : db['db_user']
		};

		tken = jwt.encode( payload,app.config['SECRET_KEY'],algorithm='HS256')

		sql.update('DBT.Users',{'tk_user':tken.decode('utf-8')},"`email`='%s'"%session.get('login'))


	db = sql.select('DBT.Users',where="`email`='%s'"%(session.get('login')))

	if not db:
		session.clear()
		return redirect('luser')

			
	return render_template("index.html",db=db[0])

def creatUser():

	if session.get('login') : return redirect('/')

	if request.method == 'POST':

		form = request.form 

		if not re.match(r'^[a-z\.\_]+@+[a-z]+\.+[a-z]{2,4}',form['#email']) :

			return render_template("createUser.html",err='block',error='Errot Email')

		elif not re.match(r'^[A-Za-z\.\_!@#$%^&*()]+$',form['#pass']):

			return render_template("createUser.html",err='block',error='Error Password must [a to z and !@#$$...]')

		

		dbname = datetime.datetime.strftime(datetime.datetime.utcnow(),"%Y%m%d_"+form['#email'].split('@')[0])

		payload = {
		    'exp'     : datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=360),
		    'iat'     : datetime.datetime.utcnow(),
		    'user'    : form['#email'].split('@')[0],
		    'pass'    : form['#pass'],
		    "db_user" : dbname
		};
		tken = jwt.encode( payload,app.config['SECRET_KEY'],algorithm='HS256',)
		dbcreate = sql.create_user(form['#email'].split('@')[0],form['#pass'],dbname)
		# if dbcreate :

		sql.insert('DBT.Users',{
				'name'     :form['#name'],
				'email'    :form['#email'],
				'user'     :form['#email'].split('@')[0],
				'password' :form['#pass'],
				'tk_user'  :"%s"%tken.decode("utf-8"),
				"db_user"  :dbname
			})


		return redirect('luser')

	return render_template("createUser.html")

def loginUser():

	if session.get('login') : return redirect('/')

	error,err = '','none'

	if request.method == 'POST':

		form = request.form 

		if form.get('#email') and form.get('#pass'):

			db = sql.select('DBT.Users','email,password',where="`email`='%s' AND `password`='%s'"%(form['#email'],form['#pass']))

			if db:
				session['login'] = db[0]['email']
				session['dtime'] = datetime.datetime.strftime(datetime.datetime.utcnow(),'%Y-%m-%d')

				return redirect('/')

		error = 'Email/password notcurrect !!'
		err   = 'block'

	return render_template("login.html",err=err,error=error)