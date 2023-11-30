import time
import threading
import queue
import requests
from utils import is_prime, DEFAULT_NUMBERS

q = queue.Queue()


def worker(number):
    start = time.time()
    time.sleep(2)
    print(f"worker {number}, started {start}, finished {time.time()}")


def get_page(number):
    # while q.empty():  # race condition
    while True:
        url = q.get()
        # print(f"Thread stated {url}")
        try:
            response = requests.get(url)
        except:
            print(f"Error occurred {url}")
        print(f"worker {number} \t get completed {url} \t queue size {q.qsize()}")
        q.task_done()
        if q.empty():
            break


def show_is_prime(worker_id):
    while True:
        number = q.get()
        is_prime(number)
        q.task_done()
        if q.empty():
            break


def multi_thread():
    # for i in range(5):
    #     worker(i)

    # for i in range(5000):
    #     t = threading.Thread(target=worker, args=(i, ))
    #     t.start()

    # links = [
    #             "https://7learn.ac",
    #             "https://google.com",
    #         ] * 2
    #
    # for link in links:
    #     q.put(link)
    #
    # threads = list()
    # for i in range(6):
    #     t = threading.Thread(target=get_page, args=(i,))
    #     threads.append(t)
    #     # t.setDaemon(True)
    #     t.start()

    # print("Thread not joined yet")
    # q.join()
    # for tr in threads:
    #     tr.join()

    for num in DEFAULT_NUMBERS:
        q.put(num)

    threads = list()
    for i in range(6):
        t = threading.Thread(target=show_is_prime, args=(i,))
        threads.append(t)
        t.setDaemon(True)
        t.start()

    print("Thread not joined yet")
    q.join()
    print("Threads finished")


class CustomThread(threading.Thread):

    def __init__(self, limit, queue, *args, **kwargs):
        self.limit = limit
        self.queue = queue
        super().__init__(*args, **kwargs)

    def run(self):
        counter = 0
        while counter < self.limit:
            print(f"{self.name} QSize: {self.queue.qsize()}")
            number = self.queue.get()
            is_prime(number)
            counter += 1
        print(f"{self.name} Thread reached limitation")

        # for _ in range(self.limit):
        #     number = self.queue.get()
        #     show_is_prime(number)


class SiteCrawler(threading.Thread):
    running = True

    def __init__(self, start_point, *args, **kwargs):
        self.start_point = start_point
        super().__init__(*args, **kwargs)

    def run(self):
        while self.running:
            super().run()


if __name__ == "__main__":
    for i in DEFAULT_NUMBERS:
        q.put(i)

    c1 = CustomThread(100, q)
    c2 = CustomThread(50, q)

    c1.start()
    c2.start()

    time.sleep(45)
    SiteCrawler.running = False
    c1.join()
    c2.join()
