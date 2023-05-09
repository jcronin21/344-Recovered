import React from 'react';
import {getHeaders} from './utils';

export default function BookmarkButton({ post, token, requeryPost }) {

    const bookmarkId = post.current_user_bookmark_id;
    const postId = post.id;

    async function bookmarkUnbook() {
        console.log(bookmarkId, postId);
        if (bookmarkId) {
            console.log('unbookmark!')
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

    return (
        <button onClick={bookmarkUnbook}>
            {bookmarkId ? 'Unbookmark' : 'Bookmark'}
        </button>
    );
}
