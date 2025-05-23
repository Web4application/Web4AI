const http = require("http");
const socketIo = require("socket.io");
const app = require("./app");

const server = http.createServer(app);
const io = socketIo(server);

io.on("connection", (socket) => {
  console.log("New client connected");

  socket.on("disconnect", () => {
    console.log("Client disconnected");
  });
});

module.exports = { server, io };
