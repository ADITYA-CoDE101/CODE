import socket  as  sk

client = sk.socket(sk.AF_INET , sk.SOCK_STREAM)

client.connect(('data.Pr4e.org',80)) # 443 port is used for secue https

req = 'GET http://data.Pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

client.send(req)

while True :
    data = client.recv(301)
    '''if len(data) <= 1:
        break
    print(data.decode())'''
    

client.close()

