// your code here:

const search = async () => {
    const locationInput = document.querySelector("#location");
    const termInput = document.querySelector("#term");
    const location = locationInput.value;
    const term = termInput.value;
    
    const url = `https://www.apitutor.org/yelp/simple/v3/businesses/search?location=${location}&term=${term}`;
  
    const response = await fetch(url);
    const data = await response.json();
    
    const resultsContainer = document.querySelector("#results");
    resultsContainer.innerHTML = "";
    
    for (const business of data) {
      const name = business.name;
      const rating = business.rating;
      const imageSrc = business.image_url;
      const reviewCount = business.review_count;
      
      const div = document.createElement("div");
      div.classList.add("result");
      
      const img = document.createElement("img");
      img.src = imageSrc;
      img.alt = `${name} photo`;
      
      const h2 = document.createElement("h2");
      h2.textContent = name;
      
      const p1 = document.createElement("p");
      p1.textContent = `Rating: ${rating} (${reviewCount} reviews)`;
      
      div.append(img, h2, p1);
      resultsContainer.append(div);
    }
  };
  