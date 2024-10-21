import socket as sc 

s = sc.socket(sc.AF_INET , sc.SOCK_STREAM)
s.bind(('localhost', 8989))

s.listen(4)
print("connecting ....")

while True:
    client, addr =  s.accept()
    print(f"connected to {addr}")
   
    print(f"Message from {addr} - messag")
    
    client.send("hello people, I am not here!".encode("utf-8"))

s.closed()