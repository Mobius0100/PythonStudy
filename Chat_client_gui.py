import sys
import socket
import threading
import tkinter

BUFFSIZ = 1024

class ChatWin(object):

    def __init__(self, win_name = 'JH'):
        self.top = tkinter.Tk()
        self.win_name = tkinter.Label(self.top, text=win_name)
        self.win_name.pack()

        
class RecvThread(threading.Thread):
    """ 接受消息线程 """

    def __init__(self, sock):
        super().__init__()
        self.daemon = True
        self.sock = sock
    
    def run(self):
        while True:
            msg = self.sock.recv(BUFFSIZ)
            print(msg.decode('utf-8'))

class SendThread(threading.Thread):

    def __int__(self, sock):
        super().__init__()
        self.sock = sock
    

def main(host='localhost', port=21567):
    addr = (host, port)
    tcpcli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpcli_sock.connect(addr)

    recv_thread = RecvThread(tcpcli_sock)
    recv_thread.start()

    while True:
        msg = input('Input >')
        msg = msg.encode('utf-8')
        tcpcli_sock.send(msg)

        if msg == b'exit':
            tcpcli_sock.close()
            break

if __name__ == "__main__":
    main()