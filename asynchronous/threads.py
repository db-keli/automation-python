#!/usr/bin/env python3
import time
# from threading import Thread
from concurrent.futures import ThreadPoolExecutor


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

# thread1 = Thread(target=complex_calculation())
# thread2 = Thread(target=ask_user())
#
# start3 = time.time()
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()

start = time.time()
with ThreadPoolExecutor(max_workers=2) as Pool:
    Pool.submit(complex_calculation)
    Pool.submit(ask_user)


print(f"Completed with 2 threads, {time.time() - start}")
