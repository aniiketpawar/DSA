expense = [2200, 2350, 2600, 2130, 2190]

# Q1
print("In feb this much extra was spent compared to jan: ", expense[1]-expense[0])

# Q2
print("Total expense of the quarter is: ", expense[0]+expense[1]+expense[2])

# Q3
#method 1
def if_expense_2000(expenses):
    if 2000 in expenses:
        return True
    else:
        return False

print(if_expense_2000(expense))

#method 2
print("if any expense is exact 2000$: ", 2000 in expense)


# Q4
expense.append(1980)
print("Expenses at the end of the June month is: ", expense)

# Q5
expense[3] = expense[3]-200
print("Expense after correction in the month of April is: ", expense)

print(expense)
