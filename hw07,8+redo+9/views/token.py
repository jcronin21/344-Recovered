from models import User
import flask_jwt_extended
from flask import Response, request
from flask_restful import Resource
import json
from datetime import timezone, datetime, timedelta

class AccessTokenEndpoint(Resource):
    # Your Job:
    # Create a route to authenticate your users and return JWT Token. The
    # create_access_token() function is used to actually generate the JWT.
    def post(self):
        body = request.get_json() or {}
        username = body.get('username')
        password = body.get('password')
        user=User.query.filter_by(username=username).one_or_none()
        if user is None :
            return Response(
                json.dumps({
                    'message': 'retry'
                }),
                status=401
            )
        print(body)
        if user.check_password(password) :
            return Response(
                json.dumps({
                    'access_token': flask_jwt_extended.create_access_token(identity=user.id),
                    'refresh_token': flask_jwt_extended.create_refresh_token(identity=user.id)
                }),
                status=200
            )
        else :
            return Response(
                json.dumps({
                    'message': 'retry'
                }),
                status=401
            )
       

class RefreshTokenEndpoint(Resource):
    # done for you :). 
    def post(self):
        body = request.get_json() or {}
        refresh_token = body.get('refresh_token')
        if not refresh_token:
            return Response(json.dumps({ 
                    "message": "retry"
                }), mimetype="application/json", status=400)
        try:
            decoded_token = flask_jwt_extended.decode_token(refresh_token)
            exp_timestamp = decoded_token.get("exp")
            now = datetime.timestamp(datetime.now(timezone.utc))
        except:
            return Response(json.dumps({ 
                "message": "retry".format(refresh_token)
            }), mimetype="application/json", status=401)

        
        if exp_timestamp > now:
            identity = decoded_token.get('sub')
            access_token = flask_jwt_extended.create_access_token(identity=identity)
            return Response(json.dumps({ 
                    "access_token": access_token, 
                    "refresh_token": refresh_token
                }), mimetype="application/json", status=200)
        else:
            return Response(json.dumps({ 
                    "message": "retry"
                }), mimetype="application/json", status=401)

def initialize_routes(api):
    api.add_resource(
        AccessTokenEndpoint, 
        '/api/token', '/api/token/'
    )

    api.add_resource(
        RefreshTokenEndpoint, 
        '/api/token/refresh', '/api/token/refresh/'
    )