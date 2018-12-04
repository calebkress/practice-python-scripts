# Calculates the total of a dinner bill, given total, tax rate, and tip percentage.
def dinner_bill(pretax = input('Enter total pre-tax: '), taxrate = input('Enter the tax rate: '), tip_pct = input('Enter your tip percentage: ')):
    posttax = pretax + (pretax * taxrate)
    tip_amt = posttax * tip_pct
    total = posttax + tip_amt
    return('Total after tax: ' + str(posttax) + ', Total with tip: ' + str(total))
print(dinner_bill())
