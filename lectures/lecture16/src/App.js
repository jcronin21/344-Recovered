/** 
 * Instructions
 * 
 * Part 1: Make a Carousel component that is 
 * initialized with the "Gallery 1" images
 *  (a) it should have a next button and a previous button
 *  (b) it should loop around when it gets to the end or the beginning
 * 
 * Part 2: Make a Galleries component that shows the various 
 * galleries that the user can browse.
 *  (a) when the user clicks a gallery, the Carousel component
 *      should re-render with the relevant gallery images
 * 
*/


import React from "react";

export default function App() {
    const galleries = [
        {
            name: "Gallery 1",
            images: [
                '/images/33-300x225.jpg',
                '/images/124-300x225.jpg',
                '/images/227-300x225.jpg'
            ]
        }, {
            name: "Gallery 2",
            images: [
                '/images/257-300x225.jpg',
                '/images/301-300x225.jpg',
                '/images/726-300x225.jpg'
            ]
        }, {
            name: "Gallery 3",
            images: [
                '/images/937-300x225.jpg',
                '/images/949-300x225.jpg',
                '/images/986-300x225.jpg'
            ]
        }
    ]
  return (
    <div>Your Carousel Here...</div>
  )
}
