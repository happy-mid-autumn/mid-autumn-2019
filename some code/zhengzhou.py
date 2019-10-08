from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import sched, time
s = sched.scheduler(time.time, time.sleep)
PATTERN1 = re.compile(r'\d{4}-\d{2}-\d{2}')
PATTERN2 = re.compile(r'\d{2}:\d{2}:\d{2}')
PATTERN3 = re.compile(r'\d{0,4}')
PATTERN4 = re.compile(r'：')
def getvalue():
    fw = open('zhenzhou.txt','a')
    html = urlopen("http://www.whalebj.com/xzjc/default.aspx").read().decode('utf-8')
    soup = BeautifulSoup(html,features='lxml')
    span = soup.find('span',attrs={"class":"content_Case"}).getText()
    date = PATTERN1.search(span).group(0)
    time = PATTERN2.search(span).group(0)
    temp = PATTERN4.split(span)
    total = PATTERN3.search(temp[1]).group(0)
    drivein = PATTERN3.search(temp[2]).group(0)
    driveout = PATTERN3.search(temp[3]).group(0)
    print(date,time,total,drivein,driveout)
    fw.write(str((date,time,total,drivein,driveout))+'\n')
    s.enter(60, 1, getvalue)
    fw.close()


s.enter(60, 1, getvalue)
s.run()

