
// loggerMiddleware.js

module.exports = (req, res, next) => {
    console.log("Request received at: " + new Date().toISOString());
    console.log("Request Method: " + req.method);
    console.log("Request URL: " + req.url);
    next();
};
