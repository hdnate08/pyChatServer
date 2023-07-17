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
        self.is_running = False
        self.client_threads = []

    def start(self):
        self.to_Log(f'Server established, host: {self.host} port: {str(self.port)}')
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        self.is_running = True
        # The next two lines specify a list of sockets to be monitored for availability,
        # and the function, which does the monitoring 'select()'. The two empty arguments
        # are for 'wlist' and 'xlist', which are lists of sockets that can be checked for
        # outgoing data, which can be written and exceptional conditions, such as errors,
        # respectively.
        sockets_to_check = [self.server_socket]
        ready_socket = select.select(sockets_to_check, [], [])

        # Only accept if the socket is open, this needed to be done because the thread would
        # attempt to run accept() on a closed socket and throw an error.
        while self.is_running and (ready_socket == self.server_socket):
            client_socket, client_address = self.server_socket.accept()
            self.to_Log(f"Client connected from {client_address[0]}:{client_address[1]}")

            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            self.client_threads.append(client_thread)
            client_thread.start()

    # The threading outputs below can be removed once its ensured that threading is being
    # handled properly
    def handle_client(self):
        current_thread = threading.current_thread()
        self.to_Log(f"Thread {current_thread.ident} started")
        while self.is_running:
            time.sleep(5)
            self.to_Log(f"Thread {current_thread.ident} printing from handle_client()")

    def stop(self):
        self.to_Log(f'Server closed, host: {self.host} port: {str(self.port)}')
        if self.server_socket:
            self.is_running = False
            self.server_socket.close()

            for thread in self.client_threads:
                self.to_Log(f"Thread {thread.ident} joining...")
                thread.join()
