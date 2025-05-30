#كود تحليل و مبيعات كل شهر و ترتيب الشهور و عمل سرم بياني عمةدي
import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_excel("store_sales.xlsx",sheet_name="2024")

data['order_date'] = pd.to_datetime(data['order_date'])
data['month_num'] = data['order_date'].dt.month
data['month_name'] = data['order_date'].dt.month_name()

grouped = data.groupby(['month_num','month_name'])['amount'].sum().sort_index()

ax = grouped.plot(kind='bar')
ax.bar_label(ax.containers[0])

plt.title("Total sales for the month")
plt.xticks(rotation=45)
plt.show()




