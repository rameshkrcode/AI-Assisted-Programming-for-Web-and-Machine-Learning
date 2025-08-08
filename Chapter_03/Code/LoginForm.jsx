
import React from 'react';

const LoginForm = () => {
  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100">
      <form className="bg-white p-6 rounded-lg shadow-lg">
        <h2 className="text-xl font-bold text-center mb-4">Login</h2>
        <div className="mb-4">
          <label className="block text-gray-700">Email</label>
          <input type="email" className="w-full px-3 py-2 border rounded-lg focus:outline-none" />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">Password</label>
          <input type="password" className="w-full px-3 py-2 border rounded-lg focus:outline-none" />
        </div>
        <button className="w-full bg-blue-500 text-white py-2 rounded-lg">Login</button>
      </form>
    </div>
  );
};

export default LoginForm;
