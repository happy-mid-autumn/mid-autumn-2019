import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.dates as mdates
import numpy as np
import seaborn as sns 
from datetime import datetime   
from pylab import mpl
import re
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

def read_service_time(filename):
    file = open(filename,'r')
    lines = file.readlines()
    people = []
    baggage = []
    cost_time = {}
    cost_time_index = {}
    for i in range(len(lines)):
        if (i == 0):
            continue
        line = lines[i]
        line = line.strip('\n').strip().split(' ')
        if 'd' in line:
            line.remove('d')
        line = list(map(int,line))
        if (len(line) == 2):
            people.append(line[0])
            baggage.append(line[1])
        elif(len(line) == 3):
            people.append(line[0])
            baggage.append(line[1])
            if ((line[0],line[1]) in cost_time):
                cost_time[(line[0],line[1])].append(line[2])
            else:
                cost_time[(line[0],line[1])] = [line[2]]
        else:
            print(i,' line can not recognize')
            exit()
    return people,baggage,cost_time

def read_waiting_car(filename):
    file = open(filename,'r')
    lines = file.readlines()
    xs = []
    ys = []
    for i in range(len(lines)):
        a=re.split(r'[\(](.*?)[\)]',lines[i].strip('\n'))
        b=re.split('[, \'\"]+',a[1])
        data_time = b[1]+' '+b[2]
        xs.append(datetime.strptime(data_time,'%Y-%m-%d %H:%M:%S'))
        ys.append(int(b[3]))
    
    #plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d %H:%M:%S'))
    #plt.gca().xaxis.set_major_locator(mdates.DayLocator())

    plt.plot(xs, ys)
    mpl.rcParams['font.sans-serif'] = ['FangSong']
    plt.title("郑州市新郑机场出租车分布",fontsize=18)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.gcf().autofmt_xdate() 
    plt.show()

def get_flight(filename):
    sheet = pd.read_excel(filename)
    flight2type = {}
    for i in range(len(sheet)):
        f=open('flight1.txt','a')
        flight = sheet.ix[i].values[0]
        html = urlopen("https://zh.flightaware.com/live/flight/"+flight,timeout=10).read().decode('utf-8')
        result = re.findall('meta name\="aircrafttype" content\="(.*?)"',html)
        print(result)
        f.write(str(result))
        f.write('\n')
        result = None
        # soup = BeautifulSoup(html,features='lxml')
        # temp = soup.find_all(text=re.compile(r'"aircraft[a-zA-z]*"\:[\{]*"(.*?)"'))
        # result = []
        # result.append(re.findall(r'"aircraftType"\:"(.*?)"',str(temp)))
        # result.append(re.findall(r'"aircraftTypeFriendly"\:"(.*?)"',str(temp)))
        # result.append(re.findall(r'"friendlyType"\:"(.*?)"',str(temp)))
        # print(i)
        # flag = 0
        # for key in result:
        #     if(key!=[]):
        #         print(key)
        #         if(flag == 0):
        #             flight2type[i]=[key[0]]
        #             flag = 1
        #         else:
        #             flight2type[i].append(key[0])
        # if flag ==1:
        #     f.write(str(flight2type[i]))
        # f.write('\n')
        # f.close()
    return flight2type

def read_flight(filename):
    f = open(filename,'r')
    lines = f.readlines()
    types = []
    number = 0
    for i in range(len(lines)):
        line = lines[i]
        t = str(line).strip('\n')
        if t in types:
            continue
        else:
            types.append(t)
            number += 1
    return types,number
if __name__ == "__main__":
    people,baggage,cost_time=read_service_time('上车时间.txt')
    print(cost_time)
    plt.scatter(cost_time[(1,0)],[6]*len(cost_time[(1,0)]))

    #x=cost_time[(1,0)]
    #x.remove(166)
    #x=(x-np.mean(x))/np.std(x)
    #sns.set_palette("hls") 
    
    #sns.distplot(x,color="r",bins=20,kde=True)
    #plt.show()
    # read_waiting_car('../zhenzhou.txt')
    #read_flight('../郑州新郑.xlsx')
    types,number=read_flight('flight1.txt')
    print(types,number)
