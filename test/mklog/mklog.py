#-------------------------------------------------------------------------------
#- This is a test module for https://github.com/bolidozor/RMDS-data-uploader/. -
#- Worry NOT.                                                                  -
#-------------------------------------------------------------------------------

import time, sys
from time import strftime, gmtime
path = 'path'
path_audio = 'path_audio'
path_data = 'path_data'
path_image = 'path_image'
path_sort = 'path_sort'
freeSpace = 1000
disk_usage = 50


f = open('Log-RMDS-py','w')

f.write('\n \nRUN.PY\t\t|| ' + time.strftime("%d %b %Y %H:%M:%S", time.gmtime()) + 'Data synchronisation system was started.\n')
f.write('SERVERSETUP.PY\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' Zacatek server setup \n')
f.write('SERVERSETUP.PY\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' slozka ' + path_data + ' neexistuje \n')
f.write('SERVERSETUP.PY\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' slozka ' + path_image + ' neexistuje\n')
f.write('SERVERSETUP.PY\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' slozka ' + path_audio + ' neexistuje \n')
f.write('SERVERSETUP.PY\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' Konec server setup \n')
f.write('SORT.PY\t||!' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' audio source path ' + path + path_audio + " does NOT EXIST" +'\n')
f.write('SORT.PY\t||!' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' data source path ' + path + path_data + " does NOT EXIST" +'\n')
f.write('SORT.PY\t||!' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' image source path ' + path + path_image + " does NOT EXIST" +'\n')
f.write('SORT.PY\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' Zacatek Sortingu \n')
f.write('SORT.PY\t||\t >> ' + strftime("%Y%m%d%H", gmtime()) + ' Konec sort.py - \n')
f.write('SYNC.PY\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' Start of synchronisation \n')
f.write('SYNC.PY\t\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + '  >> audio sort path ' + path_sort + path_audio + " does NOT EXIST" +'\n')
f.write('SYNC.PY\t\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' >> data sort path ' + path_sort + path_data + " does NOT EXIST" +'\n')
f.write('SYNC.PY\t\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' >> image sort path ' + path_sort + path_image + " does NOT EXIST" +'\n')
f.write('SYNC.PY\t\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + '\t >>   Start of Upload\n')
f.write('SYNC.PY\t\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + '\t >>    Finish of upload \n')
f.write('SYNC.PY\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' Internet connection is NOT available' + '\n')
f.write('DISKGUARD.PY\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + " disk usage:" + str(freeSpace) + "MB free" + " from " + str(disk_usage) + "MB" + '  \n')
f.write('DISKGUARD.PY\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + " disk usage:" + str(freeSpace) + "MB free" + " from " + str(disk_usage) + "MB" + " !!!!!! Na disku dochazi misto :" + '  \n')
f.write('DISKGUARD.PY\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + " disk usage:" + str(freeSpace) + "MB free" + " from " + str(disk_usage) + "MB" + " !!!!!! Zacalo mazani disku :" + '  \n')

f.close()

