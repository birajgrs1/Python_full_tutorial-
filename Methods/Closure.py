
# Defining a closure function

def print_message(message):
    # This is the outer enclosing function

    def print_message_inner():
        # This is the nested function
        print(message)

    return print_message_inner


another = print_message("Hello, Everyone!")
another()
