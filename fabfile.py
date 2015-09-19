from fabric.api import cd, put, run, settings, execute
from time import sleep
import os, stat

# Remote working directory
wd = '/tmp'

def bootstrap(hostname, username, keyfile='',):
    with (settings(host_string=hostname, user=username, key_filename=keyfile)):
        with cd(wd):
            put('./hooks/readlog.py','.')
            put('./hooks/mkmessage.py','.')

def send_to_pipe(pipe, message):
    fifo = open(pipe, 'w')
    fifo.write(message + '\n')
    fifo.flush()
    fifo.close()

def getlast(hostname, username, logname, last_position, keyfile=''):
    output = ''
    with cd(wd):
        with (settings(host_string=hostname, user=username, key_filename=keyfile)):
            output = run('python mkmessage.py last %s %s' % (logname, last_position))
    return output

def getmessage(last_position, host, logname='Log-RMDS-py'):
        with cd(wd):
            parts = ['start', 'end', 'heartbeat']
            for message_part in parts:
                pipe = '%s/%s/%s' % (wd, host, message_part)
                if os.path.isfile(pipe) and not stat.S_ISFIFO(os.stat(pipe).st_mode):
                    #file is not a fifo
                    try:
                        os.remove(pipe)
                    except Exception as ex:
                        print ex
                try:
                    os.mkdir('%s/%s' % (wd, host))
                except:
                    pass
                try:
                    os.mkfifo(pipe)
                except:
                    pass
                output = run('python mkmessage.py %s %s %s' % (message_part, logname, last_position))
                if not output == '':
                    send_to_pipe(pipe, output)
                #pipes should be read by conky
            
def test_deploy(hostname, username, logname, last_position, keyfile=''):
    with (settings(host_string=hostname, user=username, key_filename=keyfile)):
        execute(bootstrap, hostname, username, keyfile)
        print 'Bootstraping done'
        execute(getmessage, last_position, hostname, logname=logname)

def deploy(hostname, username, logname, last_position, keyfile=''):
    with (settings(host_string=hostname, user=username, key_filename=keyfile)):
        execute(getmessage, last_position, hostname, logname=logname)

