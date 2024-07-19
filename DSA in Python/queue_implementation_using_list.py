

queue=[]

def enqueue():
    ele=input("Enter the element for queue:")
    queue.append(ele)
    print(ele, " is added to queue.")

def dequeue():
    if not queue:
        print("Queue is empty!")
    else:
        e=queue.pop(0)
        print("Removed element: ",e)

def display():
    print(queue)

while True:
    print("Select the operation \n 1. add \n 2. remove \n 3. show \n 4. quit")
    choice=int(input())
    if choice ==1:
        enqueue()
    elif choice ==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Invalid Option !!!")
