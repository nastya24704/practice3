numbers=input()
x,y=map(int, numbers.split())
print(max(x,y)%min(x,y)+1)
