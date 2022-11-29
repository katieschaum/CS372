"""
Katie Schaumleffle
Oregon State University
CS372 Fall 2022
Assignment 1: Sockets & Html 
Part 3
"""

# Sources:
# https://zetcode.com/python/socket/
# Textbook: chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://www.ucg.ac.me/skladiste/blog_44233/objava_64433/fajlovi/Computer%20Networking%20_%20A%20Top%20Down%20Approach,%207th,%20converted.pdf
# https://docs.python.org/3/howto/sockets.html - used mostly to set up the socket for server
# https://www.geeksforgeeks.org/python-binding-and-listening-with-sockets/


import socket

PORT = 1385
HOST = '127.0.0.1'
data = "HTTP/1.1 200 OK\r\n"\
        "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
        "<html>Congratulations!  You've downloaded the first Wireshark lab file!</html>\r\n"

# Establish the socket for server using TCP & IPv4
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen(1)
    # connection = server.accept()
    # address = server.accept()

    while True:
           # Accepts a connection, send/rec data via address bound to socket on other end of connection.
           conn, address = server.accept()
           request = conn.recv(1024)
           print("Connected by", address, '\r\n') 
           print("Received:", request, '\r\n')
           conn.sendall(data.encode())
           print("Sending>>>>>>>>")
           print(data)
           print("<<<<<<<<")
           conn.close()
           break