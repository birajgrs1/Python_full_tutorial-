#  For loops in python

list1=[["Ram:",23],["Shyam:",22],["Hari:",21],["Sita:",19]
    ,["Gita:",18]]

dict1=dict(list1)
print(dict1)

for name,age in list1:
    print(name,age)

for item in dict1:
    print(name)

# for name,age in dict.items():
#     print(name," and age is ",age)


for i in range(1,11):
    print(i)

print("\n------------------------------------\n\n")
#  while loops in python
x=0

while(x<=100):
    print(x)
    x=x+1

