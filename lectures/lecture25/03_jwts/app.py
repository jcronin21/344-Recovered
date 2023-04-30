#pip3 install flask-jwt-extended
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, make_response, request, redirect, render_template
import flask_jwt_extended
import datetime
import os
app = Flask(__name__)


############
# JWT Code #
############
# from .env file
app.config["JWT_SECRET_KEY"] = os.environ.get('JWT_SECRET')
app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies"]
app.config["JWT_COOKIE_SECURE"] = False
jwt = flask_jwt_extended.JWTManager(app)


@app.route('/')
def home():
    # try:
    #     # check if the access token is valid:
    #     flask_jwt_extended.verify_jwt_in_request()
    # except:
    #     # otherwise, redirect to login screen:
    #     return redirect('/login', 302)
    return render_template(
        'index.html'
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form)
        # # query the DB to make sure the person's email and password
        # # are valid. If so, generate the JWT with the authenticated user's ID:

        # # pretend the DB check was successful, and store the user's ID in a variable.
        # user_id = 12 
        # expires = datetime.timedelta(seconds=10)

        # # generate the token using the Flask JWT Extended library:
        # access_token = flask_jwt_extended.create_access_token(
        #     identity=user_id, 
        #     expires_delta=expires
        # )
        response = make_response(redirect('/', 302))
        # flask_jwt_extended.set_access_cookies(response, access_token)
        return response
    return render_template(
        'login.html'
    )

@app.route('/logout')
def logout():
    response = make_response(redirect('/login', 302))
    flask_jwt_extended.unset_jwt_cookies(response)
    # print('-' * 50)
    # print('access tokens unset')
    # print('-' * 50)
    # print('Cookie (access_token_cookie):', request.cookies.get('access_token_cookie'))
    # print('Cookie (csrf_access_token):', request.cookies.get('csrf_access_token'))
    # print('-' * 50)
    return response



if __name__ == '__main__':
    app.run()
