import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import aligny
import get_both_v_d

country_list = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czechia', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland','Italy','Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Poland', 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Israel', 'Norway', 'United kingdom', 'Russia', 'Ukraine' ]

for country in country_list:
    # Asking for a country
    #country = input('Write the country you want to plot: ')
    merged = get_both_v_d.get_country_combined(country)

    reg_font_path=r'data/fonts/Helsingin-Text-TF-Book.ttf'
    reg_font = fm.FontProperties(fname=reg_font_path)

    fig = plt.figure(figsize=(10, 10))
    ax1 = fig.add_subplot(111)

    bar = ax1.bar(merged.index, merged['deaths'], width=1, color='#626a70', zorder=10, label='Kuolleiden määrää 14 vuorokauden aikana miljoona asukasta kohti')
    ax2 = ax1.twinx()
    ax2.axes.yaxis.set_visible(False)

    vaccine_1 = merged['vaccine_share_1'].fillna(method='ffill').plot(color='#f47521', ax=ax2, zorder=11, label='Ensimmäisen rokoteannoksen saaneet (%)')
    vaccine_2 = merged['vaccine_share_2'].fillna(method='ffill').plot(color='#a6ce39', ax=ax2, zorder=11, label='Toisen rokoteannoksen saaneet (%)')
    ax2.grid(axis='y', linestyle='-.', zorder=9)
    ax1.grid(axis='y', zorder=9)
    ax2.set_ylim([0, 100])
    aligny.align_yaxis(ax1, 0, ax2, 0)
    fig.legend(loc='lower center', frameon=False, prop=reg_font)
    fig.suptitle(merged['fi_name'][0], fontproperties=reg_font, size=30)

    #plt.show()
    fig.savefig(f'output/{country}_' + str(merged.index.max()) + '.svg', dpi=150)
    print('Svg created in output folder!')