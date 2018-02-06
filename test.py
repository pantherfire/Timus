from __future__ import print_function
import cx_Oracle
import tushare as ts  
import matplotlib.pyplot as plt  
import matplotlib.finance as mpf 
from matplotlib.pylab import date2num
from matplotlib import pyplot as plt     
from matplotlib import animation 
import datetime
#%matplotlib inline

def date_to_num(dates):
    num_time = []
    for date in dates:
        date_time = datetime.datetime.strptime(date,'%Y-%m-%d')
        num_date = date2num(date_time)
        num_time.append(num_date)
    return num_time



tns=cx_Oracle.makedsn('10.100.19.67',1521,'testdb')
#tns=cx_Oracle.makedsn('47.96.0.26',1521,'thdb')
db=cx_Oracle.connect('g','g',tns)

cursor = db.cursor()
cursor.execute("""select lo,cp from PLATFORMTH_TD_RAW_DAY where rownum <= 3""")
print(cursor)
for lo, cp in cursor:
    print("Values:", lo, cp)

#db.close()

wdyx = ts.get_k_data('002739','2017-01-01')
wdyx.info()
wdyx[:3]

mat_wdyx = wdyx.as_matrix()
num_time = date_to_num(mat_wdyx[:,0])
mat_wdyx[:,0] = num_time
mat_wdyx[:3]

print(str(wdyx))
print(str(mat_wdyx))


fig, ax = plt.subplots(figsize=(15,5))
fig.subplots_adjust(bottom=0.5)
mpf.candlestick_ochl(ax, mat_wdyx, width=0.6, colorup='g', colordown='r', alpha=1.0)


plt.xticks(rotation=30)
plt.title('wanda yuanxian 17')
plt.xlabel('Date')
plt.ylabel('Price')
ax.xaxis_date ()
plt.grid(True)
ax.autoscale_view()
plt.show()
