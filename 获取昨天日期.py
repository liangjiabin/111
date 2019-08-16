import datetime
def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today-oneday
    return yesterday

print('今天的日期是：{}'.format(datetime.date.today()))
print('昨天的日期是：',getYesterday())