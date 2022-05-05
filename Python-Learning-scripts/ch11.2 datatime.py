# codingf=utf-8

import datetime

d=datetime.datetime(2022,2,28)
d=datetime.datetime(2022,2,30) #outof datetime range
d=datetime.datetime(2022,2,12,23,30,00)

# datetime function
datetime.datetime.today()
datetime.datetime.now()
datetime.datetime.fromtimestamp(999999999.999)

# date function
d=datetime.date(2022,2,12)

# time function
t=datetime.time(23,59,58,1999)


#%% ch11.2.4 计算时间跨度类  timedelta
d=datetime.date.today()
delta=datetime.timedelta(10)
d+=delta


delta=datetime.timedelta(weeks=1)
d-=delta







