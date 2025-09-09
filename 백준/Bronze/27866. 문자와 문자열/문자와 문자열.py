# S의 i번째 글자 출력 (백준 27866)
S = input().strip()     # 양끝 공백/개행 제거
i = int(input().strip())
print(S[i - 1])         # 1-index → 0-index로 변환