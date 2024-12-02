const httpServer = require('http-server');

const server = httpServer.createServer({
  root: 'C://Users//User//Documents//script//HTML//fikri-tech', // Set the root directory where your HTML files are located
});

server.listen(8080, () => {
    console.log('Server is running at http://localhost:8080/');
  });
  