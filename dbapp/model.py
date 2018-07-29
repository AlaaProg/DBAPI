import mysql.connector as sql 

class MySQL():

	def __init__(self,**config:dict):
		try:
			self.sql = sql.connect(**config)

			self.cur = self.sql.cursor(dictionary=True)

		except sql.Error as er:
			raise er
	
	# $SQL SELECT 
	def select(self,table:str,col:str="*",where:str="1=1",limit:int=100):
		self.cur.execute("SELECT %s FROM %s WHERE %s LIMIT %d"%(col,table,where,limit))

		return self.cur.fetchall()

	# $SQL Insert 
	def insert(self,table:str,data:dict={}):
		cols   = ",".join([ '`'+i+'`' for i in data.keys()])
		values = str(tuple(data.values()))
		self.cur.execute("INSERT INTO %s (%s) VALUES %s"%(table,cols,values))
		self.sql.commit()

	def update(self,table:str,data:dict,where:str):
		# UPDATE `post` SET `postID` = '1' WHERE `post`.`postID` = 11;

		cols = ['`%s` ="%s"'%(v,k) for v,k in data.items()]
		cols = ','.join(cols)

		self.cur.execute("UPDATE %s SET %s WHERE %s"%(table,cols,where))
		self.sql.commit()


	# $SQL CREATE ADMIN ( FOR ADMIN )
	def create_user(self,user:str,password:str,dbname:str,host:str='127.0.0.1') -> dict:
		try:

			self.cur.execute("SELECT PASSWORD('%s')"%password)
			password = self.cur.fetchall()[0]["PASSWORD('%s')"%password]
			host_user = " '%s'@'%s' "%(user,host)
			self.cur.execute("CREATE DATABASE %s"%dbname)
			self.cur.execute("CREATE USER %s IDENTIFIED VIA mysql_native_password USING '%s';"%(host_user,password))
			self.cur.execute("GRANT ALL PRIVILEGES ON `%s`.* TO %s WITH GRANT OPTION;"%(dbname,host_user))
			self.sql.commit()

			return {'password':password,'user':user,"dbname":dbname,'host':host}
			
		except sql.Error as error:
			return {'Error':error}





