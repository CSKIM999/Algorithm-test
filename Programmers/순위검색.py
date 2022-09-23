from bisect import bisect_left
info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]

dic = {}
for l in ["cpp", "java", 'python', '-']:
    for g in ['frontend', 'backend', '-']:
        for e in ["junior", "senior", '-']:
            for f in ['pizza', 'chicken', '-']:
                dic[l+g+e+f] = []
for x in range(len(info)):
    lang, group, exp, food, point = list(info[x].split())
    for l in [lang, '-']:
        for g in [group, '-']:
            for e in [exp, '-']:
                for f in [food, '-']:
                    dic[l+g+e+f].append(int(point))
for i in dic:
    if dic[i] != []:
        dic[i].sort()

answer = []
for now in query:
    l, g, e, f = (now.split(' and '))
    f, p = f.split()
    now = dic[l+g+e+f]
    pivot = len(now)
    i = bisect_left(now, int(p))
    answer.append(pivot-i)
print(answer)

# lang = {"java": set(), "cpp": set(), "python": set()}
# exp = {"junior": set(), "senior": set()}
# food = {"pizza": set(), "chicken": set()}
# group = {"backend": set(), "frontend": set()}
# point = []

# for x in range(len(info)):
#     l, g, e, f, p = list(info[x].split())
#     lang[l].add(x)
#     group[g].add(x)
#     exp[e].add(x)
#     food[f].add(x)
#     point.append([int(p), x])
# point.sort()
# Pindex = [i[0] for i in point]
# Iindex = [i[1] for i in point]
# answer = []
# for now in query:
#     l, g, e, f = (now.split(' and '))
#     f, p = f.split()
#     newIndex = bisect_left(Pindex, int(p))
#     pivot = set(Iindex[newIndex:])
#     if l != '-':
#         pivot = pivot & lang[l]
#     if g != '-':
#         pivot = pivot & group[g]
#     if e != '-':
#         pivot = pivot & exp[e]
#     if f != '-':
#         pivot = pivot & food[f]
#     answer.append(len(pivot))
# print(answer)


'''
조건이 간단하다면 브루트포스 한 방법이 더 나은 방법일 수 있다.
'''
