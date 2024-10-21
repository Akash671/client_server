# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 21:06:04 2024

@author: Administrator
"""

import socket
import tkinter as tk
from tkinter import scrolledtext

def send_message():
    message = message_entry.get("1.0", tk.END).strip()
    if message:
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ip = ip_entry.get()
            port = int(port_entry.get())
            client_socket.connect((ip, port))
            client_socket.sendall(message.encode())
            client_socket.close()
            chat_log.insert(tk.END, f"You: {message}\n")
            chat_log.see(tk.END)
            message_entry.delete("1.0", tk.END)
        except Exception as e:
            chat_log.insert(tk.END, f"Error sending message: {e}\n")
            chat_log.see(tk.END)

root = tk.Tk()
root.title("Client")

ip_label = tk.Label(root, text="Server IP:")
ip_label.grid(row=0, column=0, padx=5, pady=5)
ip_entry = tk.Entry(root)
ip_entry.insert(0, "10.97.116.65") # Replace with server's IP
ip_entry.grid(row=0, column=1, padx=5, pady=5)

port_label = tk.Label(root, text="Port:")
port_label.grid(row=1, column=0, padx=5, pady=5)
port_entry = tk.Entry(root)
port_entry.insert(0, "5000")
port_entry.grid(row=1, column=1, padx=5, pady=5)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=2, column=1, pady=10)

message_entry = tk.Text(root, height=3, width=30)
message_entry.grid(row=2, column=0, padx=5, pady=5)

chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD)
chat_log.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()