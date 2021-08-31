import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
from PIL import Image
import matplotlib.ticker as plticker
import time

t0 = time.time()
df = pd.read_excel('data/成交量占比指标v2.xls')
# The number of days is the columns of the df minus 2.
# One is id, another is name.
num = df.shape[1]-2
# Need to reorganize data.
# Each trade day count a row.
table_as_array = np.zeros((num,5))
table = pd.DataFrame(table_as_array)
table.columns = ['日期', '前5%成交量(股)', '总成交量(股)', '指标','id']

pd.to_numeric(df.columns[2], errors='coerce')

for i in range(num):
    rolling_row_name = df.columns[i+2]
    # df1 is a temporary dataframe, only to calcute the indicator for each day.
    df1 = df.filter([df.columns[0],df.columns[1],rolling_row_name], axis=1)
    df1 = df1[pd.to_numeric(df[rolling_row_name], errors='coerce').notnull()]
    df1 = df1.sort_values(by=[rolling_row_name],ascending=False)

    five_percent = int(df1.shape[0]*0.05)
    volumn_five_percent = 0
    volumn_all = 0
    for j in range(five_percent):
        volumn_five_percent += df1.iloc[j,2]
    for k in range(df1.shape[0]):
        volumn_all += df1.iloc[k,2]
    volumn_index_on_that_day = volumn_five_percent/volumn_all

    the_date = re.findall(r'\d\d\d\d-\d\d-\d\d',str(rolling_row_name))[0]
    table.iloc[i,0] = the_date
    table.iloc[i,1] = volumn_five_percent
    table.iloc[i,2] = volumn_all
    table.iloc[i,3] = volumn_index_on_that_day
    table.iloc[i,4] = i + 1
    if(i%10==0): print("{0:0.1f}%".format((i/num)*100))


table.to_excel(r'./output/index.xlsx', index = False)
t1 = time.time()

#%%
fig = plt.figure(figsize=(12, 6), dpi=200)
ax = fig.add_subplot(111)
ax.plot(table[table.columns[0]],table[table.columns[3]] ,',-',color='#363642',linewidth='2')

ax.set_xlabel(u"Date",fontsize=8)
ax.set_ylabel(u"Top 5% Volumn / All Volumn",fontsize=8)
latest_date = table.iloc[num-1][0]
ax.set_title('The latest data is from: ' + latest_date, fontsize=8)

loc_base = int(num/12)
loc = plticker.MultipleLocator(base=loc_base) # this locator puts ticks at regular intervals
ax.xaxis.set_major_locator(loc)

plt.xticks(rotation = 45)
ax.tick_params(which='both', width=1.15)
ax.tick_params(which='major', length=4)
ax.tick_params(which='minor', length=2, color='k')
ax.tick_params(axis='x',which='major',labelsize='7')
ax.tick_params(axis='y',which='major',labelsize='8')

fig.set_facecolor('#F0EFEC')
ax.set_facecolor('#F0EFEC')
ax.grid(True,which='both',axis='both',color='#D6D1D0', linestyle='-', linewidth=1)
fig.savefig('./output/king_index_raw.png', dpi=300, bbox_inches='tight', pad_inches=1)
fig.show()

img = Image.open( 'output/king_index_raw.png', 'r')
img_w, img_h = img.size
background = Image.new('RGB', (5000, 2500), (240, 239, 236))
bg_w, bg_h = background.size
offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2 )
# offset = ((bg_w - img_w) // 2, 0)
background.paste(img, offset)
background.save('./output/king_index_1.png')
t2 = time.time()

print("Data Processing: ", t1-t0)
print("Plotting: ",t2-t2)
