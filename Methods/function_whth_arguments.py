
# find-max

def findMax(a,b):
    if a>b:
        return a
    else:
        return b
print("Maximum number is,  ", findMax(4,7))

# Print message
def hello(name, msg = ", How are you?"):
    print("Hello", name, msg)
hello("Ram",", have a nice day. ")
hello("Shyam")


def sum(*args):
    total = 0
    for i in args:
        total += i
    return total

print("Sum of all integers:", sum(1, 2, 3, 4, 5))
