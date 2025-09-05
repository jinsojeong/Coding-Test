N = int(input()) # 첫째 줄: 정수 개수 N

nums = list(map(int, input().split())) # 둘째 줄: N개의 정수 리스트
v = int(input()) # 셋째 줄: 찾고 싶은 정수 v

print(nums.count(v)) # 리스트에서 v의 개수를 세어 출력