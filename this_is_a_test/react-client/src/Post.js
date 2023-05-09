import React from 'react';
import LikeButton from './LikeButton';
import {getHeaders} from './utils';
import BookmarkButton from './BookmarkButton';
import AddComment from './AddComment';

import { useState } from "react";

export default function Post({post, token}) {

    const [actualPost, setActualPost] = useState(post);

    async function requeryPost() {
        // get a fresh copy of the post
            const response = await fetch(`/api/posts/${post.id}`, {
            method: "GET",
            headers: getHeaders(token)
        });
        const data = await response.json();
        // to make the screen redraw after requerying the post,
        // we need to set a state variable:
        setActualPost(data);
    }
   //make show comment function
//    function showComment(){
//     // if there are comments >0 return other wise none etc etc
//     actualPost.comments
//    }

    // JSX representation of a Post
    return (
        <section className="card">
            <img src={actualPost.image_url} alt={actualPost.caption} />
            <p>{actualPost.caption}</p>
            <div className="buttons">
                <LikeButton 
                    post={actualPost} 
                    token={token} 
                    requeryPost={requeryPost} />
                    
            </div>
            <div className="buttons">
   
                <BookmarkButton 
                    post={actualPost} 
                    token={token} 
                    requeryPost={requeryPost} />
            </div>
            <div className="add-comment-section">
                <AddComment token={token} post={actualPost} requeryPost={requeryPost} />
            </div>
        </section> 
    )  
}
