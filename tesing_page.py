n = int(input())
while True:
    if n == 1:break
    c = 2
    while True: 
        if n%c == 0: print(c);n = n//c;break
        c+=1