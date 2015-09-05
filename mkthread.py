import time, threading, fabfile

def cycle():
    while True:
        fabfile.test_deploy()
        time.sleep(5)

def main():
    thread = threading.Thread(target = cycle)
    thread.start()

if __name__ == '__main__':
    main()
