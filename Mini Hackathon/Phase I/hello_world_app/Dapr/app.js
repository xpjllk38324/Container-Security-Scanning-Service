const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

// Middleware
app.use(bodyParser.json());

// Routes
app.get('/hello', (req, res) => {
    res.json({ message: 'Hello, World!' });
});

// Start the server
app.listen(port, () => {
    console.log(`Hello World app listening on port ${port}`);
});
