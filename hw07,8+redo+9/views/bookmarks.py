from flask import Response, request
from flask_restful import Resource
from models import Bookmark, Post, Following, db
import json
import flask_jwt_extended

def get_list_of_user_ids_in_my_network(user_id):
        following = Following.query.filter_by(user_id=user_id).all()
        me_and_my_friend_ids = [rec.following_id for rec in following]
        me_and_my_friend_ids.append(user_id)
        return me_and_my_friend_ids

class BookmarksListEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user
    
    @flask_jwt_extended.jwt_required()
    def get(self):

        bookmarks = Bookmark.query.filter_by(user_id=self.current_user.id).all()
        return Response(json.dumps([bookmark.to_dict() for bookmark in bookmarks]), mimetype="application/json", status=200)

    @flask_jwt_extended.jwt_required()
    def post(self):

        body = request.get_json()
        if not body.get('post_id'):
            return Response(json.dumps({'error': 'required'}), status=400)
        if str(body.get('post_id')).isdigit() == False :
            return Response(json.dumps({'error': 'not found'}), mimetype="application/json", status=400)
        all_your_bookmarks = Bookmark.query.filter_by(user_id=self.current_user.id).all()
        bookmarks = [bookmark.post_id for bookmark in all_your_bookmarks]
        me_and_my_friend_ids = get_list_of_user_ids_in_my_network(self.current_user.id)
        if body.get('post_id') in bookmarks :
            return Response(json.dumps({'error': 'not found'}), mimetype="application/json", status=400)
        if Post.query.get(body.get('post_id')) is None or Post.query.get(body.get('post_id')).user_id not in me_and_my_friend_ids :
            return Response(json.dumps({'error': 'not found'}), mimetype="application/json", status=404)
        new_bookmark = Bookmark(
            post_id=body.get('post_id'),
            user_id=self.current_user.id
        )
        db.session.add(new_bookmark)                
        db.session.commit()
        return Response(json.dumps(new_bookmark.to_dict()), mimetype="application/json", status=201)

class BookmarkDetailEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user
    
    @flask_jwt_extended.jwt_required()
    def delete(self, id):

        print(id)
        try :
            bookmarkID=int(id)
            bookmark = Bookmark.query.get(id)
            me_and_my_friend_ids = get_list_of_user_ids_in_my_network(self.current_user.id)
            if bookmark is None or bookmark.user_id not in me_and_my_friend_ids :
                error_message = {
                    'error': 'not found.'.format(id)
                }
                return Response(json.dumps(error_message), mimetype="application/json", status=404)
            else :
                Bookmark.query.filter_by(id=id).delete()
                db.session.commit()
                return Response(json.dumps({}), mimetype="application/json", status=200)
        except :
            error_message = {
                'error': 'not found.'.format(id)
            }
            return Response(json.dumps(error_message), mimetype="application/json", status=404)

def initialize_routes(api):
    api.add_resource(
        BookmarksListEndpoint, 
        '/api/bookmarks', 
        '/api/bookmarks/', 
        resource_class_kwargs={'current_user': flask_jwt_extended.current_user}
    )

    api.add_resource(
        BookmarkDetailEndpoint, 
        '/api/bookmarks/<int:id>', 
        '/api/bookmarks/<int:id>',
        resource_class_kwargs={'current_user': flask_jwt_extended.current_user}
    )