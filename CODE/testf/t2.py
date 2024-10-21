import socket 

c = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

c.connect(('localhost',8989))




data1 = c.recv(1024).decode("utf-8")
print(data1)

