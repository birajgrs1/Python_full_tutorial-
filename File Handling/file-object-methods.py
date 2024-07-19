'''
# f=open("sample_file.txt",mode='w')
f=open("sample_file.txt",mode='r')

print(f.readable())
print(f.writable())

if f.readable():
    print("File is readable")
else:
    print("File is writable")

f.close()
'''

#  Check file exist or not

import os
print(os.path.isfile("biraj1.txt"))
