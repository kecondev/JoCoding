hit = 0
while hit < 5:
    print(f"Hit number: {hit}") 
    hit += 1


prompt = """
... 1. Add
... 2. Del
... 3. List
... 4. Quit
...
... Enter number: """

number = 0
while number != 4:
    print(prompt)
    number = int(input())
    if number != 4:
        print(f"{number}가 입력되었습니다. 해당 작업이 진행됩니다.")
    else:
        print("프로그램을 종료합니다.")