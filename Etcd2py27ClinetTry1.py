''' etcd2 client. Per https://pypi.python.org/pypi/python-etcd
READ also the README.rst
'''
import etcd
import json
#import os


print ("etcd API2 py2.7 client communicating with etcd version 3, non TLS")
cl0 = etcd.Client(host='127.0.0.1',port=2379)

print ("Print existing tree")
tree0 = cl0.read('/', recursive = True)
print ("old tree", tree0)
child_i=0
tree_ch={} #the tree of children, in dict format
for item in tree0._children:
    data=item
    print ("\nchildren: ",item)
    ##xx if item['dir']=='true': print "A directory"
    if 'nodes' not in item:
        print ("there are no grandsons")
        print ("Key and value: ",item['key'], item['value'])
        tree_ch[item['key']] = item['value']
        print ("DICT: ", tree_ch)
    else:
        print ("there are grandsons:")
        list1=[]
        # we know that the dir = item['key']
        # add the key to the list:
        list1.append({item['key']:'null'})
        for node_item in item['nodes']:
            print "node_item: ",node_item

            if 'nodes' not in node_item:
                print ("there are no grand-grandsons")
                print ("Key and value: ", node_item['key'], node_item['value'])
            else:
                print ("there are grand-grandsons:")
                for node_node_item in node_item['nodes']:
                    print ("A node :", node_node_item)
                    print ("its key and value: ", node_node_item['key'], node_node_item['value'])

#print ("data: ",data)
with open('data.json', 'w') as fp:
     json.dump(data, fp)
print (json.dumps(data,sort_keys=True,indent=4, separators=(',', ': ')))

#print as system command
#cmd = "cat data.json|python -m json.tool"
#returned_value = os.system(cmd)

cl0.write('/node1ns/n1', 1)
cl0.write('/node1ns/n2', 2)
##cl0.write('/node0ns/dir1/c1', 'val_dir1c1')

print ("\nsimple tree\n")
try:
    r1 = cl0.read('/node1ns/n1')
    print (r1)
    print ("r1 key and value: ",r1.key, r1.value)
except etcd.EtcdKeyNotFound:
    # do something
    print ("Error, no such key")

tree = cl0.read('/node1ns', recursive = True) #get all the values of a directory, recursively.
print ("tree: ")
print (tree)
print ("tree key: ",tree.key,tree.value)
for item in tree._children:
    print ("Key and value: ",item['key'], item['value'])

print ("end non-secured client.")


'''
Using host level CLI:
[root@gCentos7 ~]# etcdctl get "node0ns/n1"
1
'''

'''
old tree <class 'etcd.EtcdResult'>(
{'newKey': False, 'raft_index': 111, '_children':

  [{u'createdIndex': 6, u'modifiedIndex': 6, u'nodes':
     [{u'createdIndex': 6, u'modifiedIndex': 6, u'value': u'10', u'key': u'/nodes/n1'}], u'dir': True, u'key': u'/nodes'},

   {u'createdIndex': 7, u'modifiedIndex': 7, u'nodes':
       [{u'createdIndex': 44, u'modifiedIndex': 44, u'value': u'1', u'key': u'/node0ns/n1'},
        {u'createdIndex': 45, u'modifiedIndex': 45, u'value': u'2', u'key': u'/node0ns/n2'},
        {u'createdIndex': 43, u'modifiedIndex': 43, u'nodes':
             [{u'createdIndex': 43, u'modifiedIndex': 43, u'value': u'val_dir1c1', u'key': u'/node0ns/dir1/c1'}],u'dir': True, u'key': u'/node0ns/dir1'}
        ],u'dir': True, u'key': u'/node0ns'},

   {u'createdIndex': 46, u'modifiedIndex': 46, u'nodes':
       [{u'createdIndex': 86, u'modifiedIndex': 86, u'value': u'1', u'key': u'/node1ns/n1'},
        {u'createdIndex': 87, u'modifiedIndex': 87, u'value': u'2', u'key': u'/node1ns/n2'}
        ], u'dir': True, u'key': u'/node1ns'},

   {u'createdIndex': 4, u'modifiedIndex': 4, u'value': u'Hello', u'key': u'/message'},

   {u'createdIndex': 5, u'modifiedIndex': 5, u'value': u'Hello2', u'key': u'/message2'}
  ],

  'createdIndex': None, 'modifiedIndex': None, 'value': None, 'etcd_index': 87, 'expiration': None, 'key': None, 'ttl': None, 'action': u'get', 'dir': True})





'''