
const os = require('os');
setInterval(() => {
    console.log(`CPU Load: ${os.loadavg()[0]} | Free Memory: ${os.freemem() / 1024 / 1024} MB`);
}, 5000);
