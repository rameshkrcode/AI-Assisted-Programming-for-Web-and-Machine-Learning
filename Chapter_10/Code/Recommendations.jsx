import React, { useEffect, useState } from 'react';
const Recommendations = ({ userId }) => {
  const [recommendations, setRecommendations] = useState([]);
  useEffect(() => {
    fetch(`https://api.example.com/recommend?user_id=${userId}`)
      .then(res => res.json())
      .then(data => setRecommendations(data.items));
  }, [userId]);
  return (
    <div>
      <h2>Your Recommendations</h2>
      <ul>
        {recommendations.map(item => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </div>
  );
};
export default Recommendations;
