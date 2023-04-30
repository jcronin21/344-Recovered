const changeColor = () => {
    document.querySelector('.panel').style.background = 'hotpink';
};

const changeTitle = () => {
    //what do we want to change?
    document.querySelector('.panel').textContent = 'AHHHHH JAVASCRIPT';

    
};

const addImage = () => {
    // adds the following image to each panel:
    // 1. what element do you want to select?
    //`<img src="https://media1.britannica.com/eb-media/22/65322-004-8FF21CDA.jpg" />`;
    const panel = document.querySelector('.panel');
    const img = document.createElement('img');
   img.src = "https://media.istockphoto.com/id/1168168122/photo/beautiful-small-kitten-is-standing-in-the-cat-toilet-and-looking-up-to-the-camera.jpg?b=1&s=170667a&w=0&k=20&c=RZTi-C_DsDp1r4p-vtpnY3vtlUr-1E1XdawF-Ge_VSM=";
   panel.appendChild(img);
};

const clearDiv = () => {
    // clears all of the panels of content
    document.querySelector('.panel').remove();
};
