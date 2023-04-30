import React from "react";
import Carousel from "./Carousel";
import Galleries from "./Galleries";
import { useState } from 'react';


export default function App() {
    const [galleryIdx, setGalleryIdx] = useState(0);

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
    <div className="page-layout">
        <Carousel gallery={galleries[galleryIdx]} />
        <Galleries galleries={galleries} galleryIdx={galleryIdx} setGalleryIdx={setGalleryIdx} />
    </div>
  )
}
