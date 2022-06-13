const server = require('net');

server.createServer((socket) => {
    console.log('New Connection!');

    socket.setEncoding('utf-8');

    socket.write('Hey there, please enter any message here. Type "quit" to exit. \n');

    socket.on('data', (data) => {
        console.log("User typed: " + data.toString());

        if (data.trim().toLowerCase() == "quit") {
            socket.write("Bye Bye!");

            return socket.end();
        }

        socket.write(data);
    });

    socket.on("close", () => {
        console.log("Client has closed server");
    });

    socket.on("end", () => {
        console.log("Client has ended server");
    });

    socket.on("error", (error) => {
        console.log("Error occured: " + error.message);
    });
}).listen(3500);
