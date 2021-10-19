from os import stat
import pandas as pd
import plotly.figure_factory as ff
df = pd.read_csv('data.csv')
avg = df['temp'].tolist()
fig = ff.create_distplot([avg],['avg'],show_hist=False)
#fig.show()
import random
import statistics
meanlist = []
for i in range(0,1000):
    data = []
    for h in range(0,100):
        idx = random.randint(0,len(avg)-1)
        value = avg[idx]
        data.append(value)
    mean = statistics.mean(data)
    meanlist.append(mean)
fig2 = ff.create_distplot([meanlist],['avg'],show_hist=False)
fig2.show()
pm = statistics.mean(avg)
sm = statistics.mean(meanlist)
print(pm)
print(sm)
ps = statistics.stdev(avg)
ss = statistics.stdev(meanlist)
print(ps)
print(ss)