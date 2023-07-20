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
        self.to_Log(f'Server established {self.host}:{str(self.port)}')

    def handle_client(self, client_socket):
        self.to_Log(f'In handle client')

    def stop(self):
        self.to_Log(f'Server closed {self.host}:{str(self.port)}')
