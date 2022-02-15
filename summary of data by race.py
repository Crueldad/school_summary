
#%%
import pandas as pd 
import matplotlib.pyplot as plt
import mpld3
from mpld3._server import serve

read_path = r"C:\Users\cruel\OneDrive\Desktop\Data Summary - Task 2.xlsx"

data_summary = pd.read_excel(read_path)
DeKalb = data_summary.loc[data_summary['SCHOOL_DSTRCT_NM'] == 'DeKalb County']
Gwinnett = data_summary.loc[data_summary['SCHOOL_DSTRCT_NM'] == 'Gwinnett County']
Hall = data_summary.loc[data_summary['SCHOOL_DSTRCT_NM'] == 'Hall County']

districts = [DeKalb,Gwinnett,Hall]
labels = ['OVER_15_PERCENT_INDIAN','OVER_15_PERCENT_ASIAN','OVER_15_PERCENT_BLACK','OVER_15_PERCENT_WHITE','OVER_15_PERCENT_HISPANI','OVER_15_PERCENT_MULTI']

html_list = []
for i in districts:
    sizes = []
    for l in range(len(labels)):
        sizes.append((i[labels[l]].values[0]))

    explode = [0.0 if i != max(sizes) else 0.1 for i in sizes] 

    fig1, ax1 = plt.subplots()
    updated_labels = [i.split('_')[-1] for i in labels]
    ax1.pie(sizes, explode=explode, labels=updated_labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  

    school_name = i['SCHOOL_DSTRCT_NM'].item()
    plt.title((school_name+' '+'Over 15 percent'))
    html1 = mpld3.fig_to_html(fig1)
    html_list.append(html1)
    save_path = fr"""C:\Users\cruel\OneDrive\Desktop\{school_name}.html"""
    html1 = mpld3.save_html(fig1, save_path)

html_list = ' '.join(html_list) 
serve(html_list)    
    
    


# %%
