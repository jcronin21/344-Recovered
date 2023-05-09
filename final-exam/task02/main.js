// 2. Define businessToHTML here:

// const businessToHTML = business => {
//     return `<div class="business" 
//         style="background-image:url('${business}')"></div>
//     `;
// };
// const elem = document.querySelector('.business');
// elem.innerHTML = businessObjPriceDefined.map(businessToHTML).join('\n');




function businessToHTML(businessObjPriceDefined){
    const output = `<h1>${businessObjPriceDefined.name}</h1>
            <p>${location.rating}</p>
            <button>More</button>`;
  
  
            return `<h1>${businessObjPriceDefined.name}</h1>
            <p>${businessObjPriceDefined.rating}</p>
            <button>More</button>`;
  
            return output;

  }
  
  
  
  
  // 2.B. Define userToHTML here:
  function businessToHTML(businessObjPriceNotDefined){
  
    if(businessObjPriceNotDefined.verified == true){
      Vname = `${businessObjPriceNotDefined.name} <i class="fa-solid fa-circle-check"></i>`;
    }else{
      Vname = `${businessObjPriceNotDefined.name}`;
    }
    
  
    return `<img src="">
    <p>name of business: ${businessObjPriceNotDefined.name}</p>
                    <p>Rating: ${businessObjPriceNotDefined.rating}</p>
                    <p>Price: ${businessObjPriceNotDefined.price}</p>`;
  }




/****************/
/* Testing Code */
/****************/

const businessObjPriceDefined = {
    id: "d8Vg0DxRY-s2a8xnZ6ratw",
    name: "Chestnut",
    rating: 4.5,
    image_url:
        "https://s3-media3.fl.yelpcdn.com/bphoto/TprWlxsHLqjZfCRgDmqimA/o.jpg",
    display_address: "48 Biltmore Ave, Asheville, NC 28801",
    coordinates: { latitude: 35.5931657, longitude: -82.550943 },
    price: "$$",
    review_count: 1257,
};

const businessObjPriceNotDefined = {
    id: "d8Vg0DxRY-s2a8xnZ6ratw",
    name: "Chestnut",
    rating: 4.5,
    image_url:
        "https://s3-media3.fl.yelpcdn.com/bphoto/TprWlxsHLqjZfCRgDmqimA/o.jpg",
    display_address: "48 Biltmore Ave, Asheville, NC 28801",
    coordinates: { latitude: 35.5931657, longitude: -82.550943 },
    review_count: 1257,
};

// uncomment this line when you've finished with Q2A:
 console.log("HTML representation of a business:", businessToHTML(businessObjPriceDefined));
 console.log("HTML representation of a business (no price):", businessToHTML(businessObjPriceNotDefined));