from flask import request, \
    make_response, render_template, redirect
from models import User
import flask_jwt_extended
# from datetime import datetime
import datetime

def logout():
    # # Uncomment these lines to delete the cookies and
    # # redirect the user to the login screen
    
     response = make_response(redirect('/login', 302))
     flask_jwt_extended.unset_jwt_cookies(response)
     return response
    # return 'TODO: Logout'

def login():
    if request.method == 'POST':
        print(request.form)
        username = request.form.get('username')
        password = request.form.get('password')
        # authorized = False

        user = User.query.filter_by(username=username).one_or_none()

        if user is None:
            return render_template(
                'login.html',
                message = 'username not in database'
            )
            # error_message = 'Username not in database'

        if user and not user.check_password(password):
            return render_template(
                'login.html',
                message = 'password not in database'
            )
            # error_message = 'password not in database'

        expires = datetime.timedelta(minutes=20)

        access_token = flask_jwt_extended.create_access_token(
            identity=user.id,
            expires_delta=expires
        )

        response = make_response(redirect('/',302))

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