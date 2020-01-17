#!/usr/bin/env python
import gandalf
import sys

if len(sys.argv) > 3:
    hexid_list = []
    g_list = []
    addr = int(sys.argv[1],16)
    for i in range(len(sys.argv)-3):
        hexid = int(sys.argv[i+3],16)
        g = gandalf.Gandalf(hexid)

        hexid_list.append(hexid)
        g_list.append(g)

else:
    print('check the arguments')
    print('expected format (arguments itself can vary): 703c 1 id0 id1 ... idn')

for i in g_list:
    i.writeUSB( addr , int(sys.argv[2],16) )

'''
#!/usr/bin/env python
import gandalf
import sys

if len(sys.argv) > 1:
	addr = int(sys.argv[1],16)
	if (addr>>24)!=0xe0:
		print ("addr format: e0id????")
		sys.exit()
	hexid = (addr>>16) & 0xFF
	addr = addr & 0xFFFF
	g = gandalf.Gandalf(hexid)

if len(sys.argv) == 3:
	g.writeUSB( addr , int(sys.argv[2],16) )
elif len(sys.argv) == 2:
		print ("%08x" % g.readUSB( addr ))
else:
	print("usage: " + sys.argv[0] + " <addr> [<data>]")
'''