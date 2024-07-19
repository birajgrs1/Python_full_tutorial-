# Break and Continue
# Break
x=0

while(True):
    x=x+1
    if x+1<5:
        continue
    print(x+1,end=" ")
    if(x==90):
        x=x+1
        break
        x=x+1

print("\n------------------------------------\n\n")

while(True):
    inp=int(input("Enter a number:"))

    if inp>100:
        print("Congrats you have entered a number greater than 100")
        break
    else:
        print("Try Again")
        continue