import sys
import socket
import json
import glob

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

def menu():
    print "---------------------------------"
    print "1. Download  : download nama_file"
    print "2. Upload    : upload nama_file"
    print "3. Your list : mylist"
    print "4. Exit      : exit"

def checkLocalFiles():
    file_server = []
    file_server.extend(glob.glob('*'))
    print "------------mylist----------------"
    for x in file_server:
        print x
        
# Terima Data List Directory Server
listdir=""
while True:
    data = sock.recv(200)
    if data=="FINISHED":
         break
    listdir+=data

count=1
for files in json.loads(hasil):
    print count, files
    count+=1
menu()
jawab = raw_input()

if jawab=="Exit":
    sock.close()
    sys.exit()
elif jawab =="mylist":
    menu()
    checkLocalFiles()



# try:
#     # Send data
#     message = 'INI ADALAH DATA YANG DIKIRIM ABCDEFGHIJKLMNOPQ'
#     print >>sys.stderr, 'sending "%s"' % message
#     sock.sendall(message)
#     # Look for the response
#     amount_received = 0
#     amount_expected = len(message)
#     while amount_received < amount_expected:
#         data = sock.recv(16)
#         amount_received += len(data)
#         print >>sys.stderr, 'received "%s"' % data
# finally:
#     print >>sys.stderr, 'closing socket'
#     sock.close()