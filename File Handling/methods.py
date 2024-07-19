
# using tell() method
f=open("mytext.txt",mode='r')
print(f.tell())   #by default 0
f.read(4)
print(f.tell())
f.read()
print(f.seek(7))
f.close()