from crypt import methods
from flask import Flask , make_response, jsonify,render_template
from requests import request, session
import jwt
from datetime import datetime,timedelta
from functools import wraps
from framework.flask.db_wrapper import authenticate


app = Flask(__name__)
app.config['SECRET_KEY']='f20153e3a2bb468d9de3fe8df7430202'

def token_required(fn):
    @wraps(fn)
    def decorated_fn(*args,**kwargs) :
        token = request.args.get('token')
        if not token:
            return jsonify({'Alert':'Token is missing'})
        try:
            payload = jwt.decode(token,app.config['SECRET_KEY'])    
        except:
            return jsonify({'Alert':'Invalid Token'})
    return decorated_fn


@app.route('/')
def home():
    if not session['logged in']:
        return render_template('login.html')
    else:
        return 'logged in currently'        

@app.route('/login',methods=['POST'])
def login():
    username = request.form.get('username')
    passd = request.form.get('password')
    if authenticate(username,passd):
        session['logged_in']=True
        token = jwt.encode({
            'user':username,
            'expiration':datetime.utcnow()+timedelta(seconds=120)
        },
        app.config['SECRET_KEY']
        )
        return jsonify({'token':token.decode('utf-8')})

    else:
        return make_response('Unable to verify',403,{'WWW-Authenticate':'Basic Realm'})