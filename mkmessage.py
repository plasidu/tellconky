import readlog, sys
from time import gmtime, strftime

### INPUT
message_part = str(sys.argv[1])
#logname = sys.argv[2]
logname = 'foo.log'
#last_message = sys.argv[3]
last_message = 'SERVERSETUP.PY\t|| 02 Sep 2015 13:57:17 Zacatek server setup\n'

### SETUP
log = readlog.Log(logname)
#last_message = log.last_line()
raw_lines = log.tail(last_message)
regex_list = ['.*[!\s](\d+\s\w+\s\d+\s\d+:\d+:\d+)\s.*', '.*Start\sof\ssynchronisatio.*', '.*Finish\sof\supload.*']

def main(message_part):
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
        print 'heartbeat: \n%s \n' % message
    try:
        lines = readlog.filter_regex(raw_lines, regex)
        message = readlog.filter_time(lines[0], regex_list[0])
        print '%s: \n%s \n' % (message_part, message[0])
    except:
        pass

if __name__ == '__main__':
    main(message_part)

