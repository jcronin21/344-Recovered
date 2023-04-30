/**
 * Your logic here (do it however you want).
 * 
 * The things you have to have:
 *    1. A function (i.e., "Event Handler") to initiate the search.
 *    2. Logic to take the user inputs to build the search query.
 *    3. Logic to send the search query to the relevant server.
 *    4. Logic to display the results to the screen.
 * 
 * Provider-specific instructions:
 *    1. If you choose Yelp, allow your user to input both a search term
 *       and a location.
 *          * See API Tutor for guidance: https://www.apitutor.org/
 *          * Sample query: https://www.apitutor.org/yelp/simple/v3/businesses/search?location=Asheville,%20NC&term=pizza
 * 
 *    2. If you choose Spotify, allow your user to specify both a search term 
 *       and a resource type (album, artist, or track).
 *          * See API Tutor for guidance: https://www.apitutor.org/
 *          * Sample query: https://www.apitutor.org/spotify/simple/v1/search?q=beyonce&type=track
 * 
 *    3. If you choose Twitter, allow your user to specify both a search term
 *       and a result_type (mixed, recent, or popular).
 *          * See API Tutor for guidance: https://www.apitutor.org/
 *          * Sample query: https://www.apitutor.org/twitter/simple/1.1/search/tweets.json?q=cats&result_type=popular
 */

//https://www.apitutor.org/spotify/simple/v1/search?q=beyonce&type=album
const rootURL =`https://www.apitutor.org/spotify/simple/v1/search`;

//?q=beyonce&type=album



//+figure out what the user selected/typed into the inputs:
// build the url string
// send the request off to the server use fetch api
//process and display data by looping through the results
const showResults = async (ev) =>{
    console.log('clicked');
    const term = document.querySelector('#term').value;
    const resourceType = document.querySelector('#resource_type').value;
    let endpoint=`${rootURL}?q=${term}&type=${resourceType}`;

    const respone = await fetch(endpoint);
    const data = await respone.json();
    let htmlOutput;
    
    
    // const request = await fetch(endpoint);
    // const jsonData = await request.json();
    // console.log(jsonData);

    // const htmlOutput =jsonData.map(trackToHTML).join('');
    // document.querySelector('#results').innerHTML('beforeend',htmlOutput);
    if(resourceType ==="track"){
        htmlOutput=data.map(dataToTrackCard).join("");
    }else if(resourceType === "artist"){
        htmlOutput=data.map(dataToArtistCard).join("");
    }else{
        htmlOutput=data.map(dataToAlbumCard).join("");
    }

    

document.querySelector(".results").innerHTML="";
document.querySelector(".results").insertAdjacentHTML("beforeend",htmlOutput);
}

const dataToTrackCard = (data) => {
    return `
      <section class="card">
        <div class="pic" style="background-image: url('${data.album.image_url}')"></div>
        <div class="info">
          <h2>${data.name}</h2>
          <p>${data.artist.name}</p>
          <audio controls>
            <source src="${data.preview_url}" type="audio/mp3">
            Your browser does not support the audio element.
          </audio>
        </div>
      </section>
    `;
  }
  
  const dataToArtistCard = (data) => {
    return `
      <section class="card">
        <div class="pic" style="background-image: url('${data.image_url}')"></div>
        <div class="info">
          <h2>${data.name}</h2>
          <p>Popularity: <strong>${data.popularity}</strong></p>
          <a href="${data.spotify_url}">Listen on Spotify</a>
        </div>
      </section>
    `;
  }
  
  const dataToAlbumCard = (data) => {
    return `
      <section class="card">
        <div class="pic album" style="background-image: url('${data.image_url}')"></div>
        <div class="info">
          <h2>${data.name}</h2>
          <p><a href="${data.spotify_url}">Listen on Spotify</a></p>
        </div>
      </section>
    `;
  }
  
// const trackToHTML = track =>{
//     return `
//         <section class="track">
//          <img src ="${track.album.img_url}</>
//          <h2>${track.name}</h2>
//          <p>${track.preview_url}</p>
//         </section>
//    `
// }
// const artistToHTML = artist =>{
//     return `
//         <section class="artist">
//          <img src ="${artist.album.img_url}</>
//          <h2>${artist.name}</h2>
//         </section>
//    `
// }

