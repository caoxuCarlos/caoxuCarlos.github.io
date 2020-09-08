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
x1 = df["day_num"]
y1 = df["delta_of_bf_ratio"]
ax1.set_xlabel("Day")
ax1.set_ylabel('Relative Body-fat Ratio')
ax1.grid(True, which='both', axis='both', color='#D6D1D0', linestyle='-', linewidth=2)
ax1.plot(x1, y1, color='#363642', linewidth='3')
ax1.yaxis.set_major_formatter(mtick.PercentFormatter())
ax1.set_facecolor('#F0EFEC')
ax1.set_ylim((-6, 4))
fig1.set_facecolor('#F0EFEC')
fig1.savefig(pic_loc + 'rbf.png', dpi=200, pad_inches=10)


fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
x2 = df["day_num"]
y2 = df["weight"]
ax2.set_xlabel("Day")
ax2.set_ylabel("Weight")
ax2.grid(True, which='both', axis='both', color='#D6D1D0', linestyle='-', linewidth=2)
ax2.plot(x2, y2, color='#610006', linewidth='3')
ax2.set_facecolor('#F0EFEC')
ax2.set_ylim((65, 75))
fig2.set_facecolor('#F0EFEC')
fig2.savefig(pic_loc + 'w.png', dpi=200, pad_inches=10)

# plt.show()

img = Image.open(pic_loc + 'rbf.png', 'r')
img_w, img_h = img.size
background = Image.new('RGB', (2200, 1200), (240, 239, 236))
bg_w, bg_h = background.size
# offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
offset = ((bg_w - img_w) // 2, 0)
background.paste(img, offset)
background.save(pic_loc + 'rbf_1.png')

img2 = Image.open(pic_loc + 'w.png', 'r')
img2_w, img2_h = img2.size
# background2 = Image.new('RGBA', (2300, 1600), (255, 255, 255, 255))
background2 = Image.new('RGB', (2200, 1200), (240, 239, 236))
bg2_w, bg2_h = background2.size
# offset2 = ((bg2_w - img2_w) // 2, (bg2_h - img2_h) // 2)
offset2 = ((bg2_w - img2_w) // 2, 0)
background2.paste(img2, offset2)
background2.save(pic_loc + 'w_1.png')
