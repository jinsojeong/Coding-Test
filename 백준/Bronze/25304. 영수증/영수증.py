Total = int(input()) # 총 금액
T = int(input()) # TC
Sum = 0 # 누적 가격을 담을 변수

for _ in range(T): # TC만큼 반복
    A, B = map(int, input().split())
    Sum += A * B

if Total == Sum:
    print("Yes")
else:
    print("No")