import time
def countdown(n):
    i=int(input("Enter the starting count number:-"))
    while n>=i:
        yield i
        i+=1
        time.sleep(2)

n=int(input("Enter the no:-"))
for item in countdown(n):
    print(item)        