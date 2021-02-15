from icalendar import Calendar, Event, vCalAddress, vText
from datetime import date, datetime
import pytz
import tempfile, os

if __name__=="__main__":
    # 시작/종료 연도와 반복할 날짜(일의 자리), 일정이름 입력
    global startYear
    global endYear
    global summaryText
    global oneDigit
    global outputDir
    global eventIndex
    global eventList
    global cal

    def settingTime():
        # 현재 날짜와 시간을 년, 월, 일과 시, 분, 초로 각각 분리
        currDate = datetime.now().strftime("%Y-%m-%d")
        splitDate = currDate.split("-")
        currTime = datetime.now().strftime("%H:%M:%S")
        splitTime = currTime.split(":")

    def makeCalendar():
        # 캘린더 생성
        cal = Calendar()
        cal.add("prodid", "-// 반복일정 생성기 // 이효중 // leeexpert@cau.ac.kr //")
        cal.add("version", "1.0")
        # 이벤트 리스트 생성
        eventList = []
        eventIndex = 0


    # 캘린더에 이벤트 생성, 십의 자리가 0인 경우 검사 (한 자릿수 날짜는 앞에 0이 붙을수 없음)
    def addEvent(sumTxt, stYr, yrSt, mnt, oneDgt, tenDgt, isZero, index):
        eventList.append(Event())
        print("%d개 째 이벤트를 추가합니다." % eventIndex)
        eventList[index].add("summary", sumTxt)

        if isZero == True:
            eventList[index].allday = True
            eventList[index].add("dtstart", date(stYr + yrSt, mnt, oneDgt))

        else:
            eventList[index].allday = True
            eventList[index].add("dtstart", date(stYr + yrSt, mnt, int(str(tenDgt) + str(oneDgt))))

        eventList[index].add("dtstamp",
                             datetime(int(splitDate[0]), int(splitDate[1]), int(splitDate[2]), int(splitTime[0]),
                                      int(splitTime[1]), int(splitTime[2]), tzinfo=pytz.utc))


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

def doAction(oneDigit, eventIndex):

    # 종료년도 까지 while을 통해 반복
    loopYear = int(startYear)
    yearStep = 0

    while loopYear != int(endYear) + 1:
        for month in range(1, 13):
            for tenDigit in range(0, 4):
                dayStr = str(tenDigit) + oneDigit
                print("%d년 %d월 %s일을 %d번째 이벤트로 추가합니다." % ((int(startYear) + yearStep), month, dayStr, eventIndex))
                if isOver(dayStr, int(startYear) + yearStep, month) == True:
                    break
                elif isOver(dayStr, int(startYear) + yearStep, month) == False:

                    if tenDigit == "0":
                        addEvent(summaryText, int(startYear), yearStep, month, int(oneDigit), tenDigit, True,
                                 eventIndex)

                    elif tenDigit != "0":
                        addEvent(summaryText, int(startYear), yearStep, month, int(oneDigit), tenDigit, False,
                                 eventIndex)

                eventIndex += 1
        yearStep += 1
        loopYear += 1

    for index in range(0, eventIndex):
        cal.add_component(eventList[index])

    f = open(os.path.join(outputDir, "MyCal.ics"), 'wb')
    f.write(cal.to_ical())
    f.close()