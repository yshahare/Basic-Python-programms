import time
def count_down(n):
    i=int(input("Enter the starting count no:-")) 
    while n>=i:   
        yield i
        i+=1
        time.sleep(2)
        
n=int(input("Enter the number:-"))
print("****** Count Down Start *********")
for item in count_down(n):
    print(item)