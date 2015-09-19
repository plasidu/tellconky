import readlog, sys, os
from time import gmtime, strftime

### INPUT
message_part = str(sys.argv[1])
try:
    logname = str(sys.argv[2])
except:
    logname = 'Log-RMDS-py'
try:
    last_position = int(sys.argv[3])
except:
    last_position = 0


### SETUP
log = readlog.Log(logname)
raw_lines = log.tail(last_position)
regex_list = ['.*[!\s](\d+\s\w+\s\d+\s\d+:\d+:\d+)\s.*', '.*Start\sof\ssynchronisation.*', '.*Finish\sof\supload.*']

### DEBUGGING
#file = open('/tmp/debug', 'a')
#file.write('\nSTOP\n' + str(last_position) + str(raw_lines))
#file.close()

def main(message_part, last_position):
    """Process the log file and print part specified in message_part.

    :message_part: Either start, end or heartbeat. Specifies what to look for in log.
    :returns: Nothing.

    """
    if message_part == 'start':
        regex = regex_list[1]
    elif message_part == 'end':
        regex = regex_list[2]
    elif message_part == 'heartbeat':
        message = strftime("%d %b %Y %H:%M:%S", gmtime()) 
        print 'heartbeat: %s\n' % message
    elif message_part == 'last':
        print log.line_offsets()[-1]
    try:
        lines = readlog.filter_regex(raw_lines, regex)
        message = readlog.filter_time(lines[0], regex_list[0])
        if message:
            print '%s: %s\n' % (message_part, message[0])
    except:
        pass

if __name__ == '__main__':
    main(message_part, last_position)

