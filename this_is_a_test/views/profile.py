from flask import Response, request
from flask_restful import Resource
import json
import flask_jwt_extended
from models import User


@flask_jwt_extended.jwt_required()
def get_path():
    return request.host_url + 'api/posts/'


class ProfileDetailEndpoint(Resource):

    @flask_jwt_extended.jwt_required()
    def __init__(self, current_user):
        self.current_user = current_user
        self.profile = User.query.filter_by(id=self.current_user.id).first()

    @flask_jwt_extended.jwt_required()
    def get(self):
        if self.profile is None:
            return Response(json.dumps({"message": "User not found"}), mimetype="application/json", status=404)
        elif self.profile.id != self.current_user.id:
            return Response(json.dumps({"message": "Forbidden"}), mimetype="application/json", status=404)
        return Response(json.dumps(self.profile.to_dict()), mimetype="application/json", status=200)


def initialize_routes(api):
    api.add_resource(
        ProfileDetailEndpoint,
        '/api/profile',
        '/api/profile/',
        resource_class_kwargs={'current_user': flask_jwt_extended.current_user}
    )
