

stack=[]

def push():
    ele=input("Enter Elements in stack: ")
    stack.append(ele)
    print(stack)

def pop():
    if not stack:
        print("Stack is empty !")
    else:
        e=stack.pop()
        print("Removed...",e)
        print(stack)

while True:
    print("Select the operation"
          "\n 1. Push \n 2.Pop \n 3.quit")
    choice =int(input())
    if choice ==1:
        push()
    elif choice ==2:
        pop()
    elif choice ==3:
        break

    else:
        print("Enter the correct operation")

