

class Bank:
    bank_name='NRB'  #Class variables
    rate_of_interest=12

    @staticmethod
    def simple_interest(p,t):
        si=(p*t*Bank.rate_of_interest)/100
        # print(si)
        return si


# Bank.simple_interest(50000,2.5)


p= float(input("Enter principle amount:"))
t= float(input("Enter no of years:"))

Bank.simple_interest(p,t)
print("Simple Interest:", Bank.simple_interest(p, t))