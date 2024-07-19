'''
class Cart:
    def __str__(self):   #Magic method
        return "This is cart class's obj.  "


c1=Cart()
print(c1)
'''

class Cart:
    def __init__(self,basket1,basket2,basket3):
        self.clothes=basket1
        self.electronics=basket2
        self.others=basket3

    def __len__(self):   #magic method
        print("Total number of items in cart: ")
        return len(self.clothes)+len(self.electronics)+len(self.others)

obj=Cart(['Shirt','Pant','t-shirt'],['mobile','calculator','watch'],['pipe','chair','table'])
print(len(obj))