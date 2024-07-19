
class SimpleClass:
    def __init__(self,year):
        self.year=year

    def showYear(self):
        print(f"The year is: {self.year}")

myObj=SimpleClass(2024)
# print(myObj.year)
myObj.showYear()