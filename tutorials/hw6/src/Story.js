// // Job of this component is to display a single story

// import React from 'react';


// export default function Story({story}) {
//     return (
//         <div>
//             <img src={story.user.thumb_url} class="pic"/>
//             <p>{story.user.username}</p>
//         </div>
//     )
// }
import React from 'react';

export default function Story({model}) {  
    
    if (!model) {
        return '';
    }
    return (
        <div>
            <img src={ model.user.thumb_url } 
                className="pic" 
                alt={ 'profile pic for ' + model.user.username } 
                />
            <p>{ model.user.username }</p>
        </div>
    );     
}