#!/usr/bin/python
f = open('counter.txt','r')
line = f.readline()
f.close()
f = open('counter.txt','w')
p = int(line)
p += 1
#print p
f.write(str(p))
