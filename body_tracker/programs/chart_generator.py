import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from PIL import Image
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))
data_loc = cwd + "/cx_body_data.csv"
pic_loc = cwd + "/../pictures/"
df = pd.read_csv(data_loc)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.set_xlabel("Day")
ax1.set_ylabel("Weight", color='#610006')
ax1.grid(True, which='both', axis='both', color='#D6D1D0', linestyle='-', linewidth=1)
ax1.plot(df["day_num"], df["weight"], color='#610006', linewidth='3')
ax1.set_facecolor('#F0EFEC')
ax1.set_ylim((65, 73))
ax1.tick_params(axis='y', labelcolor='#610006')

ax2 = ax1.twinx()
ax2.set_xlabel("Day")
ax2.set_ylabel('Relative Body-fat Ratio', color='#363642')
ax2.plot(df["day_num"], df["delta_of_bf_ratio"], color='#363642', linewidth='3')
ax2.yaxis.set_major_formatter(mtick.PercentFormatter())
ax2.set_facecolor('#F0EFEC')
ax2.set_ylim((-6, 2))
ax2.tick_params(axis='y', labelcolor='#363642')

fig1.set_facecolor('#F0EFEC')
fig1.savefig(pic_loc + 'cx_0.png', dpi=200, bbox_inches='tight')

img = Image.open(pic_loc + 'cx_0.png', 'r')
img_w, img_h = img.size
background = Image.new('RGB', (2300, 1200), (240, 239, 236))
bg_w, bg_h = background.size
offset = ((bg_w - img_w) // 2, 0)
background.paste(img, offset)
background.save(pic_loc + 'cx_1.png')
