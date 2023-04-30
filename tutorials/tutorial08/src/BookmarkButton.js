import React from 'react';
import {getHeaders} from './utils';

export default function BookmarkButton({actualBookmark, post, token, requeryPost}) {

    const bookmarkId = post.current_user_bookmark_id;
    const postId = post.id;

    async function bookmarkUnbookmark() {
        if (bookmarkId) {
            const response = await fetch(`/api/bookmarks/${bookmarkId}`, {
                method: "DELETE",
                headers: getHeaders(token)
            });
            const data = await response.json();
            console.log(data);
            requeryPost();
        } else {
            console.log('bookmark!')
            const postData = {
                "post_id": postId
            };
            const response = await fetch("/api/bookmarks/", {
                method: "POST",
                headers: getHeaders(token),
                body: JSON.stringify(postData)
            });
            const data = await response.json();
            console.log(data);
            requeryPost();
        }
    }

    // return some JSX:
    return (
    actualBookmark ? 
    <button class="icon-button" aria-label="Bookmark Button" onClick={bookmarkUnbookmark} aria-checked="true">
        <i class="fa-solid fa-bookmark"></i>
    </button>
    :
    <button class="icon-button" aria-label="Bookmark Button" onClick={bookmarkUnbookmark} aria-checked="false">
        <i class="fa-regular fa-bookmark"></i>
    </button>
    );
}