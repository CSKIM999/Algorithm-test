from random import randrange


class TCgen:

    def __init__(self):
        self.returnlst = []

    def SetReturnOption(self, num):
        self.returnlst = [[] for _ in range(num)]
        # print(self.returnlst)

    def SingleNumGen(self, limit):
        limitMin, limitMax = limit
        rt = randrange(limitMin, limitMax+1)
        return rt

    def NumerousNumGen(self, limit):
        volume, MinLimit, MaxLimit = limit
        returnTable = []
        for i in range(volume):
            returnTable.append(randrange(MinLimit, MaxLimit))
        return returnTable

    def SingleArrayGen(self, limit, Sort=False):
        # limit => [Size, minLimit, maxLimit]
        index, limMin, limMax = limit
        node = self.returnlst[index]
        Temp = []
        for _ in range(node):
            Temp.append(randrange(limMin, limMax+1))
        if Sort:
            Temp.sort()
        return Temp

    def SecondaryArrayGen(self, limit):

        # limit => [rowSize,columnSize,ElementMinLimit, ElementMaxLimit ]

        index, MaxLimit, MinLimit = limit
        x, y = self.returnlst[index]
        returnTable = []
        for _ in range(x):
            temp = []
            for _ in range(y):
                temp.append(randrange(MaxLimit, MinLimit))
            returnTable.append(temp)
        return returnTable

    def MapDataGen(self, limit, element, function=None):
        if function != None:
            pass
        # limit => [rowSize,columnSize,ElementMinLimit, ElementMaxLimit ]
        n = len(element)
        x, y = limit
        returnTable = ''
        for _ in range(x):
            temp = ''
            for _ in range(y):
                temp += element[randrange(0, n)]
            returnTable += temp + '\n'
        return returnTable

    def RETURN(self):
        return self.returnlst
        for data in self.returnlst:
            if type(data) != int:
                if type(data[0]) != int:
                    for i in data:
                        print(' '.join(map(str, i)))
                else:
                    print(' '.join(map(str, data)))
            else:
                print(str(data))

    def SetOptionLimit(self, W2G, OptionLimitList):
        self.SetReturnOption(W2G)
        for index in range(W2G):
            data = OptionLimitList[index]
            if data[0] == 'SingleNum':
                self.returnlst[index] = self.SingleNumGen(data[1])
            elif data[0] == 'SeveralNum':
                self.returnlst[index] = self.NumerousNumGen(data[1])
            elif data[0] == 'SingleArray':
                self.returnlst[index] = self.SingleArrayGen(data[1])
            elif data[0] == 'SecondaryArray':
                self.returnlst[index] = self.SecondaryArrayGen(data[1])
            elif data[0] == 'MapData':
                self.returnlst[index] = self.MapDataGen(data[1], data[2])
        return self.RETURN()
# print(' '.join(map(str,a))) // 공백으로 구분하여 string으로 합치는 join문


gen = TCgen()

# Choice what you want to
# [ SingleNum // SeveralNum // SingleArray // SecondaryArray ]

option = [
    ['MapData', [8, 8], ['#', '.']]
]

a = gen.SetOptionLimit(1, option)[0]
