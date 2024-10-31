import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
  print(f"Sleeping for {seconds} seconds")
  time.sleep(seconds) # stop remaining execution and wait for geiven 'seconds'


# normal function call
# print(f"Start : {time.perf_counter()}") # perf_counter is : performace counter. it give the time from starting
# func(3)
# func(2)
# func(1)
# print(f"Start : {time.perf_counter()}")

def main():
  start = time.perf_counter()

  # multithreading function call
  t1 = threading.Thread(target=func, args=[3]) # initializing thread
  t2 = threading.Thread(target=func, args=[2])
  t3 = threading.Thread(target=func, args=[1])

  t1.start() # start thread
  t2.start()
  t3.start()

  t1.join() # keep on programing untill 't1' complete
  t2.join()
  t3.join()

  end = time.perf_counter()
  print(f"Total require time : {end - start}")
main()

# def poolingDemo():
#    with ThreadPoolExecutor() as executor:
#       f1 = executor.submit(func,1)
#       f2 = executor.submit(func,2)
#       f3 = executor.submit(func,3)
#       print(f1.result())
#       print(f2.result())
#       print(f3.result())
#       end = time.perf_counter()
#       print(start-end)

# poolingDemo()