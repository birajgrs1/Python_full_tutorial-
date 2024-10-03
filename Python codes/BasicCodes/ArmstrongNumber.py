num = int(input("Enter any number: "))

sum_of_cubes = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum_of_cubes += digit ** 3
    temp //= 10

if sum_of_cubes == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")


# 153 = (1*1*1)+ (5*5*5) + (3*3*3) = 1+125+27 = 153

'''
Other armstrong numbers:  
 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 548834, 1741725, 4210818, 
 9800817, 9926315, 24678050, 24678051, 88593477, 146511208, 472335975, 534494836, 912985153, and 4679307774.
'''
