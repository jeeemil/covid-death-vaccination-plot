import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import aligny
import get_both_v_d

# Asking for a country
country = input('Write the country you want to plot: ')

# Combining both vaccines and deaths
merged = get_both_v_d.get_country_combined(country)

# Fetching the font file
reg_font_path=r'data/fonts/Helsingin-Text-TF-Book.ttf'
reg_font = fm.FontProperties(fname=reg_font_path)

# Creating figure
fig = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot(111)

# Create bar chart with deaths
bar = ax1.bar(merged.index, merged['deaths'], width=1, color='#626a70', zorder=10, label='Kuolleiden määrää 14 vuorokauden aikana miljoona asukasta kohti')
# Create a second y-axis
ax2 = ax1.twinx()
ax2.axes.yaxis.set_visible(False)
# Plotting both first and second dose vaccines
vaccine_1 = merged['vaccine_share_1'].fillna(method='ffill').plot(color='#f47521', ax=ax2, zorder=11, label='Ensimmäisen rokoteannoksen saaneet (%)')
vaccine_2 = merged['vaccine_share_2'].fillna(method='ffill').plot(color='#a6ce39', ax=ax2, zorder=11, label='Toisen rokoteannoksen saaneet (%)')
# Adding grid lines for both axis
ax2.grid(axis='y', linestyle='-.', zorder=9)
ax1.grid(axis='y', zorder=9)
# Setting the vaccinaton axis to be form 0-100
ax2.set_ylim([0, 100])
# Aligning the both axes (so they start from 0 at the same line)
aligny.align_yaxis(ax1, 0, ax2, 0)
# Creating a legend
fig.legend(loc='lower center', frameon=False, prop=reg_font)
# Creating a title
fig.suptitle(merged['fi_name'][0], fontproperties=reg_font, size=30)
# Saving figure in output folde
fig.savefig(f'output/{country}_' + str(merged.index.max()) + '.svg', dpi=150)
print(f'Svg of {country} created in output folder!')
