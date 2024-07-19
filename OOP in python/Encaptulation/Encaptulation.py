class Sum:
    def __init__(self):
        self._num1=0  #private variable
        self._num2=0  #private variable

    def setValues(self,num1,num2):
        self._num1=num1
        self._num2=num2

    def add(self):
        return self._num1+self._num2

sum=Sum()
sum.setValues(2,3)
print("Sum of two numbers:", sum.add())
