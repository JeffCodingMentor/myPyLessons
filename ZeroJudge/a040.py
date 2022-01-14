# -*- coding: utf-8 -*-
'''
Zerojudge a040. 阿姆斯壯數
AC (0.5s, 3.3MB)
2021-12-08 15:39
'''

inputstr = input()
inputnumbers = inputstr.split(" ")
# print(inputnumbers)
begin = int(inputnumbers[0])
end = int(inputnumbers[1])
# print(begin, end)
armnumbers = []
for i in range(begin, end+1):
    istr = str(i)
    digit = len(istr)
    d = 0
    num = 0

    while d<digit:
        num += (int(istr[d]))**digit
        d+=1
#     print(i, num)
    if num == i:
        armnumbers.append(i)

if len(armnumbers)!=0:
    for i in range(len(armnumbers)):
        print(armnumbers[i], end=" ")
else:
    print("none")

