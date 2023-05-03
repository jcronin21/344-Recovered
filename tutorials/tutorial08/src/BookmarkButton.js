import React from 'react';
import {getHeaders} from './utils';

export default function BookmarkButton({postId, bookmarkId, requeryPost, token}) {  

    function toggleBookmark(ev) {
        bookmarkId ? unbookmark() : bookmark();
    }

    function bookmark() {
        fetch('/api/bookmarks', {
                headers: getHeaders(token),
                method: 'POST',
                body: JSON.stringify({ post_id: postId })
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                requeryPost();
            })
    }

    function unbookmark() {
        fetch(`/api/bookmarks/${bookmarkId}`, {
                headers: getHeaders(token),
                method: 'DELETE'
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                requeryPost();
            })
    }

    return (
        <button role="switch"
            className="bookmark" 
            aria-label="Bookmark Button" 
            aria-checked={bookmarkId ? 'true' : 'false'}
            onClick={toggleBookmark}>
            <i className={bookmarkId ? 'fas fa-bookmark' : 'far fa-bookmark'}></i>
        </button>
    ) 
}
