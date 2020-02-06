import socket
import requests, sys


class NetError(Exception):
  pass

class NET:
  global globaltimeout
  globaltimeout = 2
  def conn_ex(host, port):
    try:
      sockex = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      return sockex.connect_ex((host, port))
    except socket.gaierror:
      raise NetError('Error Occured Resolving %s' % (host))

  class TCP:
    timeout = globaltimeout
    socket.setdefaulttimeout(timeout)
    def __init__(self, host, port):
      self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.host = host
      self.port = port
      try:
        self.sock.connect((self.host, self.port))
      except socket.gaierror:
        raise NetError('Error Occured Resolving %s' % (host))
    def send(self, msg="INET-BlackPy"):
      self.sock.send(msg.encode())
    def recv(self, buff=1024):
      self.sock.recv(buff)
    def sendarray(self, data):
      self.sock.sendall(data)
    def close(self):
      self.sock.close()
  
  class UDP:
    timeout = globaltimeout
    socket.setdefaulttimeout(timeout)
    def __init__(self, host, port):
      self.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      self.host = host
      self.port = port

    def send(self, msg="INET-BlackPy"):
      self.udp.sendto(msg.encode(), (self.host,self.port))

    def sendarray(self, data):
      for bytes in data:
        self.udp.sendto(bytes.encode(), (self.host,self.port))

    def recvfrom(self, buff):
      self.udp.recvfrom(buff)

    def close(self):
      self.udp.close()

class CrumbsIO:
    def send(url, cookies):
      cookies = cookies
      cookie_req = requests.get(url, cookies=cookies)
      return cookie_req
    def cookies(url):
      val = {}
      req = requests.get(url)
      cookies = req.cookies
      for cookie in cookies:
        val[cookie.name] = cookie.value
      return val

class machine:
  def ip():
    return socket.gethostbyname(socket.gethostname())
  
  def platform():
    return sys.platform

  def host():
    return socket.gethostname()
  
  def sethost(new):
    if sys.platform == 'linux':
      socket.sethostname(new)