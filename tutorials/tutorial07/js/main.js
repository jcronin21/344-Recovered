// Maximize: shift + ⌘ + [
// Minimize: shift + ⌘ + ]

/********************/
/* Global Variables */
/********************/
const rootURL = 'https://photo-app-secured.herokuapp.com';
let token; 


/******************/
/* Your Functions */
/******************/
const showStories = async () => {
    const endpoint = `${rootURL}/api/stories`;
    const response = await fetch(endpoint, {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
    })
    const data = await response.json();
    console.log(data);
    const htmlChunk = data.map(storyToHtml).join('');
    document.querySelector('#stories').innerHTML = htmlChunk;
}

const storyToHtml = story => {
    return `<section class="story">
        <img src="${story.user.thumb_url}" />
        <p>${story.user.username}</p>
    </section>
    `
}

const showPosts = async () => {
    // 1. go out to the internet and grab our posts
    // 2. save the resulting data to a variable
    // 3. transform the data into an HTML represention
    // 4. display it:
    const endpoint = `${rootURL}/api/posts`;
    const response = await fetch(endpoint, {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
    })
    const data = await response.json();
    console.log('Posts:', data);

    const arrayOfHTML = data.map(postToHTML);
    const htmlString = arrayOfHTML.join('');
    document.querySelector('#posts').innerHTML = htmlString;
}
const getBookmarkButton = post =>{
    if (post.current_user_bookmark_id){
        return`
        <button onclick ="unbookmarkPost(${post.current_user_bookmark_id})">
          <i class="fa-solid fa-bookmark"></i>
        </button>
        `;
        
    }else{
        return`
        <button onclick ="BookmarkPost(${post.id})">
         <i class="fa-regular fa-bookmark"></i>
        </button>
        `;
    }
   
    
}

const BookmarkPost = async (postID) => {
    // define the endpoint:
    const endpoint = `${rootURL}/api/bookmarks/`;
    const postData = {
        "post_id": postID // replace with the actual post ID
    };

    // Create the bookmark:
    const response = await fetch(endpoint, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        },
        body: JSON.stringify(postData)
    })
    const data = await response.json();
    console.log(data);
}

const unbookmarkPost = async (bookmarkId) => {
    // define the endpoint:
    const endpoint = `${rootURL}/api/bookmarks/${bookmarkId}`;

    // Create the bookmark:
    const response = await fetch(endpoint, {
        method: "DELETE",
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
    })
    const data = await response.json();
    console.log(data);
}
const reQueryRedraw=async(postId)=>{
    const endpoint = `${rootURL}/api/stories`;
    const response = await fetch(endpoint, {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
    })
    const data = await response.json();
    console.log(data);
    
}
const postToHTML = post => {
    // console.log(post.comments.length);
    return `
        <section id="post_${post.id}" class="post">
            <img src="${post.image_url}" alt="Fake image" />

            ${getBookmarkButton(post)}


            <p>${post.caption}</p>
            ${ showCommentAndButtonIfItMakesSense(post) }
        </section>
    `
}

showModal = () => {
    alert('Show Modal');
}

const showCommentAndButtonIfItMakesSense = post => {
    const hasComments = post.comments.length > 0;
    const lastCommentIndex = post.comments.length - 1;
    if (hasComments) {
        return `<div>
            <button onclick="showModal()">View all ${post.comments.length} comments</button>
            <p>${post.comments[lastCommentIndex].text}</p>
        </div>`;
    } else {
        return '';
    } 
}


const initPage = async () => {
    // set the token as a global variable 
    // (so that all of your other functions can access it):
    token = await getAccessToken(rootURL, 'webdev', 'password');
    console.log(token);
    
    // then use the access token provided to access data on the user's behalf
    showStories();
    showPosts();

    // query for the user's profile
    // query for suggestions
}


/********************/
/* Helper Functions */
/********************/

// helper function for logging into the website:
const getAccessToken = async (rootURL, username, password) => {
    const postData = {
        "username": username,
        "password": password
    };
    const endpoint = `${rootURL}/api/token/`;
    const response = await fetch(endpoint, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(postData)
    });
    const data = await response.json();
    return data.access_token;
}

/**
 * Helper function to replace a DOM element.
 * https://developer.mozilla.org/en-US/docs/Web/API/Node/replaceChild
 * 
 *  Arguments: 
 *     1. selector: the selector you want to target (string)
 *     2. newHTML:  the HTML you want to replace
 */
const targetElementAndReplace = (selector, newHTML) => { 
	const div = document.createElement('div'); 
	div.innerHTML = newHTML;
	const newEl = div.firstElementChild; 
    const oldEl = document.querySelector(selector);
    oldEl.parentElement.replaceChild(newEl, oldEl);
}


/******************************************/
/* Invoke initPage to kick everything off */
/******************************************/
initPage();
