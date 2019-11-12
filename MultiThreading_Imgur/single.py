import logging
import os
from time import time
from threading import Thread

from MultiThreading_Imgur.download import setup_download_dir, get_links, download_link

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

os.environ["IMGUR_CLIENT_ID"] = "b4be6ea43ff4763"
"""
After registering an application we get
Client ID:
b4be6ea43ff4763
Client secret:
92b259817368716a8c7150d85ac2aec2d9468cd3
"""
from queue import Queue
##make a worker thread class
class DownloadWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)#override parent methods, means parent class can be called with with either queue param or parents param or both
        self.queue = queue
    def run(self):
        while True:
            #get work from the queue and expand tuple
            directory, link = self.queue.get()
            try:
                download_link(directory, link)
            finally:
                self.queue.task_done()
def main():
    ts = time()
    client_id = os.getenv('IMGUR_CLIENT_ID')
    if not client_id:
        raise Exception("Couldn't find IMGUR_CLIENT_ID environment variable!")
    download_dir = setup_download_dir()
    links = get_links(client_id)
    # Create a queue to communicate with the worker threads
    queue = Queue()
    # Create 8 worker threads
    for x in range(8):
        worker = DownloadWorker(queue)
        # Setting daemon to True will let the main thread exit even though the workers are blocking
        worker.daemon = True
        worker.start()
    # Put the tasks into the queue as a tuple
    for link in links:
        logger.info('Queueing {}'.format(link))
        queue.put((download_dir, link))
    # Causes the main thread to wait for the queue to finish processing all the tasks
    queue.join()
    logging.info('Took %s', time() - ts)

if __name__ == '__main__':
    main()