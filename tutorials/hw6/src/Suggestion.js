import React from 'react';
import {getHeaders} from './utils';
import { useState } from "react";

export default function Suggestion({user,token}) {
   
    const [followingId, setFollowingId] = useState(null);

    function toggleFollow() {
        followingId ? unfollow() : follow();
    }

    async function follow() {
        const response = await fetch('/api/following', {
            headers: getHeaders(token),
            method: 'POST',
            body: JSON.stringify({ user_id: user.id })
        })
        const data = await response.json();
        setFollowingId(data.id);
    }

    async function unfollow() {
        const response = await fetch(`/api/following/${followingId}`, {
            headers: getHeaders(token),
            method: 'DELETE'
        });
        await response.json();
        setFollowingId(null);
    }
   
    if (!user) {
        return '';
    }
    return (
        <section id={ 'suggestion-' + user.id }>
            <img src={ user.thumb_url }
                className="pic" alt={ 'Profile pic for ' + user.username } />
            <div>
                <p>{ user.username }</p>
                <p>suggested for you</p>
            </div>
            <div>
                <button role="switch"
                    className={followingId ? 'link following active' : 'link following'}
                    aria-checked="false"
                    aria-label={ 'Follow ' + user.username }
                    onClick={toggleFollow}
                    >{followingId ? 'unfollow' : 'follow'}</button>
            </div>
        </section>
    );    
}
