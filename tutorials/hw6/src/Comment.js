import React from 'react';
import { getHeaders } from './utils';

export default function Comment({ comment, token, requeryPost }) {

  async function handleDeleteComment() {
    const response = await fetch(`/api/comments/${comment.id}`, {
      method: "DELETE",
      headers: getHeaders(token),
    });
    const data = await response.json();
    console.log(data);
    requeryPost();
  }

  return (
    <div className="comment">
      <strong>{comment.user.username}:</strong> {comment.text}
      {comment.user.id === token.user_id &&
        <button onClick={handleDeleteComment}>Delete</button>
      }
    </div>
  );
}
