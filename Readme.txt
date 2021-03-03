21.03.03 드디어 1.0버전 완성!

입력한 날짜의 뒷자리 수 마다 반복되는 일정을 파일로
출력하는 프로그램
PyQt5와 iCalendar 패키지를 사용

달력에서 반복 시작 연도와 종료 연도를 선택하고
입력된 수(일의 자리)로 끝나는 일 마다 이벤트로 추가한
캘린더를 ICS 파일로 출력

pyinstaller --onefile --add-data="Main.ui;." --clean --windowed mainGUI.py