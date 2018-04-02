# etcd2 clinet, using python3
# ex: python3 <this py file> [<etcd server ip address>]
#
import etcd
import json
import sys


HOST='10.5.224.21'
#Get TLS file names
CERT_DIR="/root/cfssl/"
CERT=CERT_DIR+'client.pem'
KEY=CERT_DIR+'client-key.pem'
CA=CERT_DIR+'ca.pem'


#class Etcd2Py3Cli:
#    def __init__(self):
#        self.data = []

c0 = etcd.Client(host=HOST,port=2379,protocol='https', cert=(CERT,KEY),ca_cert=CA)

#c0 = etcd.Client(host='10.5.224.21',port=2379,protocol='https', cert=('/root/cfssl/client.pem','/root/cfssl/client-key.pem'),ca_cert='/root/cfssl/ca.pem')
#====================================================
	
#e0 = Etcd2Py3Cli() 

print ("Print existing tree")

## Write section
c0.write('/branch1/n1', 1)
c0.write('/branch1/n2', 2)
c0.write('/branch1/dir2/m2', 22)
c0.write('/branch1/dir2/m3', 33)



top0 = c0.read('/')
#print ("Top: ", top0)
child_i=0
top_keys=[]
top_ch={} #the tree of children, in dict format
for item in top0._children:
    print ("\nChild: ",item)
    data=item
    top_keys.append(item['key'])

print ("Top_keys: ",top_keys)
dirstr = input("Enter requested dir: ")
#depth = input("Enter depth: ")
print ("Requested: ",dirstr)

try:
    dir0 = c0.read(dirstr,recursive = True)
    print ("dir0: ",dir0)
except etcd.EtcdKeyNotFound:
    # do something
    print ("Error, no such dir")

if hasattr(dir0,'key'):
   print (dir0.key, dir0.value)
if dir0._children == []:
   print("No children. End of tree.")
for child in dir0._children:
    print (child['key'], child['value'])
 
#=================================================
print ("+++")
