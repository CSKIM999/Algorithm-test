'''
0121233000
012   3000

012312344000
0123    4000
'''
# import sys
# input = sys.stdin.readline

# # output = "VhcL2gG57qPJDQibBkUZArnzxELrLMrXRrutlL57BoQRapABp7quwrhFWpMq5je8CGIDwXcs7UVKNt5eI43v3URmlPOqCDGGJ7O4fe4JWNIhxwtz8W8x4DaTHDNjhjJUax3iAgPvgzkqGyTwQSahgIkRbPXIsaaza0XNcpTutgMUbcdRQi0grPmiQMfIYpnRFAkPgm"
# string = input().strip()
# bomb = input().strip()
# i = 0
# bl = len(bomb)
# last = 0
# bombed = set()
# answer = ""
# stack = set()

# l = len(string)
# while string:
#     if i + bl - len(stack) > l:
#         break
#     if i in bombed:
#         i += 1
#         continue
#     stack.add(i)
#     if len(stack) > bl:
#         stack = stack[1:]
#     if stack == bomb:
#         [bombed.add(j) for j in range(i-bl+1, i+1)]
#         stack = ""
#         i -= bl
#         if i < 0:
#             i = 0
#     else:
#         i += 1
# for i in range(l):
#     if i not in bombed:
#         answer += string[i]

# if not string:
#     answer = "FRULA"
# else:
#     answer = string
# print(answer)

# if answer == output:
#     print("YY")
# else:
#     print(answer)
#     print("NN")
a = set([1, 2, 3])
print(a[0])
