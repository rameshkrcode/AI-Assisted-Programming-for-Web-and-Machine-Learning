
async function fetchData(apiUrl) {
    try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        console.log("API Data:", data);
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

// Example usage:
fetchData("https://jsonplaceholder.typicode.com/posts");
