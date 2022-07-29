import socket

def recv_f(HOST="0.0.0.0",PORT,FILE):
  
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind((HOST, PORT)) 
  s.listen()
  conn, addr = s.accept()
  print ('Connected from', addr)
  try:
    
    with open(FILE,"wb") as tcp :   
      
      while 1:
        data = conn.recv(2048)
        if not data: 
          break
        tcp.write(data)
        print(data)
      
    s.close()
  
  except KeyboardInterrupt:
    conn.close()
    s.close()
  return addr;

def send_f(HOST,PORT,FILE):
  
  with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    #s.sendall(b"im reddy")
    #data = s.recv(256)
    #print(f"status [ip] :: " , data.decode())
     
    with open(FILE,"rb") as tcp_r :
      
      while True:
        data = tcp_r.read(2048)
        if not data: break
        s.sendall(data)
      
    
  

def sendcmd(HOST,PORT,CMD,Debug=False):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as send:
    send.connect((HOST,PORT))
    send.sendall(CMD)
    
    if Debug : print('sent', CMD)
    
    send.close()
  

def recvcmd(HOST,PORT,Debug=False):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sr :
    sr.bind((HOST,PORT))
    sr.listen()
    msg , addr = sr.accept()
    masa = msg.recv(2048)
    
    if Debug : print(addr,' sent: ',masa)
    
    sr.close()
    masa = masa.decode()
    return masa
  

