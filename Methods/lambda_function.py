
a= lambda x:x*2
print("Double of 10 is", a(10))

# Ex2:

my_list = [1, 3, 4, 5, 6, 7, 9, 11, 14, 16, 19]

new_list = list(filter(lambda x: x % 2 == 0, my_list))
print(new_list)
