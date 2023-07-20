"""
pyChat server module
Nathan Harris
July 17, 2023
"""
import threading
import socket
import time
import select


class PyChatServer:
    def __init__(self, host, port, to_log):
        self.host = host
        self.port = port
        self.to_Log = to_log
        self.server_socket = None
        self.client_threads = []
        self.running = False

    def start(self):
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            self.running = True
            self.to_Log("PyChat Server is running on {}:{}".format(self.host, self.port))

            while self.running:
                try:
                    client_socket, client_address = self.server_socket.accept()
                    self.to_Log("New client connected: {}:{}".format(client_address[0], client_address[1]))
                    client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
                    client_thread.start()
                except socket.error:
                    # Handle the exception when server_socket is closed while waiting for connections
                    if not self.running:
                        break
                    else:
                        raise

        except socket.error as error:
            time.sleep(0.25)
            self.to_Log("Error starting the server: {}".format(str(error)))

    def handle_client(self, client_socket):
        try:
            while self.running:
                data = client_socket.recv(1024)
                if not data:
                    break
                message = data.decode("utf-8")
                self.to_Log("Client says: {}".format(message))
        except socket.error as e:
            client_address = client_socket.getpeername()
            self.to_Log("Client disconnected: {}:{}".format(client_address[0], client_address[1]))
        finally:
            client_address = client_socket.getpeername()
            self.to_Log("Client disconnected: {}:{}".format(client_address[0], client_address[1]))
            client_socket.close()

    def stop(self):
        self.running = False
        if self.server_socket:
            self.server_socket.close()
            self.to_Log("PyChat Server has been shut down.")
