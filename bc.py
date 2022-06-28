def foo(a):
    if a == 0:
        return 1
    elif a == 1:
        return 2
    
    k = foo(a-1) + foo(a-2)
    return k


print(foo(7))