import os
from pymongo import Connection

cn = Connection()
db1 = cn.autotest
while(True):
	coll=db1.contestant.find()
	for c in coll:
		user=c["username"]+".git"
        	print user
		user1="/opt/git/"+user
	  	print user1
          	directory = user1
          	ls = os.listdir(directory)
		#ls = os.listdir("/opt/git/exmp")
          	print ls
          	if not ls:
            		#print "emptyy"
            		os.chdir(user1)
            		os.system("mkdir ttest")
            		os.chdir("ttest")
            		os.system("cp -f /vagrant/starter-files/* .")
