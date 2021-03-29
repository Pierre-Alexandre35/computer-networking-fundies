import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))


while True:
    full_msg = ''
    while True:
        msg = s.recv(8)
        full_msg += msg.decode("utf-8")
        if not msg:
            print("ddd")
            break
    print(1)