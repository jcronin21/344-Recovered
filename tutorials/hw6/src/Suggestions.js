import React, { useEffect, useState } from 'react';
import Suggestion from './Suggestion';
import { getHeaders } from './utils';

export default function Suggestions({ token }) {
  const [suggestions, setSuggestions] = useState([]);

  useEffect(() => {
    async function fetchSuggestions() {
      const response = await fetch('/api/suggestions', {
        headers: getHeaders(token)
      });
      const data = await response.json();
      setSuggestions(data);
      console.log(data);
    }
    fetchSuggestions();
  }, [token]);
  if (!suggestions) {
    return '';
  }


  // return some JSX
  return (
    <div className="suggestions">
      <h2>Suggestions</h2>
      <div>
        {suggestions.map((user) => {
         return <Suggestion key={user.id} user={user} token ={token} />

        })}
      </div>
    </div>
  );
}