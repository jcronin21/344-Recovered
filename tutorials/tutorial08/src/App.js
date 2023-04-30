import React from 'react';
import NavLinks from './NavLinks';
import Profile from './Profile.js';
import Suggestions from './Suggestions';
import Stories from './StoriesShown';
import Posts from './Posts';

import { useState, useEffect } from "react";
import {getHeaders} from './utils';


export default function App ({token}) { 
    const [profile, setProfile] = useState(null);

    useEffect(() => {
        async function fetchProfile() {
            const response = await fetch('/api/profile', {
                headers: getHeaders(token)
            });
            const data = await response.json();
            setProfile(data)
        }
        fetchProfile();
    }, [token]);

    console.log('access token:', token);
    
    return (
        <div>
            
            {/* Navbar */}
            <nav className="main-nav">
                <h1>Photo App</h1>
                <NavLinks profile={profile} />
            </nav>
           
           {/* Right Panel */}
            <aside>
                <Profile profile={profile} />
                <Suggestions  token={token}/>
            </aside>

            <main>
                {/* <Stories token={token} /> */}
                <Posts token={token} />
            </main>


        </div>
    );
    
}