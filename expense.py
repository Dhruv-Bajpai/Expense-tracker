
print('it is a expense tracker')
Table = []
amount = int(input('how much money do u have '))

while amount >= 0:
    expense = input('enter the expense: ')
    newmount = int(input('please enter the amount of this expense: '))
    amount = amount - newmount
    print(f'you have {amount} left')
    Table.append([expense, newmount])
    if amount<=0:
    	break
    
print('---------------------------------------')
for expense, amount in Table:
    print(expense, '|',amount)