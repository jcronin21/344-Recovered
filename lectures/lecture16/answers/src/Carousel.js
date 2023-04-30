import React from "react";
import { useState } from 'react';

export default function Carousel({gallery}) {

    const [idx, setIdx] = useState(0);
    console.log(gallery);
    const currentImageUrl = gallery.images[idx];

    function previous() {
        console.log('previous');
        (idx > 0) ? setIdx(idx - 1) : setIdx(gallery.images.length - 1);
    }

    function next() {
        console.log('next');
        (idx < gallery.images.length - 1) ? setIdx(idx + 1) : setIdx(0);
    }


    return (
        <div className="carousel">
            <h2>{gallery.name}</h2>
            <img src={currentImageUrl} />
            <div class="navigation">
                <button onClick={previous}>Previous</button>
                <p>Photo {idx + 1} of {gallery.images.length}</p>
                <button onClick={next}>Next</button>
            </div>
        </div>
    )
}