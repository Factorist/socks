# Socks

### Description

A soket dependent python library that makes sending files and strings more easy and faster than sftp methodes.

### Instalation 

download it and add it to the python lib folder on your PC , Then import it in your python project.
In my case (linux) it is in the `/usr/lib/python3.8/randomlib.py`

### Usage

There are a few available functions ...

- `send_f( ip of the reciver in string format, port of the reciver server [recomended to use a number over 4000],filedirectory as string)` _(void)_

  Sends a file bite by bite using sockets.

- `recv_f(ip from witch to recive a file [Default = "0.0.0.0" allowing anyone to connect to your pc and send a file], port on witch to recive the file ,path and name you want the recived file to have)` _(touple)_

  Listens for an other computer to send a file using the `send_f` function and returns the ip and port from witch the file was sent.

- `sendcmd(ip [same as above],port,a bite string [b'string'],Debug=bolean [default = False] )` _( prints string saying if the connection was succesfull [only hapesn when Debug = True])_
  
  Sends a bite string witch with you may do as you like 
- `recvcmd(ip,port,Debug=bolean[Default = False])`_(returns decoded bite string)_
  
  Listens for an other computer to send a bite string with the sendcmd function and decodes the recived bythe strin to return it.
  If the Debug bolean is True it prints the bite string as recived with out decodeing it and the client who sent it.

 made by the Factorist
