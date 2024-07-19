

# __len__():

class myList:
    def __init__(self,vals):
        self.vals=vals

    def __len__(self):
        return len(self.vals)

li=myList([1,2,3,4,5])
print(len(li))
