"""
Katie Schaumleffle
Oregon State University
CS372 Fall 2022
Assignment 1: Sockets & Html 
Part 2
"""

#Sources:
# https://zetcode.com/python/socket/
# Textbook: chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://www.ucg.ac.me/skladiste/blog_44233/objava_64433/fajlovi/Computer%20Networking%20_%20A%20Top%20Down%20Approach,%207th,%20converted.pdf
# https://docs.python.org/3/howto/sockets.html


import socket


PORT = 80
HOST = 'gaia.cs.umass.edu'

# create a string to process the get request
uri = "/wireshark-labs/HTTP-wireshark-file3.html"
get_req = "GET " + uri + " HTTP/1.1\r\nHost:" + HOST + "\r\n\r\n"

# Create an INET, STREAMing socket- per zetcode
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    fullData = "" #intialize var as empty string

    server.connect((HOST, PORT))
    # terminate after successfully transmitting data.
    server.sendall(bytes(get_req.encode()))

    # Use a while loop to process the received data and print
    while True:
        # While loop to detect when recv returns <= 0 bytes
        while True:
            data = server.recv(2)
            if not data:
                break
            # Go through the full message
            fullData += data.decode("utf-8")
    
        # if not data:
        #     break

        # Print data
        if len(fullData) > 0:
            print("Request: GET " + uri + " HTTP/1.1 \r\n" + "HOST: " + HOST + "\r\n\r\n")
            print("[RECV] - length: %d" % (len(fullData)))
            print(fullData)

        # Close the connection when recv returns <= 0 byte
        if not data:
            break