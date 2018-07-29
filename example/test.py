import requests as req 
import json 
import hashlib as hl,uuid ,binascii



class DBTAPI(object):
	"""docstring for DBTAPI"""
	def __init__(self,token):
		self.url     = 'http://127.0.0.1:8000/api/' 
		self.session = req.Session()
		self.session.headers.update({'API-TOKEN':token})

		# print(dir(self.session))

	def select(self,table:str,limit:int=100):
		get = self.session.get(self.url+"%s/%s"%(table,limit))

		return get

	def selectBy(self,tb:str,dt:str='1=1'):

		get = self.session.request('view',self.url+"%s"%tb,json=dt)

		return get
		
	def insert(self,tb:str,dt:dict):
		# 
		post = self.session.post(self.url+"%s"%tb,json=dt)


		return post


	def delete(self,tb:str,dt:str):
		delete = self.session.delete(self.url+"%s"%tb,json=dt)


		return delete
	def update(self,tb:str,dt:dict):
		# 
		put = self.session.put(self.url+"%s"%tb,json=dt)

		return put

		
token = "Your_Token"
db = DBTAPI(token)

