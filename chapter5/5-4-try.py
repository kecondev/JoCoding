'''
try:
    4 / 0
except ZeroDivisionError as e:
    print("Error:", e)
'''

class MyError(Exception):
    def __init__(self, nick):
        self.nick = nick

    def __str__(self):
        return f"'{self.nick}'은(는) 사용할 수 없는 문구입니다."

def say_nick(nick):
    if nick == "바보":
        raise MyError(nick)
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")  # 이 줄에서 MyError가 발생합니다.
except MyError as e:
    print("Error:", e)
