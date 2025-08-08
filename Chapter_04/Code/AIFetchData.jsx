
import React, { useState, useEffect } from "react";
const AIFetchData = () => {
    const [data, setData] = useState([]);
    useEffect(() => {
        fetch("https://jsonplaceholder.typicode.com/posts")
            .then(response => response.json())
            .then(json => setData(json.slice(0, 5))) // Display first 5 results
            .catch(error => console.error("Error fetching data:", error));
    }, []);
    return (
        <div>
            <h2>Fetched Data:</h2>
            <ul>
                {data.map(item => (
                    <li key={item.id}>{item.title}</li>
                ))}
            </ul>
        </div>
    );
};
export default AIFetchData;
