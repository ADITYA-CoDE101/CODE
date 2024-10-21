import socket 

host = 'en.wikipedia.org'
port = 80

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host,port))

page = "Python_(programming_language)"

req = 'GET https://en.wikipedia.org/{page} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n'

#the 'request' string is an HTTP GET request for the specification wikipedia page . the 'Host' header specifies the domeain , and 'connection :close'indicates that the server should cloce the connectin after sending the respose .

client_socket.sendall(req.encode("utf-8"))

response = b""
while True :
    data = client_socket.recv(4096)
    if not data :
        break
    response += data

client_socket.close()

header, body = response.split(b"\r\n\r\n",1)
print(body.decode)