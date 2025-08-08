
import React, { useState } from 'react';

const AICounter = () => {
    const [count, setCount] = useState(0);
    return (
        <div className="text-center">
            <h2 className="text-xl font-bold">Counter: {count}</h2>
            <button onClick={() => setCount(count + 1)} className="px-4 py-2 bg-green-500 text-white rounded">
                Increment
            </button>
        </div>
    );
};

export default AICounter;
