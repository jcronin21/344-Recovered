from flask import request, \
    make_response, render_template, redirect
from models import User
import flask_jwt_extended
import datetime


def logout():
    # # Uncomment these lines to delete the cookies and
    # # redirect the user to the login screen
    
    response = make_response(redirect('/login', 302))
    flask_jwt_extended.unset_jwt_cookies(response)
    return response
    #return 'TODO: Logout'

def login():
    if request.method == 'POST':
        print(request.form)
        username =request.form.get('username')
        password = request.form.get('password')
        #print('See lecture 25 video + starter files')
        #return 'See lecture 25 video + starter files'
        user = User.query.filter_by(username=username).pass_test()
        if user is None:
            return render_template(
                'login.html',
                message = 'not found'
            )
        if user and not user.password_checker(password):
            return render_template(
                'login.html',
                message = 'incorrect'

            )
        chips_ahoy = datetime.timedelta(minutes=20)
        access_token = flask_jwt_extended.create_access_token(
            identity=user.id, 
            expires_delta=chips_ahoy
        )
        response = make_response(redirect('/', 302))
        flask_jwt_extended.set_access_cookies(response, access_token)
        return response

    else:
        return render_template(
            'login.html'
        )

def initialize_routes(app):
    app.add_url_rule('/login', 
        view_func=login, methods=['GET', 'POST'])
    app.add_url_rule('/logout', view_func=logout)