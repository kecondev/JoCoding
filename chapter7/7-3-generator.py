def my_generator(data):
    for item in data:
        yield item

gen = my_generator([1, 2, 3, 4, 5])

#for value in gen:
#    print(value)

gen2 = (i * i for i in range(1, 10))

#for value in gen2:
#    print(value)

def longtime_job():
    import time
    time.sleep(1)
    return "Job finished!"

gen3 = (longtime_job() for _ in range(5))
print(next(gen3))
print(next(gen3))
print(next(gen3))
print(next(gen3))
print(next(gen3))
print(next(gen3))