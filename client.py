# Name: Casey Levy
# CS 372 - Server & Client
# Description: Writing a simple client/server program using python sockets
# Sources Cited:
# "Computer Networking: A Top-Down Approach", Kurose & Ross, 7th Edition
# https://realpython.com/python-sockets/
# https://docs.python.org/3/howto/sockets.html
# https://www.youtube.com/watch?v=CV7_stUWvBQ

from socket import *

chat_client = socket(AF_INET, SOCK_STREAM)
ip_client = "localhost"
port_client = int(input("\nPlease Input a Port Number: "))

with chat_client as clnt:
	clnt.connect((ip_client, port_client))
	messg = ""
	print("\n# Type /q to Quit #")
	while messg != "/q":
		rec = clnt.recv(2048)
		print(rec.decode())

		messg = input("\n> ")
		clnt.sendall(str.encode(messg))

print(" \n### CLIENT CLOSED ### ")
