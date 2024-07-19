
'''
Pickle:
The pickle module implements a fundamental, but powerful algorithm for
serializing and de-serializing a python object structure.
To use pickle, start by importing it in python.
 Example: import pickle
 pickle has two methods:
 1. Dump: which dumps an object to a file object.

 dump()---> The function is called to serialize an object hierarchy.
 Syntax:
 dump(obj,file)
 2. Load: which loads an object from a file object.
 load() ---> The function is called to de-serialize a data stream.
'''
import pickle
#  Serialize ---> dump
example1 = {
    "Name": "Biraj",
    "Age": 21,
    "isEnrolled": ["Python", "Django", "Machine Learning", "Deep Learning", "AI"]
}

# 'wb' mode for writing binary data
# rb --->data read mode
pickle_write=open("text.txt","wb")
pickle.dump(example1,pickle_write)
pickle_write.close()


# de-serialized --->Load
f=open("text.txt","rb")
pickle.load(f)

