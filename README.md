# Socks

### Description

A soket dependent python library that makes sending files and strings more easy and faster than sftp methodes.

### Instalation 

download it and add it to the python lib folder on your PC , Then import it in your python project.
In my case (linux) it is in the `/usr/lib/python3.8/randomlib.py`

### Usage

There are a few available functions ...

- `send_f( ip, port, filepath)` _(void)_

  Sends a file bite by bite using sockets. **ip** is a string of the recivers ip **port** is a number in the range of preferably[4000-65535]

- `recv_f( ip, port, filepath)` _(tuple)_

  Listens for an other computer to send a file using the `send_f` function and returns the ip and port from witch the file was sent.
  The **ip** and port used in this function must coincide with the ones you used in the `send_f` function.the ip is optional here as it only used to
  restrict from who to recive files , the defaut beeing everyone.

- `sendcmd(ip,port,a bite string [b'string'],Debug=bolean)` _( prints succesfull if the connection worked)_
  
  Sends a bite string witch with you may do as you like. 
- `recvcmd(ip,port,Debug=bolean[Default = False])`_(returns decoded bite string)_
  
  Listens for an other computer to send a bite string with the sendcmd function and decodes the recived bythe strin to return it.
  If the Debug bolean is True it prints the bite string as recived with out decodeing it and the client who sent it.

 made by the Factorist
