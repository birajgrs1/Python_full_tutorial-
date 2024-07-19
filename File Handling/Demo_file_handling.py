age = input('Enter your age: ')

# Open a file named "data.txt" in write ('w') mode.
f = open("data.txt", 'w')
# Write the user's age to the file.
f.write(age)
# Close the file to save the changes.
f.close()


# Open the file "data.txt" in read ('r') mode.
f = open("data.txt", 'r')
# Read and print the contents of the file.
print(f.read())
# Close the file after reading its contents.
f.close()





