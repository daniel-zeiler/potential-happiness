import collections
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

import requests
import re


def _extract_links(response):
    link_pattern = re.compile(
        r'(http|ftp|https)(:\/\/)([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?')
    links = link_pattern.findall(response.text)
    return links


class WebCrawler:
    def __init__(self, seed, num_threads, max_size):
        self.visited = set()
        self.queue = collections.deque()
        self.max_size = max_size
        self.queue.append(seed)
        self.lock = threading.Lock()
        self.num_threads = num_threads

    def start_crawling(self):
        with ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            threads = [executor.submit(self.crawl)]
            while len(self.visited) < self.max_size:
                for _ in as_completed(threads):
                    if self.queue:
                        threads.append(executor.submit(self.crawl))

    def crawl(self):
        with self.lock:
            url = self.queue.popleft()
            self.visited.add(url)
        response = requests.get(url)
        for protocol, slashes, base, extension in _extract_links(response):
            new_url = protocol + slashes + base + extension
            with self.lock:
                if new_url not in self.visited and len(self.visited) + len(self.queue) < self.max_size:
                    self.queue.append(new_url)


def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec))


start_time = time.time()
web_crawler = WebCrawler(seed="https://www.google.com", num_threads=10, max_size=75)
web_crawler.start_crawling()
end_time = time.time()
time_lapsed = end_time - start_time
time_convert(time_lapsed)
