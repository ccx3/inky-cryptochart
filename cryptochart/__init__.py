from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib import font_manager

w, h = (212, 104)
dpi = 144
fig, ax = plt.subplots(figsize=(212/dpi, 104/dpi), dpi=dpi)
fig.subplots_adjust(top=1, bottom=0, left=0.15, right=1)

ticks_font = font_manager.FontProperties(fname='04B_03__.TTF', size=4)
plt.rcParams['text.antialiased'] = False

for label in ax.get_yticklabels() :
    label.set_fontproperties(ticks_font)
ax.yaxis.set_tick_params(pad=2)

#ax.tick_params(labelsize=8)
ax.xaxis.set_ticks([])
#ax.xaxis.set_visible(False)
ax.set_frame_on(False)
#ax.set_axis_off()
#ax.axis('off')
