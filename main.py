import threading

def a():
  while True:
    print("Thread One")
    
def b():
  while True:
    print("Thread Two")
    
x1 = threading.Thread(target=a)
x2 = threading.Thread(target=b)

x1.start()
x2.start()
