import jwt 
from  flask  import request,jsonify,abort
from .model import MySQL 
from  application import app 

class Required:
	sql = None


	def __init__(self,*args:tuple):
		self.args = args

	def __call__(self,**kw:dict):

		tken = request.headers.get('API-TOKEN')
		if not tken :
			return jsonify({'ERROR':'mis API-TOKEN '}) , 404

		try:
			detk = jwt.decode(tken,app.config['SECRET_KEY'])

			kw.update({'sql':MySQL(user=detk['user'],db=detk['db_user'],password=detk['pass'])})

		except jwt.ExpiredSignatureError as err:
			return jsonify({'ERROR':str(err)})

		except Exception as err:
			return jsonify({'ERROR':err})


		return self.args[0](**kw)
