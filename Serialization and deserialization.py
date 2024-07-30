#Marshal Module
import marshal

data={'name':'Hasan Ali','age':19,'address':'sharaqpur'}

byte=marshal.dumps(data)
print('After Serialization:',byte)

new_data=marshal.loads(byte)
print('After Deserilaization:',new_data)


#Pickle Module
import pickle

data={'name':'Hasan Ali','age':19,'address':'sharaqpur'}

byte=pickle.dumps(data)
print('After Serialization:',byte)

new_data=pickle.loads(byte)
print('After Deserilaization:',new_data)


#JSON Module
import json

data='{"name":"Hasan Ali","age":19,"address":"sharaqpur"}'



new_data=json.loads(data)
print('After Deserilaization:',new_data)





