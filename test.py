import socket                                                                 
import sys                                                                    
import re                                                                     
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                      
server_address = ('127.0.0.1', 9007)                                          
sock.connect(server_address)                                                  
data = sock.recv(2048).decode()
print(data)

for i in range(100):
  print(str(i)+"-th")
  data = sock.recv(1000).decode()
  arr = re.findall("\d+", data)
  count = int(arr[-1])                                                  
  number = int(arr[-2])                                                 
  low = 0                                                               
  high = number
  print(count, number)
  for i in range(count):
    mid = (low+high)//2
    send = ""
    for j in range(low, mid+1): send += str(j)+" "
    send += "\n"
    sock.send(send.encode())
    data = sock.recv(100).decode()
    result = int(data)
    if result % 10 == 0:
      low = mid + 1
    else:
      high = mid


  sock.send((str(low)+"\n").encode())
  print(sock.recv(100).decode())

data = sock.recv(100).decode()                                
print(data)