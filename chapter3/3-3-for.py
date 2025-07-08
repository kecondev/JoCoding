"""
test_list = ["one", "two", "three", "four", "five"]
for item in test_list:
    print(item)

a = [(1, 2), (3, 4), (5, 6)]
for x, y in a:
    print(x + y)

for x in a:
    print(x)

scores = [95, 85, 75, 65, 55]
number = 0
for score in scores:
    number += 1
    if score >= 70:
        print(f"Score {number}: {score} - Passed")
        print("%d번 학생은 합격입니다. 점수 : %d" % (number, score))
    else:
        print(f"Score {number}: {score} - Failed")
        print("%d번 학생은 불합격입니다. 점수 : %d" % (number, score))
"""

marks = [95, 85, 75, 65, 55]
number = 0
for mark in marks:
    number += 1
    if mark < 70:
        continue
    print("%d번 학생은 합격입니다. 점수 : %d" % (number, mark))

rangeValue = range(1, 11)
for i in rangeValue:
    if i % 2 == 0:
        print(f"{i}는 짝수입니다.")
    else:
        print(f"{i}는 홀수입니다.") 



for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end="\t")
    print()