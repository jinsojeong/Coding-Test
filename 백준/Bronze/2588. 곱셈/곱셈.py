A = int(input())
B = int(input())

hundred = B // 100 # 100으로 나눈 몫
ten = (B // 10) % 10 # 10으로 나눈 것에 10으로 나눈 나머지
one = B % 10 # 100으로 나눈 나머지
print(A * one)
print(A * ten)
print(A * hundred)
print(A * B)