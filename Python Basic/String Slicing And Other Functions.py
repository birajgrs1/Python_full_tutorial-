mystr="Hello World, i'm a python programmer."
print(mystr)
print(type(mystr))

# Slicing
print(mystr[0:5])
print(mystr[:8])
print(mystr[4:])

#Length of whole string
print(len(mystr))

# Slicing advance

print(mystr[0:5:2])
print(mystr[0::2])
print(mystr[-5:])
print(mystr[-8:-1])
print(mystr[-12::2])
print(mystr[::])
print(mystr[::9])

###Functions
print(mystr.isalnum())
print(mystr.isalpha())
print(mystr.isascii())
print(mystr.isdigit())
print(mystr.endswith("programmer."))
print(mystr.count("p"))
print(mystr.capitalize())
print(mystr.find("python"))
print(mystr.lower())
print(mystr.upper())
print(mystr.isprintable())


#Separate   domain name and username from an email ID
email = "grsbiraj123@.com"
username, domain = email.split("@")
print("Username:", username)
print("Domain:", domain)




