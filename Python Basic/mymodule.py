#mymodule.py

person1 = {

    "Name": "Sabin",

    "Age": 22,

    "Country": "Nepal"

}

import mymodule

a = mymodule.person1["Age"]
print(a)

def greeting(name):
    print("Hello, "+name)

import mymodule

mymodule.greeting("Biraj")



