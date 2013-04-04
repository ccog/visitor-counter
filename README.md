visitor-counter
===============
check_num.cgi
  check_num is a very simple script that simply delivers a number
  from a text file to the php script running on the website for the
  script to print. This number is located in the file counter.txt, and
  represents the count of users having visited the site.

increment.cgi
  Used after the call to check_num.cgi, increment simply reopens the same
  text file used by check_num, counter.txt, and increments the value
  contained inside of it. This is accomplished by reading in and parsing
  the single number in the file, incrementing it, then overwriting the 
  file with the new number.

time_check.cgi
  time_check.cgi will maintain and report the results of a time-based
  histogram located in the file histogram.txt. This file is formatted
  as eight entries of "hr1-hr2 val", where hr1 and hr2 are integers from
  0 to 23 and val is some natural number representing the tally of 
  visitors having visited between the hours outlined by hr1 and hr2.
 
  time_check functions by first reading in all entries from the histogram
  file, then finding the relevant entry of these to the user's visiting
  time. The value associated with this range is then incremented, and the
  updated entry, as well as the other unused entries, are rewritten into
  the histogram file in the same format as they were originally found. The
  site visitor is then notified of their visiting time, as well as the
  current peak hour and tally associated with it.
