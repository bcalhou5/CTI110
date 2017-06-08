# Tip Tax Total
# 06/05/17
# CTI-110 M2HW2 - Tip Tax Total
# Benjamin Calhoun

total_cost = float(input('Enter the food cost: '))

tax_cost = total_cost * 0.07
tip_cost = total_cost * 0.18
final_cost = total_cost + tip_cost + tax_cost
print('the tax cost is', format(tax_cost, '.2f'))
print('the tip cost is', format(tip_cost, '.2f'))
print('the final cost is', format(final_cost, '.2f'))
