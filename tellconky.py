import sys, time, threading, Queue, fabfile, generate_conkyrc

if len(sys.argv) <= 1 or str(sys.argv[1]) == ('--help' or '-h') :
    print 'python tellconky.py logname/bootstrap username keyfile period host1 host2 .. hostN' 
    sys.exit(0)


logname = str(sys.argv[1])
username = str(sys.argv[2])
keyfile = str(sys.argv[3])
period = float(sys.argv[4])
hosts = sys.argv[5:]

if str(sys.argv[1]) == 'bootstrap' :
    #use to upload hooks only
    for host in hosts:
        fabfile.bootstrap(host, username, keyfile)
    sys.exit(0)

queue = Queue.Queue()

def cycle(hostname, username, logname, keyfile, last_position):
    while True:
        print 'Last position for host ' + hostname + ': ', last_position
        fabfile.deploy(hostname, username, logname, last_position, keyfile)
        last_position = fabfile.getlast(hostname, username, logname, last_position, keyfile)
        time.sleep(period)

class ThreadConnection(threading.Thread):
    """Threaded Connection Grab"""

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
            cycle(host, self.username, self.logname, self.keyfile, self.last_position[host])
            #signals to queue job is done
            self.queue.task_done()

def join_with_timeout(self, timeout):
    # left unused
    self.all_tasks_done.acquire()
    try:
        endtime = time.time() + timeout
        while self.unfinished_tasks:
            remaining = endtime - time.time()
            if remaining <= 0.0:
                print 'Timeout'
                break
            self.all_tasks_done.wait(remaining)
    finally:
        self.all_tasks_done.release()

start = time.time()
def main():
    for host in hosts:
        fabfile.bootstrap(host, username, keyfile)

    generate_conkyrc.main(hosts, period)
    #spawn a pool of threads, and pass them queue instance 
    for i in range(len(hosts)):
        t = ThreadConnection(queue)
        t.setDaemon(True)
        t.start()
    
    #populate queue with data and send hooks
    for host in hosts:
        queue.put(host)
 
    #wait on the queue until everything has been processed, arg is timeout
    #join_with_timeout(queue, 10)
    queue.join()

if __name__ == '__main__':
    main()
