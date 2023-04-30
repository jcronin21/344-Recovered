from flask import Response, request
from flask_restful import Resource
from models import LikePost, db
import json
import flask_jwt_extended

class PostLikesListEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user
    
    @flask_jwt_extended.jwt_required()
    def post(self):

        body = request.get_json()
        print(body)
        try:
            post_id = int(body.get('post_id'))
        except:
            return Response(json.dumps({'error': 'post_id format incorrect'}), status=400) 

        post = Post.query.get(post_id)
        authorized_ids = get_authorized_user_ids(current_user=self.current_user)

        if post == None:
            return Response(json.dumps({ "error": "post_id not valid" }), mimetype="application/json", status=404)

        if post.user_id not in authorized_ids:
            return Response(json.dumps({ "error": "post_id not valid or is unauthorized" }), mimetype="application/json", status=404)

        like_post = LikePost(
            user_id=self.current_user.id,
            post_id=body.get('post_id')
        )
        try:
            db.session.add(like_post)
            db.session.commit()
        except:
            return Response(json.dumps({ "error": "duplicate post_id" }), mimetype="application/json", status=400)

        return Response(json.dumps(like_post.to_dict()), mimetype="application/json", status=201)

class PostLikesDetailEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user
    
    @flask_jwt_extended.jwt_required()
    def delete(self, id):
  
  
        print(id)

        try:
            id = int(id)
        except:
            return Response(json.dumps({'error': 'like_post_id format incorrect'}), status=404)

        like_post = LikePost.query.get(id)

        if like_post == None or like_post.user_id != self.current_user.id:
            return Response(json.dumps({ "error": "like_post_user_id not valid or is unauthorized" }), mimetype="application/json", status=404)

        LikePost.query.filter_by(id=id).delete()
        db.session.commit()

        return Response(json.dumps(None), mimetype="application/json", status=200)



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
        resource_class_kwargs={'current_user': flask_jwt_extended.current_user})