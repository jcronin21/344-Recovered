from flask import Response, request
from flask_restful import Resource
import json
from models import db, Comment, Post, Following
import flask_jwt_extended


def get_list_of_user_ids_in_my_network(user_id):
        following = Following.query.filter_by(user_id=user_id).all()
        me_and_my_friend_ids = [rec.following_id for rec in following]
        me_and_my_friend_ids.append(user_id)
        return me_and_my_friend_ids

class CommentListEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user
    
    @flask_jwt_extended.jwt_required()
    def post(self):

        body = request.get_json()
        if not body.get('text'):
            return Response(json.dumps({'error': 'retry'}), status=400)
        try :
            postID = int(body.get('post_id'))
            post = Post.query.get(postID)
            me_and_my_friend_ids = get_list_of_user_ids_in_my_network(self.current_user.id)
            if post is None or post.user_id not in me_and_my_friend_ids :
                error_message = {
                    'error': 'not found'.format(postID)
                }
                return Response(json.dumps(error_message), mimetype="application/json", status=404)
            else :
                print(body)
                new_comment = Comment(
                    text=body.get('text'),
                    post_id=body.get('post_id'),
                    user_id=self.current_user.id
                )
                db.session.add(new_comment)                
                db.session.commit()
                return Response(json.dumps(new_comment.to_dict()), mimetype="application/json", status=201)
        except :
                return Response(json.dumps({'error': 'retry'}), status=400)

        
class CommentDetailEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user
  
    @flask_jwt_extended.jwt_required()
    def delete(self, id):

        try :
            commentID = int(id)
            comment = Comment.query.get(id)
            me_and_my_friend_ids = get_list_of_user_ids_in_my_network(self.current_user.id)
            if comment is None or comment.user_id not in me_and_my_friend_ids :
                error_message = {
                    'error': 'retry'.format(id)
                }
                return Response(json.dumps(error_message), mimetype="application/json", status=404)
            else :
                Comment.query.filter_by(id=id).delete()
                db.session.commit()
                return Response(json.dumps({}), mimetype="application/json", status=200)
        except :
            error_message = {
                'error': 'retry'.format(id)
            }
            return Response(json.dumps(error_message), mimetype="application/json", status=404)


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
        resource_class_kwargs={'current_user': flask_jwt_extended.current_user}
    )