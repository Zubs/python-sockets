<?php

$host = '127.0.0.1';
$port = 3000;

set_time_limit(0);

$socket = socket_create(AF_INET, SOCK_STREAM, 0) or die("Unable to create socket!");
echo "Socket created!" . PHP_EOL;

$result = socket_connect($socket, $host, $port) or die("Unable to connect to host");
echo "Connected" . PHP_EOL;

$message = "Vibes";

socket_write($socket, $message, strlen($message)) or die("Could not send message");
echo ":" . $message . PHP_EOL;

$result = socket_read($socket, 1024) or die("Could not read server response");
echo "> " . $result . PHP_EOL;

socket_close($socket);
echo "Socket and connection closed" . PHP_EOL;
