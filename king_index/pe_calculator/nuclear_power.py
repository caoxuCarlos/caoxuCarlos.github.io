import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import regex as re
from PIL import Image

c_name = "核电"
e_name = "nuclear_power"

original_data_path ="../data/pe/"+c_name+"/"+e_name+".xlsx"
output_data_path ="../output/pe/"+e_name+"_pe_original_data.xlsx"
y_label = e_name.capitalize()+" PE"
raw_path = "../output/pe/raw/"+e_name+"_raw.png"
img_path = "../output/pe/"+e_name+".png"
finished_noitce =e_name.capitalize()+" data processed."

#REPLACEMENT 1
df = pd.read_excel(original_data_path,engine='openpyxl')
#REPLACEMENT 2
df.to_excel(output_data_path)

df = df.iloc[:,:5]
df.columns = df.iloc[3,:5]
df = df.iloc[4:,:]

interval = (df["pe"].max()-df["pe"].min())/4

df["upper_most"] = df["pe"].max()
df["lower_most"] = df["pe"].min()
df["upper"] = df["pe"].max() - interval
df["lower"] = df["pe"].min() + interval
df["mid"] = (df["pe"].min()+df["pe"].max())/2
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

#REPLACEMENT 3
ax.set_ylabel(y_label,fontsize=8)
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
#REPLACEMENT 4
fig.savefig(raw_path, dpi=300, bbox_inches='tight', pad_inches=1)
#REPLACEMENT 5
img = Image.open(raw_path, 'r')
img_w, img_h = img.size
background = Image.new('RGB', (5000, 2500), (240, 239, 236))
bg_w, bg_h = background.size
offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2 )
# offset = ((bg_w - img_w) // 2, 0)
background.paste(img, offset)
#REPLACEMENT 6
background.save(img_path)
#REPLACEMENT 7
print(finished_noitce)
# plt.show()
