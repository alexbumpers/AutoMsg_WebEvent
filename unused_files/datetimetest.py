"""
Tests for datetime module with possible future use. Currently
not in use for the main project.
"""

import datetime

i = datetime.datetime.now()
def day_year(i):
    dy = "%s, %s" % (i.day, i.year)
    print dy
    
print day_year(i)

##maybe add a for loop here that parses web page for 
##tomorrow's day_year
#print str(datetime.date.today()) + str(datetime.timedelta(days=1))
#print datetime.date.today() + datetime.timedelta(days=1)
