from  flask.views import MethodView
from  flask       import request,jsonify,abort
from .decorator   import Required


class API(MethodView):
	
	decorators = [Required]


	# Select 
	def get(self,sql:object,tb:str,limit:int)->dict:
		try:
			return jsonify(sql.select(tb,limit=limit))
		except Exception as err:
			return jsonify({"Error":'%s'%err}),404

	# Insert 
	def post(self,sql:object,tb:str)->dict:
		dbjson = request.json
		try:
			if dbjson != None:
				# sql.insert(tb,{
				# 	'title':dbjson['data']['title'],
				# 	"post" :dbjson['data']['post' ],
				# 	'keys' :dbjson['data']['keys' ],
				# 	'date' :dbjson['data']['date' ]
				# })
				error = sql.insert(tb,dbjson['data'])
				if error:
					return jsonify({"Error":'Insert To  %s'%error}),404

				return jsonify({"Seccussfly":'Insert To  %s'%tb}),200

		except KeyError as err:
			return jsonify({"Error":'Miss Key %s'%err}),404

		return jsonify({"Error":'No Json Request '}),404

	# UPDATE 
	def put(self,sql:object,tb:str)->dict:
		dbjson = request.json
		try:
			if dbjson != None:
				sql.update(tb,dbjson['data'],dbjson['where'])

				return jsonify({"Seccussfly":'update %s'%tb}),200

		except KeyError as err:
			return jsonify({"Error":'Miss Key %s'%err}),404

		return jsonify({"Error":'No Json Request '}),404

	# DELETE 
	def delete(self,sql:object,tb:str)->dict:
		dbjson = request.json
		try:
			if dbjson != None:

				error = sql.delete(tb,dbjson['where'])
				
				if error:
					return jsonify({"Error":'%s'%error}),404

				return jsonify({"Seccussfly":'delete From %s where %s'%(tb,dbjson['where'])}),200

		except KeyError as err:
			return jsonify({"Error":'Miss Key %s'%err}),404


		return jsonify({"Error":'No Json Request '}),404

	# SELECT **cols
	def view(self,sql:object,tb:str)->dict:

		dbjson = request.json

		try:
			if dbjson != None:
				db = sql.select(tb,dbjson['cols'],dbjson['where'],
					limit =dbjson['limit'] if dbjson.get('limit') else 100 
				)

				return jsonify(db)

		except KeyError as err:
			return jsonify({"Error":'Miss Key %s'%err}),404

		except Exception as err:
			return jsonify({"Error":'%s'%err}),404


		return jsonify({"Error":'Error In Json Request '}),404
