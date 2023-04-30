from flask import Response, request
from flask_restful import Resource
import json
from models import db, Comment, Post
import flask_jwt_extended

class CommentListEndpoint(Resource):

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

        if post == None or post.user_id not in authorized_ids:
            return Response(json.dumps({ "error": "post_id not valid or is unauthorized" }), mimetype="application/json", status=404)
        
        if not body.get('text'):
            return Response(json.dumps({ "error": "missing text" }), mimetype="application/json", status=400)

        new_comment = Comment(
            text=body.get('text'),
            user_id=self.current_user.id,
            post_id=body.get('post_id'),
        )
        db.session.add(new_comment)
        db.session.commit()

        return Response(json.dumps(new_comment.to_dict()), mimetype="application/json", status=201)
        
class CommentDetailEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user

   
  
    @flask_jwt_extended.jwt_required()
    def delete(self, id):

        print(id)

        try:
            id = int(id)
        except:
            return Response(json.dumps({'error': 'comment_id format incorrect'}), status=404)

        comment = Comment.query.get(id)

        if comment == None or comment.user_id != self.current_user.id:
            return Response(json.dumps({ "error": "comment not valid or is unauthorized" }), mimetype="application/json", status=404)

        Comment.query.filter_by(id=id).delete()


        db.session.commit()

        return Response(json.dumps(None), mimetype="application/json", status=200)


def initialize_routes(api):
    api.add_resource(
        CommentListEndpoint, 
        '/api/comments', 
        '/api/comments/',
        resource_class_kwargs={'current_user': flask_jwt_extended.current_user}

    )
    api.add_resource(
        CommentDetailEndpoint, 
        '/api/comments/<int:id>', 
        '/api/comments/<int:id>/',
        resource_class_kwargs={'current_user': flask_jwt_extended.current_user})