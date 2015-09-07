import time, threading, fabfile

logname = 'foo.log'
last_position = 0

def cycle(logname, last_position):
    while True:
        print 'debug: ', last_position
        fabfile.test_deploy(logname, last_position)
        last_position = fabfile.getlast(logname, last_position)
        time.sleep(5)

def main():
    thread = threading.Thread(target = cycle, args = (logname, last_position))
    thread.start()

if __name__ == '__main__':
    main()
