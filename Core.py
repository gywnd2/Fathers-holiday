from icalendar import Calendar, Event, vCalAddress, vText
from datetime import date, datetime
import pytz, os

# 현재 날짜와 시간을 년, 월, 일과 시, 분, 초로 각각 분리
currDate = datetime.now().strftime("%Y-%m-%d")
splitDate = currDate.split("-")
currTime = datetime.now().strftime("%H:%M:%S")
splitTime = currTime.split(":"  )

# 캘린더 생성
cal = Calendar()
cal.add("prodid", "-// 반복일정 생성기 // 이효중 // leeexpert@cau.ac.kr //")
cal.add("version", "1.0")
calendar = cal

# 이벤트 리스트 생성
eventIndex=0
eventList = []

# 캘린더에 이벤트 생성, 십의 자리가 0인 경우 검사 (한 자릿수 날짜는 앞에 0이 붙을수 없음)
def addEvent(summaryText, startYear, yearStep, month, oneDigit, tenDigit, isZero):
    event=Event()
    event.add("summary", summaryText)

    if isZero == True:
        if oneDigit==0:
            pass

        else:
            event.allday = True
            event.add("dtstart", date(startYear + yearStep, month, oneDigit))

    else:
        event.allday = True
        event.add("dtstart", date(startYear + yearStep, month, int(str(tenDigit) + str(oneDigit))))

    event.add("dtstamp", datetime(int(splitDate[0]), int(splitDate[1]), int(splitDate[2]),
                                  int(splitTime[0]), int(splitTime[1]), int(splitTime[2]), tzinfo=pytz.utc))
    eventList.append(event)
    global eventIndex
    eventIndex+=1

# 윤년, 36일, 37일 등 범위 벗어난 날짜 검사
def isOver(dayStr, year, month):
    if year % 4 == 0:
        lastDay = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if int(dayStr) > lastDay[month - 1]:
            return True
        else:
            return False

    else:
        lastDay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if int(dayStr) > lastDay[month - 1]:
            return True
        else:
            return False

def doAction(oneDigit, startYear, endYear, summaryText, outputDir):

    # 종료년도 까지 while을 통해 반복
    currLoopYear = int(startYear)
    yearStep = 0

    while currLoopYear != int(endYear) + 1:
        for month in range(1, 13):
            for tenDigit in range(0, 4):
                dayStr = str(tenDigit) + str(oneDigit)
                print("%d년 %d월 %s일을 %d번째 이벤트로 추가합니다." % ((int(startYear) + yearStep), month, dayStr, eventIndex))
                if isOver(dayStr, int(startYear) + yearStep, month) == True:
                    print("break")
                    break
                elif isOver(dayStr, int(startYear) + yearStep, month) == False:
                    if tenDigit == 0:
                        print("isOver 통과")
                        addEvent(summaryText, int(startYear), yearStep, month, int(oneDigit), tenDigit, True)

                    elif tenDigit != 0:
                        print("isOver 통과")
                        addEvent(summaryText, int(startYear), yearStep, month, int(oneDigit), tenDigit, False)
        yearStep += 1
        currLoopYear += 1

    for index in range(0, eventIndex):
        calendar.add_component(eventList[index])

    f = open(os.path.join(outputDir, "MyCal.ics"), 'wb')
    f.write(calendar.to_ical())
    f.close()