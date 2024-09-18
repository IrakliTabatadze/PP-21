import time
import threading
import concurrent.futures
import multiprocessing

# def serve_customer(customer):
#     print(f"Serving customer {customer}")
#     time.sleep(1)
#     print(f"{customer} has been served!")
#
# start_time = time.perf_counter()

# serve_customer("Sam")
# serve_customer("Bob")
# serve_customer("Alice")

# serving1 = threading.Thread(target=serve_customer, args=("Sam",))
# serving2 = threading.Thread(target=serve_customer, args=("Bob",))
# serving3 = threading.Thread(target=serve_customer, args=("Alice",))
#
# serving1.start()
# serving2.start()
# serving3.start()
#
# serving1.join()
# serving2.join()
# serving3.join()
#
# end_time = time.perf_counter()
#
# delta = end_time - start_time
# print(f"It took {round(delta, 4)} seconds to serve all customers")

# def print_document(doc):
#     print(f"Printing {doc}.....")
#     time.sleep(3)
#     print(f"{doc} printed!!!")
#
# documents = ["document1", "document2", "document3"]
#
# threads = []
#
# start = time.perf_counter()
# for doc in documents:
#     document_thread = threading.Thread(target=print_document, args=(doc,))
#     document_thread.start()
#     threads.append(document_thread)
#
# for thread in threads:
#     thread.join()
#
# end = time.perf_counter()
# delta = end - start
# print(f"Time taken: {delta}")

# def background_music():
#     while True:
#         print("Annoying music is playing...")
#         time.sleep(1)
#
# def browsing():
#     print("User is browsing this page....")
#     time.sleep(15)
#     print("User has finished browsing")
#
#
# music_thread = threading.Thread(target=background_music)
# music_thread.daemon = True
# music_thread.start()
# browsing()

# balance = 1000
# lock = threading.Lock()
#
# def withdraw(amount):
#     global balance
#
#     with lock:
#         if balance >= amount:
#             print(f"withdrawing {amount}$")
#             time.sleep(1)
#             balance -= amount
#         else:
#             print(f"Insufficient funds")
#
# threads = []
# for _ in range(3):
#     thread = threading.Thread(target=withdraw, args=(500,))
#     threads.append(thread)
#     thread.start()
#
# for thread in threads:
#     thread.join()
#
# print(f"Final balance: {balance}$")
#
# semaphore = threading.Semaphore(3)
#
# def parking_lot(car):
#     print(f"{car} is trying to park")
#     semaphore.acquire()
#     print(f"{car} parked at the spot")
#     time.sleep(5)
#     semaphore.release()
#
# cars = ['BMW', 'Ford', 'Volvo', 'Audi', 'Mercedes']
#
# threads = [threading.Thread(target=parking_lot, args=(car,)) for car in cars]
#
# for thread in threads:
#     thread.start()
#
# for thread in threads:
#     thread.join()

# def sleep_function(secs):
#     print(f"sleeping for {secs} seconds")
#     time.sleep(secs)
#     return f"slept for {secs} seconds"
#
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     secs = [5,4,3,2,1]
#     results = [executor.submit(sleep_function, sec) for sec in secs]
#     # results = executor.map(sleep_function, secs)
#     for result in results:
#         print(result.result())

# def fibonacci(n):
#     if n == 0 or n ==1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# def calculate_fibonacci(number):
#     result = fibonacci(number)
#     print(f"Fibonacci of {number} is {result}")
#
#
# if __name__ == "__main__":
#
#     numbers = [31, 32, 33, 34]
#     start = time.perf_counter()
#     processes = []
#
#     for number in numbers:
#         result = fibonacci(number)
#         print(f"Fibonacci of {number} is {result}")

    # for number in numbers:
    #     process = multiprocessing.Process(target=calculate_fibonacci, args=(number,))
    #     processes.append(process)
    #     process.start()
    #
    # for process in processes:
    #     process.join()
    #
    # end = time.perf_counter()
    #
    # delta = end - start
    # print(f"Time taken to calculate fibonacci is {delta} secs")










