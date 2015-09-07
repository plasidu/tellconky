from fabric.api import cd, put, run, settings, execute
from fabric.api import shell_env
from time import sleep
import os, stat

# Remote working directory
wd = '/tmp'

def bootstrap():
    with (settings(host_string='dunewalker.local', user='takyari', key_filename='/home/takyari/.ssh/id_rsa.pub')):
        with cd(wd):
            put('/home/sync/scripts/py/tellconky/hooks/readlog.py','.')
            put('/home/sync/scripts/py/tellconky/hooks/mkmessage.py','.')

def send_to_pipe(pipe, message):
    fifo = open(pipe, 'w')
    fifo.write(message + '\n')
    fifo.flush()
    fifo.close()

def getlast(logname, last_position):
    output = ''
    with cd(wd):
        with (settings(host_string='dunewalker.local', user='takyari', key_filename='/home/takyari/.ssh/id_rsa.pub')):
            output = run('python mkmessage.py last %s %s' % (logname, last_position))
    return output

def getmessage(last_position, logname='Log-RMDS-py'):
        with cd(wd):
            parts = ['start', 'end', 'heartbeat']
            for message_part in parts:
                pipe = '%s/%s' % (wd, message_part)
                if os.path.isfile(pipe) and not stat.S_ISFIFO(os.stat(pipe).st_mode):
                    #file is not a fifo
                    try:
                        os.remove(pipe)
                    except Exception as ex:
                        print ex
                try:
                    os.mkfifo(pipe)
                except:
                    pass
                output = run('python mkmessage.py %s %s %s' % (message_part, logname, last_position))
                if not output == '':
                    send_to_pipe(pipe, output)
                #pipes should be read by conky
            
def test_deploy(logname, last_position):
    with (settings(host_string='dunewalker.local', user='takyari', key_filename='/home/takyari/.ssh/id_rsa.pub')):
        execute(bootstrap)
        print 'Bootstraping done'
        execute(getmessage, last_position, logname=logname)

if __name__ == '__main__':
    test_deploy('foo.log', 0)
