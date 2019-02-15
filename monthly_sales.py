# monthly_sales.py


CSV_FILENAME = "sales-201803.csv"

csv_filepath = os.path.join("data" , CSV_FILENAME)

def month_lookup(month):
	year_month={'01':'January','02':'February','03':'March','04':'April',
	'05':'May','06':'June','07':'July','08':'August','09':'September','10':'October',
	'11':'November', '12':'December'}
	return year_month[month]


# thanks to @hiepnguyen034 for help with the dictionary structure, lines 6-10 --> lines 16-20


# now using #matplotlib

#inputs


def to_usd(sales):
    return "${0:,.2f}".format(sales)

def to_usd(total_sales):
    return "${0:,.2f}".format(total_sales)

def month_lookup(month):
	selected_month ={'01':'January','02':'February','03':'March','04':'April',
	'05':'May','06':'June','07':'July','08':'August','09':'September','10':'October',
	'11':'November', '12':'December'}
	return selected_month[month]


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


	csv_file_name = csv_file_name.replace("sales-", "")
	year = csv_file_name[0:4]
	month = csv_file_name[4:6]
	month = month_lookup(month)
		


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

	print("TOTAL MONTHLY SALES: " + str(total_sales))

	count = 0

	print("-----------------------")
	print("TOP SELLING PRODUCTS:")
	for idx, i in sales.iterrows():
		count = count + 1
		print(count, idx, to_usd(i['sales price']))

	print("-----------------------")
	print("VISUALIZING THE DATA...")
