import sys
def Prepare_Coding_Test():
    sys.stdin = open('BOJ_\Input_Data.txt','r')
    beta = open('BOJ_\Output_Data.txt','r')
    delta = beta.readlines()
    beta = []
    for i in delta:
        beta.append(int(i.strip()))
    return beta

def xprint(a):
    for i in a:
        print(i)

def GetPrimeNumbers(n):
    s = [0,0]+[1]*(n-1)
    for i in range(2,int(n**.5)+1):
        if s[i]:
            s[i*2::i] = [0]*((n-i)//i)
    primeList = [i for i,v in enumerate(s) if v]
    return primeList


def isPrime(n):
    if n<2:
        return False
    for i in range(2,int(n**.5)+1):
        if n%i == 0:
            return False
    return True