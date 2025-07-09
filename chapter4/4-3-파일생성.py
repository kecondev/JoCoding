'''
f = open("./Temp/test.txt", "w", encoding="utf-8")
f.write("문서의 시작입니다.")

for i in range(5):
    f.write(f"\nLine {i + 1}: This is a test line.")

f.write("\nThis is the end of the file.")
f.close()

r = open("./Temp/test.txt", "r", encoding="utf-8")
print(r.read())

lines = r.readlines()
for line in lines:
    print(line)


r.close()
'''

a = open("./Temp/test.txt", "a", encoding="utf-8")
for i in range(5, 10):
    a.write(f"\nLine {i + 1}: This is an appended test line.")
a.write("\n이 파일의 두번째 끝입니다.")
a.close()