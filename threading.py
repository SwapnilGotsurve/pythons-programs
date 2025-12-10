import threading

def greet(name):
    print("hellow" , name)

t1 = threading.Thread(target=greet, args=("Alice",))
t2 = threading.Thread(target=greet, args=("Bob",))

t1.start()   # Start thread 1
t1.join()    # Wait for thread 1 to finish

t2.start()   # Start thread 2
t2.join()    # Wait for thread 2 to finish
