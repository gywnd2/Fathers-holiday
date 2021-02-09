from icalendar import Calendar, Event, vCalAddress, vText
from datetime import datetime
import pytz
import tempfile, os

cal = Calendar()

cal.add("prodid", "-//My calendar product//mxm.dk//")
cal.add("version", "2.0")

#UTC시간 기준이므로 입력받은 시간에서 9시간 뒤로 뺴줘야 함
event=Event()
event.add("summary", "My first schedule made with python")
event.add("dtstart", datetime(2021,2,9,1,0,0, tzinfo=pytz.utc))
event.add("dtend", datetime(2021,2,15,1,0,0, tzinfo=pytz.utc))
event.add("dtstamp", datetime(2021,2,9,12,0,0, tzinfo=pytz.utc))

organizer=vCalAddress("MAILTO:leeexpert@cau.ac.kr")

cal.add_component(event)

directory="C:/Users/skarn/Documents/Github/Fathers-holiday"
f=open(os.path.join(directory, "MyCalendar.ics"), 'wb')
f.write(cal.to_ical())
f.close()