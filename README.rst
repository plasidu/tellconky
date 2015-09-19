#########
tellconky
#########

A python scriptset for reading remote logs and displaying their filtered content in conky.

* author: Tomas Prochazka (plasidu at email dot cz)
* github: https://github.com/plasidu/tellconky

-------------
Dependencies:
-------------
* python 2.7
* fabric (http://www.fabfile.org/)
* conky (http://www.conky.sourceforge.net)

-----------
Quickstart:
-----------

   git clone https://github.com/plasidu/tellconky.git 
   cd tellconky 
   python tellconky.py logname username keyfile period host1 host2 .. hostN  
   conky -c tellconkyrc 

logname: the name of the file (the remote log) to be read
username: the user as which to login through ssh
keyfile: a file with ssh keys used for authentication
period: time in second after which the remote file is periodicaly read
host1..hostN: hosts running ssh to which to connect

Tellconky.py has to be started from its directory. It send a file to /tmp on remote host and periodicaly uses it to read maximaly 1000 lines of log. After reading it stores last read position and the next run continues there.
Remotely read content is then filtered and then writen to fifo, from which it is suppoesed to be queried by conky, watch or similiar periodicaly reading program.
Running tellconky.py generate tellconkyrc in current directory. This file has to be used as config by conky. 
