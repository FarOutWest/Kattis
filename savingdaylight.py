import sys, datetime
months = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6,
          'July':7, 'August':8, 'September':9, 'October':10, 'November':11,
          'December':12}
for line in sys.stdin:
    line = line.strip().split()
    mon, day, year, t1, t2 = line[0], int(line[1]), int(line[2]), line[3], line[4]
    t1, t2 = t1.strip().split(':'), t2.strip().split(':')
    h1, m1, h2, m2 = int(t1[0]), int(t1[1]), int(t2[0]), int(t2[1])
    month = months[mon]
    dt1 = datetime.datetime(year, month, day, h1, m1)
    dt2 = datetime.datetime(year, month, day, h2, m2)
    ans = (dt2 - dt1)
    ans = str(ans).split(':')
    minans = ans[1]
    if int(minans) < 10: minans = minans[-1:]
    print(str(mon) + ' ' + str(day) + ' ' + str(year) + ' ' + ans[0] + ' hours ' + minans + ' minutes')
