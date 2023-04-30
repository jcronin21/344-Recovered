from flask import Response, request
from flask_restful import Resource
from models import User
from views import get_authorized_user_ids
import json
import flask_jwt_extended


class SuggestionsListEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user
    

    @flask_jwt_extended.jwt_required()
    def get(self):
        # suggestions should be any user with an ID that's not in this list:
        # print(get_authorized_user_ids(self.current_user))
        #return Response(json.dumps([]), mimetype="application/json", status=200)

        suggested = User.query.filter(~User.id.in_(get_authorized_user_ids(self.current_user))).limit(7).all()


        return Response(json.dumps([suggestion.to_dict() for suggestion in suggested]), mimetype="application/json", status=200)


def initialize_routes(api):
    api.add_resource(
        SuggestionsListEndpoint, 
        '/api/suggestions', 
        '/api/suggestions/', 
        resource_class_kwargs={'current_user': api.app.current_user}
    )
