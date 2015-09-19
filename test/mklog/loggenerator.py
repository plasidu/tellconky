import random, time, sys, os

if len(sys.argv) <= 1 or str(sys.argv[1]) == '--help' :
    print 'python loggenerator.py output_file period'
    sys.exit(0)

to = sys.argv[1]
interval = sys.argv[2]

def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile):
      if random.randrange(num + 2): continue
      line = aline
    return line

def speak_gibberish(target):
    '''Write random line from freshly generated source log into target'''
    execfile('mklog.py')
    log = open(target, 'a')
    source = open('Log-RMDS-py', 'r')
    log.write(random_line(source))
    log.close()
    source.close()
    os.remove('Log-RMDS-py')

def speak_slowly(target, interval):
    '''Speak gibberish once in the interval to the target'''
    while True:
        speak_gibberish(target)
        time.sleep(interval)

if __name__ == '__main__':
    speak_slowly(to, float(interval))
