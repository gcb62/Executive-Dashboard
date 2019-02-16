# monthly_sales.py



import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import operator
import csv

#inputs


def to_usd(sales):
    return "${0:,.2f}".format(sales)

# def to_usd(total_sales):
#     return "${0:,.2f}".format(total_sales)

def month_lookup(month):
	selected_month ={'01':'January','02':'February','03':'March','04':'April',
	'05':'May','06':'June','07':'July','08':'August','09':'September','10':'October',
	'11':'November', '12':'December'}
	return selected_month[month]

# thanks to @hiepnguyen034 for help with the dictionary structure, lines 6-10 --> lines 21-25

def main():
	print(" -------------------------------- ")
	print("                                  ")
	print("Welcome to the executive dashboard ")
	print("                                  ")
	print(" -------------------------------- ")
	print("                                  ")
	print(" -------------------------------- ")
	print("                                  ")
	print("Insert your data file below")
	print("                                  ")
	print(" -------------------------------- ")
	print("                                  ")




	csv_file_name = input("Please enter the file's name (without the '.csv' extension) in the format " + " sales-YYYYMM: ")
	csv_file_extension = csv_file_name + ".csv"
	file_title = os.path.join("CSV Data/" , csv_file_extension)

	# matching the inputs with the data

	file_results = 0

	if (os.path.isfile(file_title)):
		file_results = pd.read_csv(file_title)
	else:
		print('invalid file')
		return

	# defining variables, matching the month and the years from the csv files

	csv_file_name = csv_file_name.replace("sales-", "")
	year = csv_file_name[0:4]
	month = csv_file_name[4:6]
	month = month_lookup(month)
		
	#defining sales variables, formula borrow from @hiepnguyen034

	sales = file_results.groupby(file_results["product"]).sum()
	sales = sales.sort_values(by=["sales price"], ascending=False)
	# print(sales.columns)
	# print(file_results)
	# print(sales)
	total_sales = sales[['sales price']].sum()[0]
	# print(total_sales)

	print("-----------------------")
	print("MONTH and YEAR: {} {}".format(month,year))

	print("-----------------------")
	print("CRUNCHING THE DATA...")

	print("-----------------------")

	print("TOTAL MONTHLY SALES: " + to_usd(total_sales))

	count = 0

	print("-----------------------")
	print("TOP SELLING PRODUCTS:")
	for idx, i in sales.iterrows():
		count = count + 1
		print(count, idx, to_usd(i['sales price']))
# $ conversion so the output of sales is more human-friendly

# big shoutout to TA @robchurchill for helping institute this function

	# plot the graph
	fig, ax = plt.subplots()
	# format the graph
	fig.set_figheight(5)
	fig.set_figwidth(25)
	ax.barh(sales.index, sales['sales price'])
	ax.set_xlabel("USD")
	ax.set_ylabel("Products")
	# format it into $
	fmt = '${x:,.2f}'
	tic = tick.StrMethodFormatter(fmt)
	ax.xaxis.set_major_formatter(tic)
	ax.set_title('Total Sales')
	for idx, val in sales.iterrows():
		ax.text(val['sales price'], idx, to_usd(val['sales price']))
	plt.show()


if __name__ == "__main__":
	main()
