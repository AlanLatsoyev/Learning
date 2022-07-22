import socket
import threading

LOCALHOST = "localhost"
PORT = 1488


class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.clientAddress = clientAddress
        self.csocket = clientsocket
        self.msg = ''
        self.number = ''
        self.time = ''
        self.id_ = ''
        self.grop = ''

    def run(self):
        print("Подключение клиента : ", self.clientAddress, flush=True)
        while True:
            if self.check_message():
                break
            self.message_processing()
            self.log_message(self.msg)
        print("Клиент ", self.clientAddress, " покинул нас...")

    def check_message(self):
        data = self.csocket.recv(4096)
        self.msg = data.decode(encoding='utf-8')
        if self.msg == '' or 'exit':
            print("Отключение клиента : ", self.clientAddress, flush=True)
            return True
        try:
            self.msg = self.msg.split('\r')
            self.number, self.id_, self.time, self.grop = self.msg.split(' ')
        except Exception as exc:
            self.csocket.send(bytes(str(exc), 'UTF-8'))
            return True

    def message_processing(self):
        if self.grop[:2] == '00':
            print(f"Спортсмен с нагрудным номером {self.number}"
                  f" прошёл отсечку {self.id_} время {self.time[:10]}", flush=True)

    def log_message(self, msg):
        with open('file.txt', mode='a', encoding='utf8') as f:
            f.write(msg)


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((LOCALHOST, PORT))
    print("Сервер запущен!")

    while True:
        server.listen(1)
        clientsock, clientAddress = server.accept()
        newthread = ClientThread(clientAddress, clientsock)
        newthread.start()
        newthread.join()


if __name__ == '__main__':
    main()


