import React from 'react';


export default function NavLinks({profile}) { 



    if (!profile) {
        return '';
    }
    return (
        <ul>   
            <li>API Docs</li>
            <li><span>{profile.username}</span></li>
            <li>Sign out</li>
        </ul> 
    );
    
}
