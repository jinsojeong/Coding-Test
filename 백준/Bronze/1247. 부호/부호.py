# 총 3개의 테스트 셋이 주어짐
for _ in range(3):

    # 각 테스트 셋마다 합을 새로 계산해야 하므로 0으로 초기화
    Ans = 0

    # 현재 테스트 셋에서 입력받을 정수의 개수 N
    N = int(input())

    # N개의 정수를 입력받아 합 계산
    for i in range(N):
        A = int(input())
        Ans += A

    # 모든 정수를 다 더한 후, 합의 부호를 판단하여 출력
    if Ans == 0:
        print("0")
    elif Ans > 0:
        print("+")
    else:
        print("-")