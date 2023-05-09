from flask import Response, request
from flask_restful import Resource
from models import Post, db, Following
from views import get_authorized_user_ids, can_view_post

import json


def get_path():
    return request.host_url + 'api/posts/'


class PostListEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user
        self.user_ids = get_authorized_user_ids(self.current_user)

    def get(self):
      
        posts = Post.query.filter(Post.user_id.in_(self.user_ids))

        try:
            limit = int(request.args.get('limit', 20))
        except ValueError:
            return Response(json.dumps({"message": "Invalid limit parameter"}), mimetype="application/json", status=400)

        if limit > 50:
            return Response(json.dumps({"message": "Invalid limit parameter"}), mimetype="application/json", status=400)
        posts = posts.limit(limit)

        return Response(json.dumps([post.to_dict() for post in posts]), mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        if not body.get('image_url'):
            return Response(json.dumps({'error': 'image_url required'}), status=400)

        new_post = Post(
            image_url=body.get('image_url'),
            user_id=self.current_user.id,  
            caption=body.get('caption'),
            alt_text=body.get('alt_text')
        )
        db.session.add(new_post)  
        db.session.commit()

        return Response(json.dumps(new_post.to_dict()), mimetype="application/json", status=201)


class PostDetailEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user

    def patch(self, id):
        body = request.get_json()

        try:
            id = int(id)
        except:
            return Response(json.dumps({"message": "Invalid post id"}), mimetype="application/json", status=400)

        try:
            post = Post.query.get(id)
        except:
            return Response(json.dumps({"message": "Not Found"}), mimetype="application/json", status=404)

        if post is None:
            return Response(json.dumps({"message": "Not Found"}), mimetype="application/json", status=404)
        if body.get('image_url'):
            post.image_url = body.get('image_url')
        if body.get('caption'):
            post.caption = body.get('caption')
        if body.get('alt_text'):
            post.alt_text = body.get('alt_text')

        db.session.commit()

        return Response(json.dumps(post.to_dict()), mimetype="application/json", status=200)

    def delete(self, id):
        try:
            id = int(id)
        except:
            return Response(json.dumps({"message": "Invalid post id"}), mimetype="application/json", status=400)
        try:
            post = Post.query.get(id)
        except:
            return Response(json.dumps({"message": "Not Found"}), mimetype="application/json", status=404)
        if post is None:
            return Response(json.dumps({"message": "Not Found"}), mimetype="application/json", status=404)
        if post.user_id != self.current_user.id:
            return Response(json.dumps({"message": "invalid"}), mimetype="application/json", status=404)
        Post.query.filter_by(id=id).delete()
        db.session.commit()
        return Response(json.dumps({"message": "OK"}), mimetype="application/json", status=200)

    def get(self, id):
        post = Post.query.filter_by(id=id).first()
        if post is None:
            return Response(json.dumps({"message": "Not Found"}), mimetype="application/json", status=404)
        elif can_view_post(user=self.current_user, post_id=post.id):
            return Response(json.dumps(post.to_dict()), mimetype="application/json", status=200)
        else:
            return Response(json.dumps({"message": "invalid"}), mimetype="application/json", status=404)


def initialize_routes(api):
    api.add_resource(
        PostListEndpoint,
        '/api/posts', '/api/posts/',
        resource_class_kwargs={'current_user': api.app.current_user}
    )
    api.add_resource(
        PostDetailEndpoint,
        '/api/posts/<int:id>', '/api/posts/<int:id>/',
        resource_class_kwargs={'current_user': api.app.current_user}
    )
