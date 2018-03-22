#Python3 clinet for etcd2 with tls
#---------------------------------
import etcd
import json

c0 = etcd.Client(host='10.5.224.21',port=2379,protocol='https', cert=('/root/cfssl/client.pem','/root/cfssl/client-key.pem'),ca_cert='/root/cfssl/ca.pem')

r1=c0.read('/node1ns/n2')
print ("key and value: ",r1.key, r1.value)
print ("children", r1._children)
tree0=c0.read('/',recursive=True)
print ("the whole tree: ",tree0,"\n")

print (json.dumps(tree0._children,sort_keys=True, indent=4))
#print (json.dumps(tree0,sort_keys=True, indent=4))

#print ("tree: ",tree0,"\n")
#print (json.dumps(tree0,sort_keys=True,indent=4, separators=(',', ': ')))
