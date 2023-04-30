
const defaultTheme = ev => {
    document.querySelector("body").className="default";
};

const oceanTheme = ev => {
    document.querySelector("body").className="ocean";

};

const desertTheme = ev => {
    document.querySelector("body").className="desert";
};

const highContrastTheme = ev => {
    document.querySelector("body").className="highContrast";
}; 

/*
    Hints: 
    1. Attach the event handlers (functions) above to the click event
       of each of the four buttons (#default, #ocean, #desert, 
        and #high-contrast) in index.html.
    2. Then, modify the  body of each function so that it
       sets the className property of the body tag based on 
       the button that was clicked.
*/
document.getElementById("default").addEventListener("click",defaultTheme);
document.getElementById("ocean").addEventListener("click",oceanTheme);
document.getElementById("desert").addEventListener("click",desertTheme);
document.getElementById("highContrast").addEventListener("click",highContrastTheme);