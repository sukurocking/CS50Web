def announce(f):
    def wrapper():
        print("About to run function")
        f()
        print("Completed the function")
    return wrapper
    
    
@announce
def hello():
    print("Hello World!")
    
hello()