from flask import Response, request
from flask_restful import Resource
from models import LikePost, db
import json

from views import can_view_post
import flask_jwt_extended


class PostLikesListEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user
    
    @flask_jwt_extended.jwt_required()
    def post(self):

        body = request.get_json()
        print(body)
        if not body['post_id']:
            return Response(json.dumps({'error': 'post_id required'}), status=400)
        try:
            body['post_id'] = int(body['post_id'])
        except:
            return Response(json.dumps({'error': 'post_id must be an integer'}), status=400)

        if not can_view_post(user=self.current_user, post_id=body['post_id']):
            return Response(json.dumps({'error': 'You cannot like this post'}), status=404)

        like_post = LikePost(
            post_id=body['post_id'],
            user_id=self.current_user.id
        )
        try:
            db.session.add(like_post)  
            db.session.commit()
        except:
            return Response(json.dumps({'error': 'Error creating like'}), status=400)
        return Response(json.dumps(like_post.to_dict()), mimetype="application/json", status=201)

class PostLikesDetailEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user
    
    @flask_jwt_extended.jwt_required()
    def delete(self, id):

        print(id)
        like_post = LikePost.query.get(id)
        if like_post is None:
            return Response(json.dumps({'error': 'Not Found'}), status=404)
        if self.current_user.id != like_post.user_id:
            return Response(json.dumps({'error': 'You cannot delete this like'}), status=404)
        LikePost.query.filter_by(id=id).delete()
        db.session.commit()
        return Response(json.dumps({"message": "OK"}), mimetype="application/json", status=200)



def initialize_routes(api):
    api.add_resource(
        PostLikesListEndpoint, 
        '/api/posts/likes', 
        '/api/posts/likes/', 
        resource_class_kwargs={'current_user': flask_jwt_extended.current_user}
    )

    api.add_resource(
        PostLikesDetailEndpoint, 
        '/api/posts/likes/<int:id>', 
        '/api/posts/likes/<int:id>/',
        resource_class_kwargs={'current_user': flask_jwt_extended.current_user}
    )
