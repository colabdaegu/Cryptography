def solution(s, n):
    charE='abcdefghijklmnopqrstuvwxyz'
    charK='ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣ'
    answer = ''
    cryp = ''
    
    for i in s:
        ind=charK.find(i)+n
        print(ind%24)
        answer += charK[ind%24]
    return answer

for i in range(3):
    print(solution("ㄴㅓㅣㅅㅣㅇㅓㅣㅊㅜㄹㅂㅏㄹ", i))
