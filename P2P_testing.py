
host = socket.gethostbyname(socket.gethostname()) #IP we want to send too

'''
sent = 0
send.sendall(encoded_msg)
c, addr = listen.accept()
print("Connected by {}".format(c))
data = ""
msg = ""
while True:
    data = c.recv(1024)
    if not data:
        break
    msg += data.decode()
listen.close()
print(repr(msg))
'''

'''
while True:
    send.send(encoded_msg[sent:])
    sent = len(encoded_msg[sent:])
    if len(encoded_msg) >= len(msg[sent:]):
        break
'''
'''
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
receiver_ip = "10.41.115.93"
port = 12345

s.connect((receiver_ip,port))
s.connec
sent = 0
msg = "Hello world"
while sent < len(msg):
    sent = s.send(msg[sent:])
    if sent == 0:
        print("Connection has not been made")

'''