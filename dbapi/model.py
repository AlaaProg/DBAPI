import mysql.connector as sql 

class MySQL():
	
	def __init__(self,**config:dict):
		try:
			self.sql = sql.connect(**config)
			#  (
			#   	buffered=None, raw=None, prepared=None, 
			#   	cursor_class=None, dictionary=None, named_tuple=None
			# )
			self.cur = self.sql.cursor(dictionary=True)

		except sql.Error as er:
			raise er

	

	def select(self,table:str,col:str="*",where:str="1=1",limit:int=100)->dict:
		try:
			
			self.cur.execute("SELECT %s FROM %s WHERE %s LIMIT %d"%(col,table,where,limit))

			return self.cur.fetchall()

		except Exception as err :
			return err

	def insert(self,table:str,data:dict={})->bool:
		try:

			cols   = ",".join([ '`'+i+'`' for i in data.keys()])
			values = str(tuple(data.values()))


			self.cur.execute("INSERT INTO %s (%s) VALUES %s"%(table,cols,values))
			self.sql.commit()

			return True
		except Exception as err :
			return err


	def delete(self,table:str,where:str)->bool:
		# DELETE FROM `post` WHERE `post`.`postID` = 8
		try:

			self.cur.execute("DELETE FROM `%s` WHERE %s "%(table,where))
			self.sql.commit()

			return True

		except Exception as err :
			return err

	# Bool if Seccussfly
	def update(self,table:str,data:dict,where:str)->bool:
		# UPDATE `post` SET `postID` = '1' WHERE `post`.`postID` = 11;
		try:

			cols = ['`%s` ="%s"'%(v,k) for v,k in data.items()]
			cols = ','.join(cols)

			self.cur.execute("UPDATE `%s` SET %s WHERE %s"%(table,cols,where))
			self.sql.commit()
			return True

		except Exception as err :
			return err
