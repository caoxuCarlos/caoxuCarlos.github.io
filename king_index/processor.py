import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
from PIL import Image

df = pd.read_excel('data/成交量占比指标.xls')

num = df.shape[1]-2
table_as_array = np.zeros((num,4))
table = pd.DataFrame(table_as_array)
table.columns = ['日期', '前5%成交量(股)', '总成交量(股)', '指标']

df.columns[2]
for i in range(num):
    rolling_row_name = df.columns[i+2]
    df1 = df.filter([df.columns[0],df.columns[1],rolling_row_name], axis=1)
    df1 = df1[pd.to_numeric(df[rolling_row_name], errors='coerce').notnull()]
    df1 = df1.sort_values(by=[rolling_row_name],ascending=False)

    five_percent = int(df1.shape[0]*0.05)
    volumn_five_percent = 0
    volumn_all = 0
    for j in range(five_percent):
        volumn_five_percent += df1.iloc[j,2]
    df.shape[0]
    for k in range(df1.shape[0]):
        volumn_all += df1.iloc[k,2]
    volumn_index_on_that_day = volumn_five_percent/volumn_all
    the_date = re.findall(r'\d\d\d\d-\d\d-\d\d',rolling_row_name)[0]
    table.iloc[i,0] = the_date
    table.iloc[i,1] = volumn_five_percent
    table.iloc[i,2] = volumn_all
    table.iloc[i,3] = volumn_index_on_that_day

table.to_excel(r'./output/index.xlsx', index = False)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(table[table.columns[0]],table[table.columns[3]] ,',-',color='#363642',linewidth='3')
# more linestyles: https://matplotlib.org/2.0.2/api/lines_api.html#matplotlib.lines.Line2D.set_linestyle
ax.set_xlabel(u"Date",fontsize=10)
plt.xticks(rotation = 45)
ax.set_ylabel(u"Top 5% Volumn / All Volumn")
# ax.set_title('Index')
ax.set_facecolor('#F0EFEC')
# ax.set_ylim((0.3, 0.5))
ax.grid(True,which='both',axis='both',color='#D6D1D0', linestyle='-', linewidth=2)
fig.set_facecolor('#F0EFEC')
# fig.savefig('./output/king_index_raw.png', dpi=200, pad_inches=10, bbox_inches='tight')
fig.savefig('./output/king_index_raw.png', dpi=300, bbox_inches='tight', pad_inches=1)
fig.show()

img = Image.open( 'output/king_index_raw.png', 'r')
img_w, img_h = img.size
background = Image.new('RGB', (3000, 2000), (240, 239, 236))
bg_w, bg_h = background.size
offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2 )
# offset = ((bg_w - img_w) // 2, 0)
background.paste(img, offset)
background.save('./output/king_index_1.png')