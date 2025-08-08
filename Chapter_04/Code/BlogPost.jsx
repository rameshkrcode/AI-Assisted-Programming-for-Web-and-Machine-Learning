import React from "react";
const BlogPost = ({ title, summary }) => (
    <div className="max-w-lg border rounded-lg shadow-lg p-4">
        <h2 className="text-xl font-bold">{title}</h2>
        <p className="text-gray-600">{summary}</p>
        <button className="mt-3 px-4 py-2 bg-blue-500 text-white rounded">Read More</button>
    </div>
);
export default BlogPost;