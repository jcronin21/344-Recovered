from flask import Response, request
from flask_restful import Resource
from models import Following, User, db
import json
import flask_jwt_extended


def get_path():
    return request.host_url + 'api/posts/'

class FollowingListEndpoint(Resource):
    def __init__(self, current_user):
        self.current_user = current_user
    
    @flask_jwt_extended.jwt_required()
    def get(self):
        # return all of the "following" records that the current user is following
        
        followings = Following.query.filter_by(user_id=self.current_user.id).all()

        return Response(json.dumps([]), mimetype="application/json", status=200)


    @flask_jwt_extended.jwt_required()
    def post(self):
        # create a new "following" record based on the data posted in the body 
        body = request.get_json()
        print(body)
        try:
            following_id = int(body.get('user_id'))
        except:
            return Response(json.dumps({'error': 'user_id format incorrect'}), status=400) 
        
        user = User.query.get(following_id)
    
        if user == None:
            return Response(json.dumps({ "error": "user_id not valid" }), mimetype="application/json", status=404)

        following = Following(
            user_id=self.current_user.id,
            following_id=body.get('user_id')
        )
        try:
            db.session.add(following)
            db.session.commit()
        except:
            return Response(json.dumps({ "error": "duplicate user_id" }), mimetype="application/json", status=400)
    
        return Response(json.dumps(following.to_dict_following()), mimetype="application/json", status=201)    

class FollowingDetailEndpoint(Resource):
    def __init__(self, current_user):
        self.current_user = current_user
    
    @flask_jwt_extended.jwt_required()
    def delete(self, id):

        
        print(id)

        following = Following.query.get(id)
    
        if following == None or following.user_id != self.current_user.id:
            return Response(json.dumps({ "error": "follow_user_id not valid or is unauthorized" }), mimetype="application/json", status=404)

        Following.query.filter_by(id=id).delete()
        db.session.commit()

        return Response(json.dumps(None), mimetype="application/json", status=200)




def initialize_routes(api):
    api.add_resource(
        FollowingListEndpoint, 
        '/api/following', 
        '/api/following/', 
        resource_class_kwargs={'current_user': flask_jwt_extended.current_user}
    )
    api.add_resource(
        FollowingDetailEndpoint, 
        '/api/following/<int:id>', 
        '/api/following/<int:id>/', 
        resource_class_kwargs={'current_user': flask_jwt_extended.current_user})