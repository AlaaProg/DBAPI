from flask  import Blueprint
from .views import index,creatUser,loginUser

app = Blueprint('APP',__name__,template_folder='templates')



app.add_url_rule("/",'index',index,methods={'GET','POST'})
app.add_url_rule("/cuser",'cuser',creatUser,methods={'GET','POST'})
app.add_url_rule("/luser",'luser',loginUser,methods={'GET','POST'})
