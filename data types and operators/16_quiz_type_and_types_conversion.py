mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#todo: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.

week_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
week_sales = str(week_sales)
print("This week\'s total sales: " + week_sales)