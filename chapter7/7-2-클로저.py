def mul(m):
    def inner(n):
        return m * n
    return inner    

mul3 = mul(3)
mul5 = mul(5)

if __name__ == "__main__":
    print(__name__)
    print(mul3(10))  # 30
    print(mul5(10))  # 50
    