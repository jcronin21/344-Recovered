from flask import Response, request
from flask_restful import Resource
from models import LikePost, Following, db
import json
import flask_jwt_extended

def get_list_of_user_ids_in_my_network(user_id):
        following = Following.query.filter_by(user_id=user_id).all()
        me_and_my_friend_ids = [rec.following_id for rec in following]
        me_and_my_friend_ids.append(user_id)
        return me_and_my_friend_ids

class PostLikesListEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user

    @flask_jwt_extended.jwt_required()   
    def post(self):

        body = request.get_json()
        all_your_likes = LikePost.query.filter_by(user_id=self.current_user.id).all()
        likes = [like.post_id for like in all_your_likes]
        if body.get('post_id') in likes :
            return Response(json.dumps({'error': 'already liked'}), mimetype="application/json", status=400)
        try :
            likeID = int(body.get('post_id'))
            like = LikePost.query.get(likeID)
            me_and_my_friend_ids = get_list_of_user_ids_in_my_network(self.current_user.id)
            if like is None or like.user_id not in me_and_my_friend_ids :
                error_message = {
                    'error': 'retry'.format(likeID)
                }
                return Response(json.dumps(error_message), mimetype="application/json", status=404)
            new_like = LikePost(
                user_id=self.current_user.id,
                post_id=body.get('post_id')
            )
            db.session.add(new_like)                
            db.session.commit()
            return Response(json.dumps(new_like.to_dict()), mimetype="application/json", status=201)
        except :
            error_message = {
                'error': 'retry'.format(body.get('post_id'))
            }
            return Response(json.dumps(error_message), mimetype="application/json", status=400)

class PostLikesDetailEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user

    @flask_jwt_extended.jwt_required()
    def delete(self, id):

        try :
            postID=int(id)
            like = LikePost.query.get(id)
            me_and_my_friend_ids = get_list_of_user_ids_in_my_network(self.current_user.id)
            if like is None or like.user_id not in me_and_my_friend_ids :
                error_message = {
                    'error': 'retry'.format(id)
                }
                return Response(json.dumps(error_message), mimetype="application/json", status=404)
            else :
                LikePost.query.filter_by(id=id).delete()
                db.session.commit()
                return Response(json.dumps({}), mimetype="application/json", status=200)
        except :
            error_message = {
                'error': 'retry'.format(id)
            }
            return Response(json.dumps(error_message), mimetype="application/json", status=400)

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