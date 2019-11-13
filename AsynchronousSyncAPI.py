"""
https://medium.com/@apbetahouse45/asynchronous-web-scraping-in-python-using-concurrent-module-a5ca1b7f82e4
How to handle multiple requests in API
even when web scraping, there is synch handling of requests
There are other ways of asynchronous execution, other than using asyncio lib
    - Process Level multi-processing
    - Thread level multi-processing
    - Application level multi-processing
"""

## Process level multi-processing: By dividing the total work across seperate processes
#Each process running on a different processor core, this way each task is divided into chunks and run on a seperate core, this is built in an OS

##Thread level multi-processing: Here each task is divided across multiple threads.
#Thread is like a light weight process, we can add multiple threads under a single process context
#this is also built in the OS itself, can be utilized using python

##Application level multi-processing: Here the OS thinks that it is executing only one process with a single thread
#but our application schedules different tasks on tht thread for exec
#so async part of application is exectd in our app itself

"Concurrent module can be used to implement the above and give better scraping speeds for large number of requests"
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import Future
from bs4 import BeautifulSoup
import requests

pool_t = ThreadPoolExecutor(3)#3 threads
pool_p = ProcessPoolExecutor(3)#3 processes


def download_extract(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')
    print(list(soup.children))



if __name__ == '__main__':
    from subprocess import call
    download_extract("https://scrapethissite.com")





