def gugu(n):
    result = []
    for i in range(1, 10):
        result.append(f"{n} * {i} = {n * i}")
    return result

result = gugu(2)

print(result)