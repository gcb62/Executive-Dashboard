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



print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")

