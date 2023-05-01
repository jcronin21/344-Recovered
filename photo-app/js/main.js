// import {getAccessToken} from './utilities.js';
// const rootURL = 'https://photo-app-secured.herokuapp.com';

// const showStories = async (token) => {
//     const endpoint = `${rootURL}/api/stories`;
//     const response = await fetch(endpoint, {
//         headers: {
//             'Content-Type': 'application/json',
//             'Authorization': 'Bearer ' + token
//         }
//     })
//     const data = await response.json();
//     console.log('Stories:', data);
// }

// const showPosts = async (token) => {
//     console.log('code to show posts');
// }


// const initPage = async () => {
//     // first log in (we will build on this after Spring Break):
//     const token = await getAccessToken(rootURL, 'webdev', 'password');

//     // then use the access token provided to access data on the user's behalf
//     showStories(token);
//     showPosts(token);
// }

// initPage();
import { getAccessToken } from './utilities.js';

const rootURL = 'https://photo-app-secured.herokuapp.com';

const showStories = async (token) => {
  const endpoint = `${rootURL}/api/stories`;
  try {
    const response = await fetch(endpoint, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
      }
    });
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    console.log('Stories:', data);
  } catch (error) {
    console.error('Error fetching stories:', error);
  }
}

const showPosts = async (token) => {
  console.log('Code to show posts');
  // Implement function here
}


const initPage = async () => {
  try {
    const token = await getAccessToken(rootURL, 'webdev', 'password');


    showStories(token);
    showPosts(token);
  } catch (error) {
    console.error('Error initializing page:', error);
  }
}

initPage();

