import React from 'react';
import AddComment from './AddComment';
import LikeButton from './LikeButton';
import BookmarkButton from './BookmarkButton';
import { useState } from "react";
import {getHeaders} from './utils';

export default function Post({model, token}) {  

    const [post, setPost] = useState(model);
    // const isModalShowing, setIsModalShowing = useState(null);

    async function requeryPost() {
        const response = await fetch(`/api/posts/${post.id}`, {
                headers: getHeaders(token)
            });
        const data = await response.json();
        setPost(data);
    }
    
    if (!post) {
        return (
            <div></div>  
        );
    }
    return (
        <section className="card">
            <div className="header">
                <h3>{ post.user.username }</h3>
                <i className="fa fa-dots"></i>
            </div>
            <img 
                src={ post.image_url } 
                alt={'Image posted by ' +  post.user.username } 
                width="300" 
                height="300" />
            <div className="info">
                <div className="buttons">
                    <div>
                        <LikeButton 
                            token={token}
                            postId={post.id} 
                            likeId={post.current_user_like_id}
                            requeryPost={requeryPost} />
                        <i className="far fa-comment"></i>
                        <i className="far fa-paper-plane"></i>
                    </div>
                    <div>
                        <BookmarkButton 
                            token={token}
                            postId={post.id} 
                            bookmarkId={post.current_user_bookmark_id}
                            requeryPost={requeryPost} />
                    </div>
                </div>
                <p className="likes"><strong>{ post.likes.length } { post.likes.length === 1 ? 'like' : 'likes' }</strong></p>
                <div className="caption">
                    <p>
                        <strong>{ post.user.username }</strong> 
                        { post.caption }
                    </p>
                    <p className="timestamp">{ post.display_time }</p>
                </div>
                
            </div>
            
            <AddComment token={token} requeryPost={requeryPost} postId={post.id} />
        </section> 
    );     
}

