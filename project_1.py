# Name: Casey Levy
# CS 372 - Sockets and HTTP
# Description: Creating a socket to communicate with a server
# Sources Cited:
# "Computer Networking: A Top-Down Approach", Kurose & Ross, 7th Edition
# https://www.geeksforgeeks.org/socket-programming-python/
# https://www.binarytides.com/python-socket-programming-tutorial/
# https://docs.python.org/3.8/howto/sockets.html

import sys
import socket

# https://www.geeksforgeeks.org/socket-programming-python/
def newSocket():
    sock_main = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Creating a socket
	# Creating host, port number, and then connecting
    host = socket.gethostbyname("gaia.cs.umass.edu")                
    port_num = 80
    sock_main.connect((host, port_num))
	# Setting request
    req = "GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"
	# Encoding, then decoding the request
    sock_main.sendall(req.encode())
    ans = sock_main.recv(1030).decode()
    sock_main.close()

    print("[RECV] - length:", len(ans))
    print(ans)


def httpServer():
	print("Please open your favorite browser and enter '127.0.0.1:2050' ")     
	sock_main = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # Creating a socket
	# Creating host IP, port number, then binding
	host_ip = "127.0.0.1"
	port_num = 2050
	sock_main.bind((host_ip, port_num))
	sock_main.listen()
	print("Listening on port: %s" % port_num)

	data =  "HTTP/1.1 200 OK\r\n"\
            "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
            "<html>Congratulations!  You've downloaded the first Wireshark lab file!</html>\r\n"    

	connect, address = sock_main.accept()
	with connect:
		print("Connected by:", address, "\n")
		while True:
			ans = connect.recv(1030)        # Reading data

			if not ans:
				break

			print("\nReceived: ", ans, "\n")
			print("SENDING>>>>>>")
			connect.sendall(bytes(data, 'utf8'))

			print(data)
			print("<<<<<<<<<")

			sock_main.close()
			break

# https://stackoverflow.com/questions/36230789/how-to-get-html-code-using-python-sockets
def getData():
    sock_main = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # Creating socket
	# Creating host, port number, and connecting
    host = socket.gethostbyname("gaia.cs.umass.edu")
    port_num = 80
    sock_main.connect((host, port_num))
	# Setting request
    req = "GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"
    sock_main.sendall(req.encode())
    ans = sock_main.recv(1030).decode()
    get_ans = ans
    temp = 1     # Use for while loop

    while(temp != 0):
        ans = sock_main.recv(1030).decode()
        get_ans += ans

        if not ans:
            temp = 0

    sock_main.close()

    print("[RECV] - length:", len(get_ans))
    print(get_ans)


def main():
	print(" ---------- Socket/Get File ----------")
	newSocket()
	print(" ---------- Get Large Data ---------- ")
	getData()
	print("\n ---------- HTTP Server ----------")
	httpServer()



if __name__ == "__main__":
    main()
