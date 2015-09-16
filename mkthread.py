import time, threading, Queue, fabfile

hosts = ['dunewalker.local', 'localhost']
#hostname = 'dunewalker.local'
username = 'takyari'
logname = 'foo.log'
keyfile = '/home/takyari/.ssh/id_rsa.pub'

queue = Queue.Queue()

def cycle(hostname, username, logname, keyfile, last_position):
    while True:
        print 'debug: ', last_position
        fabfile.test_deploy(hostname, username, logname, last_position, keyfile)
        last_position = fabfile.getlast(hostname, username, logname, last_position, keyfile)
        time.sleep(5)

def main2():
    last_position = 0
    thread = threading.Thread(target = cycle, args = (hostname, username, logname, last_position, keyfile))
    thread.start()

# It's obvious. I need to create dictionary with hosts and last positions.

class ThreadUrl(threading.Thread):
    """Threaded Url Grab"""
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.username = username
        self.keyfile = keyfile
        self.logname = logname
        self.last_position = dict()

    def run(self):

        host = self.queue.get()
        self.last_position[host] = 0

        while True:
        #grabs host from queue
   
        #grabs urls of hosts and prints first 1024 bytes of page
        #url = urllib2.urlopen(host)
        #print url.read(1024)
            cycle(host, self.username, self.logname, self.keyfile, self.last_position[host])
   
        #signals to queue job is done
            self.queue.task_done()

start = time.time()
def main():
    #spawn a pool of threads, and pass them queue instance 
    for i in range(len(hosts)):
        t = ThreadUrl(queue)
        t.setDaemon(True)
        t.start()
    
    #populate queue with data   
    for host in hosts:
        queue.put(host)
 
    #wait on the queue until everything has been processed     
    queue.join()

if __name__ == '__main__':
    main()
