# Name: Casey Levy
# CS 372 - Server & Client
# Description: Writing a simple client/server program using python sockets
# Sources Cited:
# "Computer Networking: A Top-Down Approach", Kurose & Ross, 7th Edition
# https://realpython.com/python-sockets/
# https://docs.python.org/3/howto/sockets.html
# https://www.youtube.com/watch?v=CV7_stUWvBQ

from socket import *

serv = socket(AF_INET, SOCK_STREAM)
serv.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
ip_serv = "localhost"
port_serv = int(input("\nPlease Input a Port Number: "))

with serv as s:
	s.bind((ip_serv, port_serv))
	s.listen(1)
	print("SERVER LISTENING ON:", ip_serv, "\nON PORT:", port_serv)
	
	connect, address = s.accept()

	with connect:
		print("CONNECTED BY:" + str(address))
		print("\n# Type /q to Quit #")
		print("Waiting to Receive Message...")
		connect.sendall(b"Enter a Message to Send: ")

		while 1:
			receive = connect.recv(2048)
			if not receive or receive.decode() == "/q":
				break
			
			print(receive.decode())
			messg = input("\n> ")
			connect.sendall(str.encode(messg))

print(" \n### SERVER CLOSED ### ")
