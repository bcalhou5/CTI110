# Sales Prediction
# 06/05/17
# CTI-110 M2T1 - Sales Prediction
# Benjamin Calhoun

# Get the projected total sales.
total_sales = float(input('Enter the projected sales: '))

# Calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23

# Display the profit
print('The profit is $', format(profit, ',.2f'))
