#!/usr/bin/python

from datetime import datetime
current_time = str(datetime.time(datetime.now()))

#Read in the data from the histogram file
f = open('histogram.txt')
entries = f.read().splitlines()
f.close()

current_hour = int(current_time.split(':')[0])

final_entries = []

#Find which of the entries in the histogram file is relevant
for entry in entries:
    hours = entry.split()[0]
    hour1 = int(hours.split('-')[0])
    hour2 = int(hours.split('-')[1])
    if (current_hour >=hour1 and current_hour <= hour2):
        final_entries.append(hours + " " + str(int(entry.split()[1]) + 1))
    else:
        final_entries.append(entry)

#Determine the maximum visiting period
max_entry = final_entries[0]
max_count = int(max_entry.split()[1])

for entry in final_entries:
    if (max_count < int(entry.split()[1])):
        max_entry = entry
        max_count = int(entry.split()[1])

print "\nYou are currently visiting at ",current_time,".\n"
print "At present, the peak visiting period is",max_entry.split()[0],"o'clock,"
print "with a current tally of",max_entry.split()[1],"visitor(s)."


#Update the histogram file
f = open('histogram.txt','w')

for entry in final_entries:
    f.write(entry + '\n')
