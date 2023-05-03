// Job of this component is to display a single story

import React from 'react';


export default function Story({story}) {
    return (
        <div>
            <img src={story.user.thumb_url} class="pic"/>
            <p>{story.user.username}</p>
        </div>
    )
}