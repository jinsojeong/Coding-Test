A, B = map(int, input().split())
B -= 45 # 최종 분 (합)

if B < 0:       # 음수가 되면
    B += 60     # 분 보정
    A -= 1      # 시간 -1
    if A < 0:   # 시간이 음수가 되면 23시로 되돌림
        A = 23

print(A, B)