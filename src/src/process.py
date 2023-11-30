import time
# import multiprocessing
from multiprocessing import Pool, Queue, Process

from utils import is_prime, DEFAULT_NUMBERS

# q = Queue()


# def worker(worker_id):
#     while True:
#         number = q.get()
#         start = time.time()
#         is_prime(number)
#         # print(f"worker {worker_id} job {number} started {start} finished {time.time()}")


def multi_process():

    # for i in DEFAULT_NUMBERS:
    #     q.put(i)
    #
    # process_list = list()
    # for i in range(4):
    #     p = multiprocessing.Process(target=worker, args=(i,))
    #     p.start()
    #     process_list.append(p)
    #
    # for pr in process_list:
    #     pr.join()

    pool = Pool(4)
    with pool:
        pool.map(is_prime, DEFAULT_NUMBERS)
    print("All processes finished")