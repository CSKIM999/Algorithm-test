from random import randrange 
class TCgen:

    def __init__(self):
        self.returnlst=[]

    def SetReturnOption(self,num):
        self.returnlst=[[] for _ in range(num)]
        print(self.returnlst)
    
    def SingleNumGen(self,limit):
        limitMin,limitMax = limit
        rt = randrange(limitMin,limitMax+1)
        return rt

    def SingleArrayGen(self,limit,Sort=False):
        index,limMin,limMax = limit
        node = self.returnlst[index]
        Temp = []
        for _ in range(node):
            Temp.append(randrange(limMin,limMax+1))
        if Sort:
            Temp.sort()
        return Temp


    def RETURN(self):
        for data in self.returnlst:
            if type(data) != int:
                print(' '.join(map(str,data)))
            else:
                print(str(data))

    def SetOptionLimit(self,W2G,OptionLimitList):
        self.SetReturnOption(W2G)
        for index in range(W2G):
            data = OptionLimitList[index]
            if data[0] == 'SingleNum':
                self.returnlst[index] = self.SingleNumGen(data[1])
            elif data[0] == 'SingleArray':
                self.returnlst[index] = self.SingleArrayGen(data[1])
        self.RETURN()
# print(' '.join(map(str,a))) // 공백으로 구분하여 string으로 합치는 join문

gen = TCgen()

option = [
    ['SingleNum',[1,100]],
    ['SingleNum',[1,100]],
    ['SingleArray',[0,1,1000]]
]

gen.SetOptionLimit(3,option)