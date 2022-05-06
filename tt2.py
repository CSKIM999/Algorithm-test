gems =["XYZ", "XYZ", "XYZ"]

num = len(set(gems))
length = len(gems)
l,r = 0,0
ans = []
lst = {}
lst[gems[0]] = 1

while True:
    
    if len(lst) == num:
        if not ans:
            ans = [l,r]
        else:
            if r-l < ans[1]-ans[0]:
                ans = [l,r]
        lst[gems[l]] -=1
        if lst[gems[l]] == 0:
            del lst[gems[l]]
        l += 1
        
        if l>r:
            r = l
            try:
                lst[gems[r]] = 1
            except IndexError:
                break

    else:
        r +=1
        try:
            lst[gems[r]] += 1
        except KeyError:
            lst[gems[r]] = 1
        except IndexError:
            break
    if l >length-1 or r > length:
        break

ans[0],ans[1] = ans[0]+1,ans[1]+1
print(ans)