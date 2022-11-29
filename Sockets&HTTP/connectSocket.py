"""
Katie Schaumleffle
Oregon State University
CS372 Fall 2022
Assignment 1: Sockets & Html 
Part 1
"""

#Sources:
# https://zetcode.com/python/socket/
# Textbook: chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://www.ucg.ac.me/skladiste/blog_44233/objava_64433/fajlovi/Computer%20Networking%20_%20A%20Top%20Down%20Approach,%207th,%20converted.pdf
# https://docs.python.org/3/howto/sockets.html


import socket


PORT = 80
HOST = 'gaia.cs.umass.edu'

# create a string to process GET request
uri = "/wireshark-labs/INTRO-wireshark-file1.html"
get_req = "GET " + uri + " HTTP/1.1\r\nHost:" + HOST + "\r\n\r\n"

# Create an INET, STREAMing socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    # Connect to the web server on port 80
    server.connect((HOST, PORT))

    # Send the GET request to read the page
    server.sendall(bytes(get_req.encode()))

    # Use a while loop to process the received data and print
    while True:
        data = server.recv(1028)
        if not data:
            break
        print("Request: GET " + uri + " HTTP/1.1 \r\n" + "HOST:" + HOST + "\r\n\r\n")
        print("[RECV] - length: %d" % (len(data)))
        print(data.decode())