import React from 'react';


export default function Profile({ profile }) {
    if (!profile) {
        return '';
    }

    return (
        <header>
            <img src={profile.thumb_url} alt="Profile thumbnail" />
            <h3>{profile.username}</h3>

        </header>
    )
}
