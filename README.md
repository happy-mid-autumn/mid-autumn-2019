## 问题C 机场的出租车问题

#### 数据
- 预计获得的数据
  - 合肥新桥机场
    - (1)(2)
      - 出租车平均等候时间
      - 平均收入与机场载客的收益、can refer to the data online
      - 司机对航班情况的熟悉程度
      - 等候区空人概率 the high time and the low time
      - 其他影响乘客数量的不确定因素（一辆车坐几人等）and the possibility
      - the time the pessenger need to get in a car and the distribution（the time the later car arrive minus the time the former car arrive）
      - （N、t）fit
      - the possibility of the airflight be late and the distribution
    - (3)
      - 出租车乘坐区的规划
      - the photo and the map
      - the arriving rate of the passengers
      - the delay of a car
      - the rate of the pessengers with a suitcase
    - (4)
    
  - 网络
    - 航班达到数据集
    - 候车处人数随时间变化关系

#### 解题方案
- (1)(2)
  1. 通过网络和实地考察收集间接数据
  2. 利用间接数据，通过模拟的方法构造数据集({N,t} -> y)
  3. 用数据集-training训练logistic二分函数(y = a1*g(x1) + a2*x2 + b)，给出出租车司机的决策方案
  4. 利用数据集-test评估方案的合理性
- (3)
  1. 采用多服务台排队模型
  2. 旅客的服务时间与其类型有关（散客，多人2, 3, 4）, 同时满足一定分布的随机性
  3. 当旅客数目不足时（n<k），只放入n辆车
  4. 进入上车点区域车速减慢(防止出现安全问题)
  5. 增大服务车辆的等待参数(显著降低车速，考虑前车的跟车距离)
  6. 对旅客的方案做多种方案讨论，对k值做连续的优化
- (4)
  1. 确立k级优先级
  2. 建立载客距离长短与收益水平（横向比较）的关系，并由此确定该车具有几级优先级
  3. 增加aging机制预防饥饿问题
