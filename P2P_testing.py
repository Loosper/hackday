import socket, time
from threading import Thread

def listen(my_ip):
    listen_msg = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    listen_msg.bind((my_ip,2000))
    listen_msg.listen(1)
    send_thr.start()
    send_thr.join()
    while True:
        c, addr = listen_msg.accept()
        print("Connected to {}".format(c))
        data = ""
        msg = ""
        while True:
            data = c.recv(1024)
            if data == 0:
                break
            print(data.decode())
def send(msg):
    send_msg = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = socket.gethostbyname(socket.gethostname()) #IP we want to send too
    port = 2000 #Port receiver is using
    encoded_msg = msg.encode("utf-8")
    send_msg.connect((host,port))
    sent = 0
    while True:
        send_msg.send(encoded_msg[sent:])
        sent = len(encoded_msg[sent:])
        print(sent)
        if len(encoded_msg) <= sent:
            break

ip = socket.gethostbyname(socket.gethostname())
if __name__ == "__main__":
    listen_thr = Thread(target = listen, args = [ip])
    send_thr = Thread(target = send, args = ["hello"])
    listen_thr.start()
    listen_thr.join()


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