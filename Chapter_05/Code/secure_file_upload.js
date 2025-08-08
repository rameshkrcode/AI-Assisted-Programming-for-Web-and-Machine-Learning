
const express = require('express');
const multer = require('multer');
const path = require('path');
const app = express();
// Configure upload with file type and size validation
const upload = multer({
    dest: 'uploads/',
    limits: { fileSize: 5 * 1024 * 1024 }, // 5 MB limit
    fileFilter: (req, file, cb) => {
        const filetypes = /jpeg|jpg|png|pdf/;
        const extname = filetypes.test(path.extname(file.originalname).toLowerCase());
        const mimetype = filetypes.test(file.mimetype);
        if (mimetype && extname) {
            return cb(null, true);
        } else {
            cb(new Error("Invalid file type. Only images and PDFs are allowed."));
        }
    }
});
app.post('/upload', upload.single('file'), (req, res) => {
    res.json({ message: "File uploaded securely" });
});
