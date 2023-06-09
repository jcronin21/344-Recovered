// import React from 'react';
// import {getHeaders} from './utils';
// import { useState } from "react";

// export default function AddComment({token, post, requeryPost}) {

//     async function addComment() {
//         const commenting = document.querySelector('#addComment' + post.id);
//         const response = await fetch('/api/comments/', {
//             method: "POST",
//             headers: getHeaders(token),
//             body: JSON.stringify({
//                 "post_id": post.id,
//                 "text": commenting.value
//             })
//         });
//         const data = await response.json();
//         console.log(data);
//         requeryPost();
//         commenting.value = "";
//         commenting.focus();
//     }

//     return (
//     <div class="add-comment">
//         <div class="input-holder">
//             <i class="far fa-smile"></i>
//             <input type="text" id={'addComment' + post.id} placeholder="Add a comment..."/>
//         </div>
//             <button class="button" onClick={addComment}>Post</button>
//     </div>
//     );
// }



// import React, { useRef } from "react";
// import { getHeaders } from "./utils";

// export default function AddComment({ token, post, requeryPost }) {
//   const commentingRef = useRef(null);

//   async function addComment(e) {
//     e.preventDefault();

//     const commenting = commentingRef.current;
//     const response = await fetch("/api/comments/", {
//       method: "POST",
//       headers: getHeaders(token),
//       body: JSON.stringify({
//         post_id: post.id,
//         text: commenting.value,
//       }),
//     });
//     const data = await response.json();
//     console.log(data);
//     requeryPost();
//     commenting.value = "";
//     commenting.focus();
//   }

//   return (
//     <form class="add-comment" onSubmit={addComment}>
//       <div class="input-holder">
//         <i class="far fa-smile"></i>
//         <input
//           type="text"
//           id={"addComment" + post.id}
//           placeholder="Add a comment..."
//           ref={commentingRef}
//           autoFocus
//         />
//       </div>
//       <button type="submit" class="button">
//         Post
//       </button>
//     </form>
//   );
// }

import React from 'react';
import {getHeaders} from './utils';
import { useState } from "react";

export default function AddComment({postId, requeryPost, token}) {  
    const [value, setValue] = useState('');


    function handleChange(ev) {
        setValue(ev.target.value)
    }
    
    async function handleSubmit(ev) {
        ev.preventDefault();
        const postData = {
            "post_id": postId,
            "text": value
        };
        
        const response = await fetch('/api/comments', {
                method: "POST",
                headers: getHeaders(token),
                body: JSON.stringify(postData)
            });
        await response.json();
        requeryPost();
        setValue('');
    }

    return (
        <form onSubmit={handleSubmit} className="add-comment">
            <div className="input-holder">
                <input className="comment-textbox" 
                    aria-label="Add a comment" 
                    autoFocus
                    placeholder="Add a comment..."
                    value={value} 
                    onChange={handleChange} />
            </div>
            <button className="link">Post</button>
        </form>
    )
}

