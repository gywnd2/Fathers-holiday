from icalendar import Calendar, Event, vCalAddress, vText
from datetime import datetime
import pytz
import tempfile, os

# 시작/종료 연도와 반복할 날짜(일의 자리), 일정이름 입력
startYear=input("시작연도를 입력하세요. ex)2021\n: ")
endYear=input("종료연도를 입력하세요. ex)2100\n: ")
summaryText=input("일정 이름을 입력하세요.\n: ")
oneDigit=input("몇으로 끝나는 날짜마다 반복할까요?\n: ")

# 현재 날짜와 시간을 년, 월, 일과 시, 분, 초로 각각 분리
currDate=datetime.datetime.now().strftime("%Y-%m-%d")
splitDate=currDate.split("-")
currTime=datetime.datetime.now().strftime("%H:%M:%S")
splitTime=currTime.split(":")

cal=Calendar()
cal.add("prodid", "반복일정 생성기 (leeexpert@cau.ac.kr)")
cal.add("version", "1.0")

def addEvent(sumTxt, stYr, yrSt, mnt, oneDgt, )

for yearStep in range(0, splitDate[0]+1-startYear)
    for month in range(1, 13)
        for tenDigit in range(0, 4)
            dayStr=tenDigit+oneDigit

            if tenDigit=="0":
                event = Event()
                event.add("summary", summaryText)
                event.add("dtstart", datetime(startYear+i, month, oneDigit, 1, 0, 0, tzinfo=pytz.utc))
                event.add("dtend", datetime(startYear+i, month, oneDigit, 1, 0, 0, tzinfo=pytz.utc))
                # UTC => 서울 시간 보정 필요
                event.add("dtstamp", datetime(currDate[0], currDate[1], currDate[2], currTime[0], currTime[1], currTime[2]))

            elif tenDigit!="0":
                event=Event()
                event.add("summary", summaryText)
                event.add("dtstart", datetime(startYear+i, month, tenDigit+oneDigit, 1, 0, 0, tzinfo=utc))
                event.add("dtend", datetime(startYear+i, month, tenDigit+oneDigit, 1, 0, 0, tzinfo=utc))
                event.add("dtstamp", datetime(currDate[0], currDate[1], currDate[2], currTime[0], currTime[1], currTime[2]))

            elif month=="int(tenDigit+oneDigit)>