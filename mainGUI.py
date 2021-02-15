from datetime import date, datetime
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore
import Core, sys

form_class = uic.loadUiType("Main.ui")[0]

# 현재 날짜와 시간을 년, 월, 일과 시, 분, 초로 각각 분리
currDate=datetime.now().strftime("%Y-%m-%d")
splitDate=currDate.split("-")
currTime=datetime.now().strftime("%H:%M:%S")
splitTime=currTime.split(":")

class main(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Father's Holiday")
        self.setFixedSize(622, 636)
        self.initCore()
        self.statusBar().showMessage("오늘은 : "+splitDate[0]+"년 "+splitDate[1]+"월 "+splitDate[2]+"일")

        self.startYearSpinBox.setRange(int(splitDate[0]), 2500)
        self.startYearSpinBox.setValue(int(splitDate[0]))
        self.endYearSpinBox.setRange(int(splitDate[0]), 2500)
        self.endYearSpinBox.setValue(int(splitDate[0]))
        self.startYearSpinBox.valueChanged.connect(self.startYearChanged)
        self.endYearSpinBox.valueChanged.connect(self.endYearChanged)
        self.repeatNumSpinBox.valueChanged.connect(self.repeatNumChanged)

        self.dirSelectButton.installEventFilter(self)
        self.letsGetit.installEventFilter(self)
        self.dirSelectButton.clicked.connect(self.selectDir)
        self.letsGetit.clicked.connect(self.run)

    def eventFilter(self, obj, event):
        if obj == self.dirSelectButton and event.type() == QtCore.QEvent.HoverEnter:
            self.statusBar().showMessage("경로를 선택합니다.")
        elif obj == self.dirSelectButton and event.type() == QtCore.QEvent.HoverLeave:
            self.statusBar().showMessage("오늘은 : "+splitDate[0]+"년 "+splitDate[1]+"월 "+splitDate[2]+"일")
        elif obj == self.letsGetit and event.type() == QtCore.QEvent.HoverEnter:
            self.statusBar().showMessage("Let's Get it!")
        elif obj == self.letsGetit and event.type() == QtCore.QEvent.HoverLeave:
            self.statusBar().showMessage("오늘은 : "+splitDate[0]+"년 "+splitDate[1]+"월 "+splitDate[2]+"일")
        return super(main, self).eventFilter(obj,event)

    def initCore(self):
        Core.startYear = self.startYearSpinBox.value()
        Core.endYear = self.endYearSpinBox.value()
        Core.summaryText = self.description
        Core.oneDigit=0
        Core.outputDir=""
        Core.summaryText=""

    def selectDir(self):
        dirStr = QFileDialog.getExistingDirectory(self, "경로 선택", "./")

        if dirStr:
            self.dirText.setText(dirStr)
            Core.outputDir = dirStr

    def startYearChanged(self):
        Core.startYear = self.startYearSpinBox.value()

    def endYearChanged(self):
        Core.endYear = self.endYearSpinBoxSpinBox.value()

    def repeatNumChanged(self):
        Core.oneDigit = self.repeatNumSpinBox.value()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "종료", "프로그램을 종료하시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def run(self):
        if Core.outputDir=="":
            notice=QMessageBox.information(self, "경고", "경로를 선택하십시오.")
        else:
            Core.summaryText=self.description
            Core.settingTime()
            Core.makeCalendar()
            Core.doAction(Core.oneDigit, Core.eventIndex)

if __name__=="__main__":
    app=QApplication(sys.argv)
    mainGUI=main()
    mainGUI.show()
    app.exec_()