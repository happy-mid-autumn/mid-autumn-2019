# Input
# 一天内航班的安排（包括时间、载客量等）
# 给定某个(wait_cars,time) 本程序将模拟出下面进行的情形
# 计算出司机去或留的收入期望
import matplotlib.pyplot as plt
from bisect import bisect_right
import random
from datetime import datetime,timedelta,date
import pandas as pd
import re
import numpy as np
import collections
from read_data import read_service_time
import seaborn as sns
type2capacity = {'B738':189,'B737':168,'B732':136,'B739':215,'B733':149,'B736':132,\
        'B789':360,'B788':310,'A320':164,'A321':199,'A333':335,'A330':293,'MA6':56,\
        'E190':114,'CRJ9':90,'A319':142}
class driver(object):
    def __init__(self,wait_cars,time_width,time,average_price):
        self.wait_cars = wait_cars
        self.time_width = time_width
        self.time = time
        self.average_price = average_price
    def decide(self,cost_time):
        pass

class plane(object):
    def __init__(self,arr_time,plane_type):
        self.arr_time = arr_time 
        self.plane_type = plane_type
        self.capacity =  type2capacity[plane_type]


class simulate(object):
        def __init__(self,driver,flight_list,people_prob,baggage_prob,service_time_prob):
            self.time = driver.time
            self.wait_cars = driver.wait_cars
            self.time_width = driver.time_width
            self.flight_list = flight_list
            self.people_prob = people_prob
            self.baggage_prob = baggage_prob
            self.service_time_prob = service_time_prob
        
        def preprocess(self):
            #sorted(self.flight_list,key=lambda flight: flight.arr_time)
            self.start_point = next(x[0] for x in enumerate(self.flight_list) if x[1].arr_time >= self.time)
            j = self.start_point
            num = 0
            self.start_time = self.time
            while(self.flight_list[j].arr_time<self.start_time+self.time_width):
                num += 1
                j += 1
                if(j == len(self.flight_list)):
                    self.start_time -= timedelta(days=1)
                    self.time -= timedelta(days=1)
                    j = next(x[0] for x in enumerate(self.flight_list) if x[1].arr_time >= self.time)
            self.wait_people = 0
            return num

        def flight_check(self):
            while(self.time>=flight_list[self.start_point].arr_time):
                self.wait_people += int(flight_list[self.start_point].capacity*0.80*0.1) # different plane has not concern
                self.start_point += 1
                if(self.start_point == len(self.flight_list)-1):
                    self.start_time -= timedelta(days=1)
                    self.time -= timedelta(days=1)
                    self.start_point = next(x[0] for x in enumerate(self.flight_list) if x[1].arr_time >= self.time)
        
        def taxi_arrive(self):
            customers = np.random.choice(np.arange(1, 5),p=self.people_prob)
            customers = min(self.wait_people,customers)
            self.wait_people -= customers
            self.wait_cars -= 1
            baggage = np.random.choice(np.arange(0, 2),p=self.baggage_prob)
            if (customers,baggage) not in self.service_time_prob:
                baggage += 1;
            mean,stdt = self.service_time_prob[(customers,baggage)]
            sevice_time = timedelta(seconds=max(int(np.random.normal(mean,stdt)),10))
            self.time += sevice_time
            

        def start(self):
            time = self.time
            while(self.wait_cars>0):
                if(self.wait_people>0):
                    self.taxi_arrive()
                    self.flight_check()
                else:
                    self.time = flight_list[self.start_point].arr_time
                    self.flight_check()
            self.cost_time = self.time - self.start_time
            return self.cost_time

if __name__ == "__main__":
    sheet = pd.read_excel('郑州新郑.xlsx')
    #generate flight list
    flight_list = []
    for i in range(len(sheet)):
        arrive_time = sheet.ix[i].values[4]
        arrive_time = datetime.combine(date(2019,9,14),arrive_time)
        plane_type = sheet.ix[i].values[5]
        flight = plane(arrive_time,plane_type)
        flight_list.append(flight)
    flight_list=sorted(flight_list,key=lambda flight: flight.arr_time)

    #get probability distribution
    people,baggage,service_time=read_service_time('上车时间.txt')
    counter = collections.Counter(people)
    people_prob = []
    for i in range(4):
        people_prob.append(counter[i+1]/len(people))
    counter = collections.Counter(baggage)
    baggage_prob = []
    for j in range(2):
        baggage_prob.append(counter[j]/len(people))    
    service_time_prob = {}
    for key,value in service_time.items():
        mean = np.mean(value)
        stdt = np.std(value)
        service_time_prob[key] = (mean,stdt)
    f = open('zhenzhou1.txt','r')
    lines = f.readlines()
    repeat_time = 250
    cost_times = []
    for j in range(repeat_time):
        num = random.randint(0,len(lines)-1)
        a=re.split(r'[\(](.*?)[\)]',lines[num].strip('\n'))
        b=re.split('[, \'\"]+',a[1])
        date_time = b[1]+' '+b[2]
        waiting = int(b[3])+int(np.random.normal(60,20))
        date_time = datetime.strptime(date_time,'%Y-%m-%d %H:%M:%S')
        if date_time.day == 13 :
            date_time += timedelta(days=1)
        print(date_time,waiting)
        time_width = timedelta(hours=2)
        dr = driver(waiting,time_width,date_time,average_price=50)
        si = simulate(dr,flight_list,people_prob,baggage_prob,service_time_prob)
        num = si.preprocess()
        cost_time = si.start()
        print(cost_time)
        cost_times.append(cost_time)
        #get dataset
        f = open('datasets.txt','a')
        dataset = (waiting,num,cost_time.seconds//60)      
        f.write(str(dataset))
        f.write('\n')
        f.close()










