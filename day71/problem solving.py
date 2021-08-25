customer_detail = {1001:'John',1004:'Jill',1005:'Joe',1003:'Jack'}

#1. Print details of customers
print('Customer Details: ')
print(customer_detail,'\n')


#2.print number of customers
print('Number of Customers are:',len(customer_detail),'\n' )

#3.print Customer in names in ascending order


#4.Delete the details of customer with customer id = 1005 and print updated dictionary
customer_detail.pop(1005)
print(customer_detail)

print()
#5.update the name of customer with customer id = 1003 to 'mary' and print
customer_detail[1003] = 'mary'
print('Updated customer_detail:')
print(customer_detail)

#6. check whether the detail of customer id 1002 exists in dict
if customer_detail[1002] in customer_detail:
    print('Customer detail of id=1002 is exists.')
else:
    print('Id 1002 does not exists.')
