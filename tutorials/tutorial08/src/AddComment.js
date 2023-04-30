import React from 'react';
import {getHeaders} from './utils';
import { useState } from "react";

export default function AddComment({token, post, requeryPost}) {

    async function addComment() {
        const commenting = document.querySelector('#addComment' + post.id);
        const response = await fetch('/api/comments/', {
            method: "POST",
            headers: getHeaders(token),
            body: JSON.stringify({
                "post_id": post.id,
                "text": commenting.value
            })
        });
        const data = await response.json();
        console.log(data);
        requeryPost();
        commenting.value = "";
        commenting.focus();
    }

    return (
    <div class="add-comment">
        <div class="input-holder">
            <i class="far fa-smile"></i>
            <input type="text" id={'addComment' + post.id} placeholder="Add a comment..."/>
        </div>
            <button class="button" onClick={addComment}>Post</button>
    </div>
    );
}