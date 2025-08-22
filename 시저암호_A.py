def solution(s, n):
    low = "abcdefghijklmnopqrstuvwxyz"
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = ''
    for char in s:
        if char in low:
            ind = low.find(char)+n
            answer += low[ind%26]
        elif char in up:
            ind = up.find(char)+n
            answer += up[ind%26]
        else:
            answer += " "
    return answer

for i in range(26):
    #print(solution("kbkxeznotm corr hk jutk ol eua zxe ngxj", i))
    print(solution("ulcly wba vmm mvy avttvyyvd doha fvb jhu kvavkhf", i))
