
import React from "react";
const PortfolioProject = ({ title, description, image }) => (
    <div className="max-w-lg border rounded-lg shadow-lg p-4">
        <img src={image} alt={title} className="w-full h-40 object-cover rounded-md" />
        <h2 className="text-xl font-bold mt-2">{title}</h2>
        <p className="text-gray-600">{description}</p>
    </div>
);
export default PortfolioProject;
