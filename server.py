# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 21:10:55 2024

@author: Administrator
"""

import socket

def start_server(port):
    """Starts a TCP server to receive messages."""
    try:
        while True:
         server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         server_socket.bind(('', port))  # Listen on all interfaces
         server_socket.listen(1)  # Accept only one connection at a time
         #print(f"Server listening on port {port}...")
         client_socket, addr = server_socket.accept()
         #print(f"Accepted connection from {addr}")
         data = client_socket.recv(1024).decode()
         if data=='stop':
                break  # Client disconnected
         else:
                print(f"Received message from client: {data}")

        client_socket.close()
        server_socket.close()

    except Exception as e:
        print(f"Server error: {e}")

if __name__ == "__main__":
    port = 5000  # Choose a port number (must be the same on both PCs)
    start_server(port)