#IMPORT Libs
from flask  import Blueprint
from .views  import API


# API
api = Blueprint("API",__name__)



# VIEW 
api_view = API.as_view('API')

# METHOD VIEW POST PUT GET DELETE PATCH COPY HEAD OPTIONS LINK UNLINK
# URL 
api.add_url_rule("/<string:tb>/<int:limit>",view_func=api_view,methods={"GET"})
api.add_url_rule("/<string:tb>",view_func=api_view,methods={'VIEW','PUT','POST','DELETE'})