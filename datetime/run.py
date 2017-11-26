#!/usr/bin/python
# Python 2.6+
from __future__ import print_function

from datetime import datetime
from datetime import timedelta
from datetime import date

import pytz

if __name__ == '__main__':
	print('Try some functionalities regarding date and time.\n')

	print('dt = datetime.now()')

	dt = datetime.now()

	print(dt)
	print("")

	print("A new timedelta object with 10 days, 48 hours, 90 minutes, and 4000 seconds in the future.")
	delta = timedelta(days = 10, hours = 48, minutes = 90, seconds = 4000)
	print("That is ")
	print(delta)

	print("And dt will be")
	print( dt + delta )

	print("It is equivalent to say dt marches %d seconds in time." % delta.total_seconds())
	
	print("")
	print("Create a date object with date.today()")

	d = date.today()

	print(d)

	print("Access year, month, and the day in the month by ")
	print("d.year = %d, d.month = %d, d.day = %d" % (d.year, d.month, d.day))

	print("Modify our delta. Let delta be a time shift of 31 days.")
	delta = timedelta(days = 31)
	print(delta)

	print("Shift d by delta days and get dd")
	dd = d + delta
	print( dd )

	print("We could do a subtraction operation between d and dd and get a timedelta objcet")
	td = d - dd
	print("perform td = d - dd, we should obtain a negative td")
	print(td)

	print("")
	print("Construct a new date object with specific date information: 2012-12-12")
	d = date(year = 2012, month = 2, day = 28)
	print(d)

	print("Change one of the values into some other value with replace() function.")
	print(d.replace(year = 2017))

	try:
		print("Here I attempt to change from 2012-2-29 directly into 2017-12-29 by replace(). An exception will be raised since the February of 2017 does not have 29 days.")
		d = date(year = 2012, month = 2, day = 29)
		d.replace(year = 2017)
	except ValueError as e:
		print("The ValueError exception is caught.")
	else:
		pass
	finally:
		pass

	print("Now let us use today() as the value of d")
	d = date.today()
	print(d)

	print("")
	print("Today is the %dth day of a week. (By using weekday())" % (d.weekday() + 1))
	print("Today is the %dth day of a week. (By using isoweekday())" % (d.isoweekday()))

	print("")
	d = date.today()
	print("Today is the %dth day of this year. (Not in ISO calendar)" % (d.timetuple().tm_yday))

	print("")
	print("What's more interesting is that the day of the year by the ISO standard.")
	print("Let's start with the date Monday 2018-01-01")
	d = date(year = 2018, month = 1, day = 1)
	isoc = d.isocalendar()

	print("It is the %dth day of the %dth week of the year %d." % (isoc[2], isoc[1], isoc[0]))

	print("")
	print("Let's look at the date Monday 2018-12-31")
	d = date(year = 2018, month = 12, day = 31)
	isoc = d.isocalendar()
	print("It is the %dth day of the %dth week of the year %d." % (isoc[2], isoc[1], isoc[0]))

	print("Do you see the difference?")

	print("")
	print("Let's use today() again.")
	d = date.today()
	print("Print the date details in different formats.")
	print("ISO format: %s" % (d.isoformat()))
	print("Custom format: %s" % ( d.strftime("%m/%d/%y") ))
	print("Custom format: %s" % ( d.strftime("%A, %B %d, %y") ))
	print("There are lots of other useful formats.")

	# ================= The datetime class. =================
	
	print("")
	print("The datetime class essentially contains information from a date object and a time object.")
	print("We have datetime.tody() = ", end = "")
	print(datetime.today())
	print("We have datetime.now() = ", end = "")
	print(datetime.now())
	print("We have datetime.utcnow() = ", end = "")
	print(datetime.utcnow())
	print("We have datetime.combine(date, time)")
	print("We have datetime.date()")
	print("We have datetime.now()")
	print("We have datetime.replace()")
	print("We have datetime.weekday()")
	print("We have datetime.isoweekday()")
	print("We have datetime.isocalendar()")
	print("We have datetime.isoformat()")
	print("We have datetime.strftime()")

	print("")
	print("Let n = datetime.now()")
	n = datetime.now()
	print("For isoformat() use n.replace(microsecond = 0).isoformat(" ") to get")
	print( n.replace(microsecond = 0).isoformat(" ") )

	print("")
	print("n.year = %d, n.month = %d, n.day = %d" % (n.year, n.month, n.day))
	print("n.hour = %d, n.minute = %d, n.second = %d" % (n.hour, n.minute, n.second))

	# ================== The time class. =======================

	print("")
	print("OK, the time class is roughly the same with date and datetime.")

	# ================== The tzinfo and pytz. =================

	print("")
	print("One thing we haven't talked about is the concept of timezone.")

	print("")
	print("Get a tzinfo object (tzShanghai) from pytz to represent the 'Asia/Shanghai' timezone.")
	tzShanghai = pytz.timezone('Asia/Shanghai')

	print("Get another tzinfo (tzNewYork) object from pytz to represent the 'America/New_York' timezone. (Note that the underscore is required.)")
	tzNewYork  = pytz.timezone('America/New_York')

	print("")
	print("We can use datetime.now() to obtain a tz aware time specification.")
	print("nShanghai = datetime.now( tzShanghai )")
	nShanghai = datetime.now( tzShanghai )
	print(nShanghai)

	print("")
	print("We can convert nShanghai into the America/New_York timezone. It will be ")
	nNewYork = nShanghai.astimezone( tzNewYork )
	print(nNewYork)

	print("")
	print("Both of the above time specification could be converted into UTC timezone.")
	print( nShanghai.astimezone( pytz.utc ) )

	print("")
	print("The offset from UTC of the timezone 'Asia/Shanghai' AT THE MOMENT is ")
	print("%.2f hours" % (nShanghai.utcoffset().seconds / 3600))

	print("")
	print("The offset from UTC of the timezone 'America/New_York' AT THE MOMENT is ")
	print("%.2f hours" % (nNewYork.utcoffset().seconds / 3600))

	print("")
	print("All the timezones are listed in pytz.all_timezones")
	print("You can also refer to pytz.country_timezones which is a dictionary.")
	print("The index of each entry in the dictionary is an abbreviation of nation name according to ISO 3166.")
	print("The value of each entry in the dictionary is a list. The list contains all the timezones of that country.")
