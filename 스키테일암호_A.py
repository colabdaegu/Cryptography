k = 6
s = 'SYBLCRESEERACHTAYPUOHIPHRUEMTYILSOO!TDFG'

answer=''
for o in range(0, k):
    for i in range(o, len(s), k):
        answer += s[i]

print(answer)
