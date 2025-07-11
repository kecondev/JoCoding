import time

def elapsed_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Elapsed time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@elapsed_time
def sample_function(n):
    time.sleep(n)
    return "Function complete"

if __name__ == "__main__":
    print(sample_function(3))