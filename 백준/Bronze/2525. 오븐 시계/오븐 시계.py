A, B = map(int, input().split())
C = int(input())

M = B + C # 총 분 합
if M >= 60:
    H = A + (M // 60) # 최종 시간
    M = M % 60  # 최종 분

    if H >= 24:
        H -= 24

else:
    H = A

print(H, M)
