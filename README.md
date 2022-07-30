# Socks

### Description

A socket dependent python library that makes sending files and strings convenient, and it's faster than sftp methodes.

### Installation 

download it and add it to the python lib folder on your PC , Then import it in your python project.
In my case (linux) it is in the `/usr/lib/python3.8/randomlib.py`

### Usage

There are a few available functions ...

- `send_f( ip, port, filepath)` _(void)_

  Sends a file byte by byte using sockets. **ip** is a string of the recivers ip **port** is a number in the range of preferably[4000-65535]

- `recv_f( ip, port, filepath)` _(tuple)_

  Listens for another computer to send a file using the `send_f` function and returns the ip and port from witch the file was sent.
  The **ip** and **port** used in this function must coincide with the ones you used in the `send_f` function.the ip is optional here as it's only used to
  restrict from who to recive files , the defaut beeing everyone.

- `sendcmd(ip,port,a byte string [b'string'],Debug=bolean)` _( prints succesfull if the connection worked)_
  
  Sends a byte string wich with you may do as you like. 
- `recvcmd(ip,port,Debug=bolean)`_(returns decoded byte string)_
  
  Listens for an other computer to send a byte string wich the `sendcmd` function and decodes the recived byte string to return it.
  If the **Debug** bolean is True it prints the bite string as recived with out decoding it and the ip and port of who sent it.
  The **Debug** variable default state is False

 made by the Factorist
