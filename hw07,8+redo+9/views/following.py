from flask import Response, request
from flask_restful import Resource
from models import Following, User, db
import json
import flask_jwt_extended


def get_path():
    return request.host_url + 'api/posts/'

def get_list_of_user_ids_in_my_network(user_id):
        following = Following.query.filter_by(user_id=user_id).all()
        me_and_my_friend_ids = [rec.following_id for rec in following]
        me_and_my_friend_ids.append(user_id)
        return me_and_my_friend_ids

class FollowingListEndpoint(Resource):
    def __init__(self, current_user):
        self.current_user = current_user
    
    @flask_jwt_extended.jwt_required()
    def get(self):
        # return all of the "following" records that the current user is following
        followings = Following.query.filter_by(user_id=self.current_user.id).all()
        return Response(json.dumps([following.to_dict_following() for following in followings]), mimetype="application/json", status=200)

    @flask_jwt_extended.jwt_required()
    def post(self):
        # create a new "following" record based on the data posted in the body 
        body = request.get_json()
        if not body.get('user_id'):
            return Response(json.dumps({'error': 'retry'}), status=400)
        all_users = Following.query.all()
        all_users_ids = [user.user_id for user in all_users]
        if str(body.get('user_id')).isdigit() == False :
            return Response(json.dumps({'error': 'retry'}), mimetype="application/json", status=400)
        if body.get('user_id') not in all_users_ids :
            return Response(json.dumps({'error': 'retry'}), mimetype="application/json", status=404)
        me_and_my_friend_ids = get_list_of_user_ids_in_my_network(self.current_user.id)
        if body.get('user_id') in me_and_my_friend_ids :
                return Response(json.dumps({'error': 'currently following.'}), mimetype="application/json", status=400)
        new_following = Following(
            user_id=self.current_user.id,
            following_id=body.get('user_id')
        )
        db.session.add(new_following)                
        db.session.commit()
        return Response(json.dumps(new_following.to_dict_following()), mimetype="application/json", status=201)

class FollowingDetailEndpoint(Resource):
    def __init__(self, current_user):
        self.current_user = current_user

    @flask_jwt_extended.jwt_required()
    def delete(self, id):
        # delete "following" record where "id"=id
        try :
            followingID=int(id)
            following=Following.query.get(id)
            me_and_my_friend_ids = get_list_of_user_ids_in_my_network(self.current_user.id)
            if following is None or following.following_id not in me_and_my_friend_ids :
                error_message = {
                    'error': 'retry'.format(id)
                }
                return Response(json.dumps(error_message), mimetype="application/json", status=404)
            else :
                Following.query.filter_by(id=id).delete()
                db.session.commit()
                return Response(json.dumps({}), mimetype="application/json", status=200)
        except :
            error_message = {
                'error': 'retry'.format(id)
            }
            return Response(json.dumps(error_message), mimetype="application/json", status=404)

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
        resource_class_kwargs={'current_user': flask_jwt_extended.current_user}
    )