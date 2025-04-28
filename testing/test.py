import time

start = time.perf_counter()

# some code
time.sleep(1)

end = time.perf_counter()
print(f"Time taken: {end - start} seconds")
