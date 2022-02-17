a=[[1],[2],[]]
def check():
    cC = 0
    for i in a:
        if i:
            cC+=1
    if cC == 1:
        return False
    else:
        return True

print(check())