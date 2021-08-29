#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import regex as re
from PIL import Image
#%%
df = pd.read_excel("data/pe/医药/average_pe_method.xlsx",engine='openpyxl')
df = df.iloc[:,:5]
df.columns = df.iloc[3,:5]
df = df.iloc[4:,:]

interval = (df["pe"].max()-df["pe"].min())/4

df["upper_most"] = df["pe"].max()
df["lower_most"] = df["pe"].min()
df["upper"] = df["pe"].max() - interval
df["lower"] = df["pe"].min() + interval
df["mid"] = (df["pe"].min()+df["pe"].max())/2
#%%
fig = plt.figure(figsize=(12,6),dpi=200)
ax = fig.add_subplot(111)

# float one sigma
ax.plot(df["date"],df[df.columns[2]],
        '-.',color='#B88D4C',linewidth='1')
ax.plot(df["date"],df[df.columns[3]],
        '-.',color='#B88D4C',linewidth='1')
ax.plot(df["date"],df[df.columns[4]],
        '-.',color='#B88D4C',linewidth='1')

# band lines
ax.plot(df["date"],df["upper_most"],
        "-",color='#487049',linewidth='2',
        label=str(round(df["pe"].max(),2)))

ax.plot(df["date"],df["upper"],
        "-",color='#E58133',linewidth='2',
        label=str(round(df["pe"].max() - interval,2)))

ax.plot(df["date"],df["mid"],
        "-",color='#AC3018',linewidth='2',
        label=str(round((df["pe"].min()+df["pe"].max())/2,2)))

ax.plot(df["date"],df["lower"],
        "-",color='#233279',linewidth='2',
        label=str(round(df["pe"].min() + interval,2)))

ax.plot(df["date"],df["lower_most"],
        "-",color='#807750',linewidth='2',
        label=str(round(df["pe"].min(),2)))

# pe line
ax.plot(df["date"],df[df.columns[1]],
        '-',color='#363642',linewidth='2')

ax.set_xlabel(u"Date",fontsize=8)
ax.set_ylabel(u"PE",fontsize=8)
latest_date = str(df.iloc[df.shape[0]-1,0])
ptn=r'\d\d\d\d-\d\d\-\d\d'
latest_date =re.findall(ptn,latest_date)[0]
ax.set_title('The latest data is from: ' + latest_date, fontsize=8)

loc_base = int(df.shape[0]/12)
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
ax.legend(loc='upper right',facecolor='#F0EFEC',edgecolor='#716F6E',fontsize='10')
fig.savefig('output/pe/medical_raw.png', dpi=300, bbox_inches='tight', pad_inches=1)

img = Image.open( 'output/pe/medical_raw.png', 'r')
img_w, img_h = img.size
background = Image.new('RGB', (5000, 2500), (240, 239, 236))
bg_w, bg_h = background.size
offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2 )
# offset = ((bg_w - img_w) // 2, 0)
background.paste(img, offset)
background.save('./output/pe/medical.png')
plt.show()