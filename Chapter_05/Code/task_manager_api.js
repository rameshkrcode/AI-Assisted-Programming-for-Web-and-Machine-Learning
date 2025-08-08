
// Import required modules
const express = require('express');
const mongoose = require('mongoose');
const app = express();
// Middleware to parse incoming JSON requests
app.use(express.json());
// Connect to local MongoDB database named 'taskDB'
mongoose.connect('mongodb://localhost:27017/taskDB', {
    useNewUrlParser: true,
    useUnifiedTopology: true
});
// Define schema for Task documents
const TaskSchema = new mongoose.Schema({
    title: String,
    description: String,
    completed: Boolean
});
// Create Mongoose model for Task collection
const Task = mongoose.model('Task', TaskSchema);
// Route: Create a new task (POST /tasks)
app.post('/tasks', async (req, res) => {
    const task = new Task(req.body);        // Create a task object from request body
    await task.save();                      // Save the task to MongoDB
    res.status(201).json(task);             // Return the saved task with 201 status
});
// Route: Retrieve all tasks (GET /tasks)
app.get('/tasks', async (req, res) => {
    const tasks = await Task.find();        // Retrieve all tasks from database
    res.json(tasks);                        // Send tasks as JSON response
});
// Route: Update a specific task (PUT /tasks/:id)
app.put('/tasks/:id', async (req, res) => {
    const task = await Task.findByIdAndUpdate(
        req.params.id,                     // Task ID from URL
        req.body,                          // Updated data
        { new: true }                      // Return the updated document
    );
    res.json(task);                        // Send updated task
});
// Route: Delete a task by ID (DELETE /tasks/:id)
app.delete('/tasks/:id', async (req, res) => {
    await Task.findByIdAndDelete(req.params.id);  // Delete task from DB
    res.json({ message: "Task deleted" });        // Send confirmation message
});
// Start the Express server on port 5000
app.listen(5000, () => console.log(`Server running on port 5000`));
