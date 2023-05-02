from dotenv import load_dotenv
load_dotenv()
from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS
from flask import render_template
import os
from sqlalchemy import and_
from models import db, Post, User, Following, ApiNavigator, Story
from views import initialize_routes, get_authorized_user_ids
import flask_jwt_extended
from lib.flask_multistatic import MultiStaticFlask as Flask
from flask import send_from_directory


app = Flask(__name__)

app.static_folder = [
    os.path.join(app.root_path, 'react-client', 'build', 'static'),
    os.path.join(app.root_path, 'static')
]

cors = CORS(app,
    resources={r"/api/*": {"origins": '*'}},
    supports_credentials=True 
)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["JWT_SECRET_KEY"] = os.environ.get('JWT_SECRET')
app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies"]
app.config["JWT_COOKIE_SECURE"] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
jwt = flask_jwt_extended.JWTManager(app)


db.init_app(app)
api = Api(app)


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    user_id = jwt_data["sub"]
    return User.query.filter_by(id=user_id).one_or_none()


initialize_routes(api)

@flask_jwt_extended.jwt_required()
@app.route('/')
def home():
 
    return send_from_directory(app.root_path + '/react-client/build', 'index.html')


@flask_jwt_extended.jwt_required()
@app.route('/api')
def api_docs():
    navigator = ApiNavigator(flask_jwt_extended.current_user)
    return render_template(
        'api/api_docs.html', 
        user=flask_jwt_extended.current_user,
        endpoints=navigator.get_endpoints(),
        url_root=request.url_root[0:-1] 
    )



# enables flask app to run using "python3 app.py"
if __name__ == '__main__':
    app.run()