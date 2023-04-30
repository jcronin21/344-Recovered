from flask import Response, request
from flask_restful import Resource
from models import Post, Following, db
from views import get_authorized_user_ids
import access_utils
import flask_jwt_extended

import json

def get_path():
    return request.host_url + 'api/posts/'

class PostListEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user

    def get(self):
        me_and_my_friend_ids = access_utils.get_list_of_user_ids_in_my_network(self.current_user.id)
        try:
            limit = request.args.get('limit') or 20
            limit = int(limit)
        except:
            return Response(
                json.dumps({'error': 'No string for limit.'}), status=400
            )
        if limit > 50:
            return Response(
                json.dumps({'error': 'Bad data. Limit cannot exceed 20.'}), status=400
            )
        posts = Post.query.filter(Post.user_id.in_(me_and_my_friend_ids)).limit(limit)
        return Response(json.dumps([post.to_dict() for post in posts]), mimetype="application/json", status=200)

    def post(self):
        # request.get_json() is holding the data that the user
        # just sent over the network. Stored as a python dictionary
        body = request.get_json()
        if not body.get('image_url'):
            return Response(json.dumps({'error': 'image_url required'}), status=400)

        # convert the data that the user sent over HTTP to a SQLAlchemy object
        new_post = Post(
            image_url=body.get('image_url'),
            user_id=self.current_user.id, # must be a valid user_id or will throw an error
            caption=body.get('caption'),
            alt_text=body.get('alt_text')
        )
        # save it to the database
        db.session.add(new_post)    # issues the insert statement
        db.session.commit()  

        # send the new data object to the user
        return Response(json.dumps(new_post.to_dict()), mimetype="application/json", status=201)

    
#user doesnt specify a limit: 20
# user specifies a valid int <= 50:
#    that number
#user gives you abc -> 400 error
# user gives you a limi 51 -> 400 error
class PostEndpoint(Resource):
    def __init__(self, current_user):
        self.current_user = current_user
    def patch(self,id):
        post = Post.query.get(id)
        if not post:
            return Response(json.dumps({'error': 'Post not found'}), status = 404)
        if post.user_id!=self.current_user.id:
            return Response(json.dumps({'error': 'exit'}), status = 401)
        body = request.get_json()
        if body.get('image_url'):
            post.image_url = body.get('image_url')
        if body.get('caption'):
            post.caption = body.get('caption')
        if body.get('alt_text'):
            post.alt_text = body.get('alt_text')

        db.session.commit()

        return Response(json.dumps(post.to_dict()), mimetype ="application/json", status = 200)
    def delete(self,id):

        post = Post.query.get(id)
        if not post:
            return Response(json.dumps({'error': 'Post not found'}), status = 404)
        if post.user_id != self.current_user.id:
            return Response(json.dumps({'erorr:' 'none'}), status=401)
        
        db.session.delete(post)
    def get(self):
        limit = request.args.get('limit')
        # get posts created by one of these users:
        #1 get all of the user ids of the ppl that the user 12 is following 
        following = Following.query.filter_by(user_id=self.current_user.id).all()
        friend_ids = []
        #building a list of friend usernames
        for rec in following:
            friend_ids.append(rec.following_id)
        friend_ids.append(self.current_user.id)
        print(friend_ids)
        try:
            limit = (request.args.get('limit')) or 20
            limit = int(limit)
        except:
            return Response(
                json.dumps({'error': 'no string fro limit.'}), status=400
            )
        if limit > 50:
            return Response(
                json.dumps({'error': 'Bad data. Limit cannot exceed 20.'}), status =400
            )
        #posts = Post.query.filter_by(user_id = self.current_user.id).all()
        posts = Post.query.filter(Post.user_id.in_(friend_ids)).limit(limit)
        return Response(json.dumps([post.to_dict() for post in posts]), mimetype="application/json", status=200)

    def post(self):
        # create a new post based on the data posted in the body 
        data = request.get_json()
        if not data or 'image_url' not in data:
            error_message={'error': 'Missing required field: image_url'}
            return Response(json.dumps(error_message), status=400)
        post = Post(
            user_id= self.current_user.id,
            image_url=data['image_url'],
            caption=data.get('caption'),
            alt_text=data.get('alt_text'),
        )
        db.session.add(post)

        response_data = {'id':post.id, 'url': get_path()+str(post.id)}

        # body = request.get_json()
        # print(body)  
        return Response(json.dumps({}), mimetype="application/json", status=200)

        
class PostDetailEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user
        
    @access_utils.can_modify_or_404
    def patch(self, id):
        # update post based on the data posted in the body 
        body = request.get_json()
        post=Post.query.get(id)

        if body.get('image_url'):
            post.image_url = body.get('image_url')
        if body.get('caption'):
            post.caption =body.get('caption')
        if body.get('alt_text'):
            post.alt_text = body.get('alt_text')

            db.session.commit()      
        return Response(json.dumps(post.to_dict()), mimetype="application/json", status=200)

    @access_utils.can_modify_or_404
    def delete(self, id):
        # delete post where "id"=id
        Post.query.filter_by(id=id).delete()
        db.session.commit()
        return Response(json.dumps(None), mimetype="application/json",status=200)
    

    @access_utils.can_view_or_404
    def get(self, id):
        # get the post based on the id
        post = Post.query.get(id)
        if post is None:
            error_message ={
                'error': ' post {0} does not exist.'.format(id)
            }
            return Response(json.dumps(error_message), mimetype="application/json",status=404)
        else:
         return Response(json.dumps(post.to_dict()), mimetype="application/json", status=200)

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