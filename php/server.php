<?php

$host = "127.0.0.1";
$port = 3000;

set_time_limit(0);

$socket = socket_create(AF_INET, SOCK_STREAM, 0) or die("Unable to create socket!");
echo "Socket created!" . PHP_EOL;

$result = socket_bind($socket, $host, $port) or die("Could not bind socket to port");
echo "Socket running on http://" . $host . " and bound to port " . $port . PHP_EOL;

$result = socket_listen($socket, 3) or die("Unable to setup listener");
echo "Socket listening on port " . $port . PHP_EOL;

$spawn = socket_accept($socket) or die("Unable to receive requests");
echo "Accepted request from " . $socket . PHP_EOL;

$input = socket_read($spawn, 1024) or die("Unable to read input");
echo "> " . $input . PHP_EOL;

$output = strtoupper($input);
echo ": " . $output . PHP_EOL;

socket_write($spawn, $output, strlen($output)) or die("Could not write output");

socket_close($spawn);
socket_close($socket);
echo "Socket and connection closed" . PHP_EOL;
