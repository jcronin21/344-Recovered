import React from 'react'
import Story from './Story'

import React, { useEffect, useState } from 'react';
import { getHeaders } from './utils';

export default function StoriesShown({token}) {  
  const [stories, setStories] = useState([]);
 
  useEffect(() => {
      async function fetchStories() {
          const response = await fetch('/api/stories', {
              headers: getHeaders(token)
          });
          const data = await response.json();
          setStories(data)
      }
      fetchStories();

  }, [token]);  
 
  // return some HTML:
  if (!stories.length===0) {
      return '';
  }
// return the stories:
return(
    <>
    {
        stories.map(story =>{
            return(
                <Story story={story}/>
            )     })
    }
    </>

)
//     if (!stories) {
//         return '';
//     }
//     return (
//         stories.map(story => {
//             return (
//                 <Story model={story} key={'story-' + story.id} token ={token} />
//             )
//         })
//     );     
// }

// function Story({model}){
//     return <div>{model.text}</div>;
 }