from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore
from datetime import date, datetime
import pytz, sys, Core

form_class = uic.loadUiType("Main.ui")[0]

class main(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Father's Holiday 1.0")
        self.setFixedSize(622, 636)
        self.initEnv()
        self.statusBar().showMessage("오늘은 : "+self.splitDate[0]+"년 "+self.splitDate[1]+"월 "+self.splitDate[2]+"일")

        self.startYearSpinBox.setRange(int(self.splitDate[0]), 2500)
        self.startYearSpinBox.setValue(int(self.splitDate[0]))
        self.endYearSpinBox.setRange(int(self.splitDate[0]), 2500)
        self.endYearSpinBox.setValue(int(self.splitDate[0]))
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
            self.statusBar().showMessage("오늘은 : "+self.splitDate[0]+"년 "+self.splitDate[1]+"월 "+self.splitDate[2]+"일")
        elif obj == self.letsGetit and event.type() == QtCore.QEvent.HoverEnter:
            self.statusBar().showMessage("Let's Get it!")
        elif obj == self.letsGetit and event.type() == QtCore.QEvent.HoverLeave:
            self.statusBar().showMessage("오늘은 : "+self.splitDate[0]+"년 "+self.splitDate[1]+"월 "+self.splitDate[2]+"일")
        return super(main, self).eventFilter(obj,event)

    def initEnv(self):
        # 현재 날짜와 시간을 년, 월, 일과 시, 분, 초로 각각 분리
        self.currDate = datetime.now().strftime("%Y-%m-%d")
        self.splitDate = self.currDate.split("-")
        self.currTime = datetime.now().strftime("%H:%M:%S")
        self.splitTime = self.currTime.split(":")

        self.startYear = self.splitDate[0]
        self.endYear = self.splitDate[0]
        self.outputDir=""
        self.summaryText=""
        self.oneDigit=self.repeatNumSpinBox.value()
        self.fileName=""

    def selectDir(self):
        dirStr = QFileDialog.getExistingDirectory(self, "경로 선택", "./")

        if dirStr:
            self.dirText.setText(dirStr)
            self.outputDir = dirStr

    def startYearChanged(self):
        self.startYear = self.startYearSpinBox.value() #QSpinBox의 value는 int

    def endYearChanged(self):
        self.endYear = self.endYearSpinBox.value()

    def repeatNumChanged(self):
        self.oneDigit = self.repeatNumSpinBox.value()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "종료", "프로그램을 종료하시겠습니까?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def run(self):
        if self.outputDir=="":
            notice=QMessageBox.information(self, "경고", "경로를 선택하십시오.")
        else:
            self.summaryText=self.description.text()
            self.fileName = self.fileNameEdit.text()
            Core.doAction(self.oneDigit, self.startYear,
                          self.endYear, self.summaryText, self.outputDir, self.fileName)

if __name__=="__main__":
    app=QApplication(sys.argv)
    mainGUI=main()
    mainGUI.show()
    app.exec_()