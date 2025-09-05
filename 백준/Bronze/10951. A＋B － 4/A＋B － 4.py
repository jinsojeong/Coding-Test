while True:
    try:
        A,B = map(int, input().split())
        print(A + B)
    except EOFError: # 입력이 더이상 없을 떄를 의미
        break