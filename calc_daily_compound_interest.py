import csv
import pandas as pd
import matplotlib.pyplot as plt

# plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.3f'))#y軸小数点以下3桁表示

principal = 3300 * 80
interest = 0.05
periods = 365 * 5

result = principal

index = []
list = []

for i in range(periods):
	dailyProfit = result * interest / 365
	result += dailyProfit
	profit = result - principal
	index.append(i)
	list.append(round(dailyProfit, 2))

profit = result - principal

print('結果: ', result)
print('利益: ', profit)
print('期間: ', periods / 365, '年')

# CSV出力
# with open ('example.csv', 'w') as f:
# 	writer = csv.writer(f)
# 	for item in list:
# 		writer.writerow([item])

# 折れ線グラフ出力
sales = pd.Series(list, index)
plt.plot(sales.index, sales.values)
plt.title(f' Daily compound interest simulation {periods} days {principal} yen')
plt.xlabel('Periods')
plt.ylabel('Profit')
plt.show()