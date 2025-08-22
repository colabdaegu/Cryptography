k = None
s = '속들담담의겨을지있보혜음면와을그삶알나의수라통있선찰어조이요'

while (k!=0):
    answer=''
    k = int(input())
    for o in range(0, k):
        for i in range(o, len(s), k):
            answer += s[i]

    print(answer)
