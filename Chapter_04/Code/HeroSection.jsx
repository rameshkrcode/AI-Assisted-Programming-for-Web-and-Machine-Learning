
import React from 'react';

const HeroSection = () => {
    return (
        <section className="flex flex-col items-center justify-center h-screen bg-gray-100">
            <h1 className="text-4xl font-bold text-blue-600">Enhance Your Workflow with AI</h1>
            <p className="text-lg text-gray-600 mt-2">AI-assisted development for modern web applications.</p>
            <button className="mt-4 px-6 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600">
                Get Started
            </button>
        </section>
    );
};

export default HeroSection;
