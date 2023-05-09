// Your Code Here:

const getStatuses = async (searchTerm,number) => {
    const rootURL = 'https://www.apitutor.org/twitter/simple/1.1/search/tweets.json';
    const endpoint = `${rootURL}?q=${searchTerm}&count=${number}`;
    const response = await fetch(endpoint);
    const jsonData = await response.json();
    console.log(`Matches for ${searchTerm}:`, jsonData);

    // for(let i = 0; i < number; i++){
    //     console.log(jsonData[i].text);
    // }

    return jsonData;
}

function statusToHTML(statusObject){
    const output = `<h1>${statusObject.screen_name}</h1>
            <p>${statusObject.text}</p>
            <button>More</button>`;
  
  
            // return `<h1>${statusObject.screen_name}</h1>
            // <p>${statusObject.text}</p>
            // <button>More</button>`;
  
        return output;
    // document.querySelector("body").innerHTML = output;
  }
  
const displayMatchingStatues = async ()=> {

    //I was going to get the statues then term them into html to be displayed 
    //I totally blanked out bc timed coding test make me nervous and I am ADHD so my focus == bad :))))
    const rootURL = 'https://www.apitutor.org/twitter/simple/1.1/search/tweets.json';
    const term = document.querySelector("#term").value;
    const num = document.querySelector("#count").value;
    const endpoint = `${rootURL}?q=${term}&count=${num}`;
    const response = await fetch(endpoint);
    const jsonData = await response.json();
    console.log(`Matches for ${term}:`, jsonData);
    console.log(data);
    //const statuses = data.map(item => statusToHTML);
    // // for(let i = 0; i < data.length; i++){
    // //     document.querySelector("body").innerHTML = statusToHTML(data[i]);
    // // }
}  