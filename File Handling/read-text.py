

'''

#  Using read() method

f=open("mytext.txt", mode='r')
# data=f.read()
data=f.read(6)
data1=f.read(4)
print(data)
print(data1)
f.close()

'''


'''

#  Using readline() method
f=open("mytext.txt", mode='r')
data=f.readline(8)
data1=f.readline()
print(data,end=" ")
print(data1, end=" ")
f.close()

'''
"""
#  Using readlines() method
f=open("mytext.txt", mode='r')
data=f.readlines()
print(data)
f.close()
"""

# Using for loop
f = open("mytext.txt", mode='r')

for line in f:
    print(line)

f.close()
