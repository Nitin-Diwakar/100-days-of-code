furniture = ['sofa set','dinning table','t.v. stand','cupboard']
costs = [20000, 8500,4599,13920]

def bill(quantity):
    if a == 'sofa set':
        bill_s = costs[0]
        total = quantity*bill_s
        print('Total amount is',total)

    elif a == 'dinning table':
        bill_d = costs[1]
        total = quantity*bill_d
        print('Total amount is',total)

    elif a == 't.v. stand':
        bill_t = cost[2]
        total = quantity*bill_t
        print('Total amount is',total)
    else:
        bill_c = cost[3]
        total = quantity*bill_c
        print('Total amount is',total)
    

a = input('Enter the name of Furniture:')
if a in furniture:
    quantity = int(input('Enter the quantity of {}'.format(a)))
    if quantity > 0:
        bill(quantity)
    else:
        print('Total is 0')


    
