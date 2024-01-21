import time
from multiprocessing import Process

def ask_user():
    start1 = time.time()
    user_input = input("What's your name? ")
    print(f"Hello {user_input}, Welcome to concurrency, {time.time() - start1}")


def complex_calculation():
    start2 = time.time()
    print("Started Calculating")
    [x**2 for x in range(20000000)]
    print(f"Completed Calculating, {time.time() - start2}")


start = time.time()
ask_user()
complex_calculation()
print(f"Completed with 1 thread, {time.time() - start}")

process = Process(target=complex_calculation())
process.start()

start = time.time()

ask_user()

process.join()