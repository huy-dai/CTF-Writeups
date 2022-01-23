from datetime import date, timedelta
import pandas 

sdate = date(1900,1,1) #start date
edate = date(2050,1,1) #end date

dates = pandas.date_range(sdate,edate-timedelta(days=1),freq='d')
#print(dates)

date_lst = dates.strftime("%Y%m%d").tolist()

with open("bdays.txt","w+") as f:
    for date in date_lst:
        f.write("%s\n" % date)

