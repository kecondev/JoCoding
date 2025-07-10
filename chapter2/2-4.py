t = (1, 2, 3, (4, 5))

print(t[0])
print(t[3])
print(t[0:])

t1 = (1, 2, 3)
t2 = ('a', 'b', 4, 5)
t3 = t1 + t2
print(t3)  # (1, 2, 3, 'a', 'b', 4, 5)

t4 = t1 * 3
print(t4)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

print(len(t4))  # 길이 출력
print(2 in t4)   # 포함 여부 확인
print(t4.index(2))  # 인덱스 찾기
print(t4.count(1))  # 개수 세기