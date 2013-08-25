import os
import time

source = ['/Users/varun/Desktop/bookmann.in/']

target_dir = '/Users/varun/Desktop/backup_v1/'

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr '%s' %s" % (target, ''.join(source))

if os.system(zip_command) == 0:

	print 'Successful backup to ', target
else:
	print 'Backup failed'


