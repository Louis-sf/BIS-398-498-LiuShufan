#5.15 (Tuples Representing Invoices) When you purchase products or
#services from a company, you typically receive an invoice listing what you
#purchased and the total amount of money due. Use tuples to represent
#hardware store invoices that consist of four pieces of data—a part ID
#string, a part description string, an integer quantity of the item being
#purchased and, for simplicity, a float item price (in general, Decimal
#should be used for monetary amounts). Use the sample hardware data
#shown in the following table.
 
invoice = (('83','Electric sander', 7, 57.98),
           ('24','Power saw', 18, 99.99),
           ('7','Sledge hammer',11, 21.50),
           ('77','Hammer', 76, 11.99),
           ('39','Jig Saw', 3, 79.50))


#1Use function sorted with a key argument to sort the tuples by
#part description, then display the results. To specify the element
#of the tuple that should be used for sorting, first import the
#itemgetter function from the operator module as in
#   from operator import itemgetter
#Then, for sorted’s key argument specify itemgetter(
#index ) where index specifies which element of the tuple should
#be used for sorting purposes.
from operator import itemgetter
invoice = sorted(invoice,key = itemgetter(1))
print(invoice)

#2. Use the sorted function with a key argument to sort the tuples
#by price, then display the results.
invoice = sorted(invoice,key = itemgetter(3))
print(invoice)

#3.Map each invoice tuple to a tuple containing the part description
#and quantity, sort the results by quantity, then display the results.
invoice3 = sorted(tuple(map(lambda x: x[1:3] , invoice)),key =itemgetter(1))
print(invoice3)
    
  
    
#4.Map each invoice tuple to a tuple containing the part description
#and the value of the invoice (the product of the quantity and the
#item price), sort the results by the invoice value, then display the
#results.
invoice4 = list(invoice)
invoice4 = list(map(lambda x : list(x), invoice4))    
for item in invoice4:
    item = item.append(item[2]*item[3])
invoice4 = tuple(sorted(invoice4, key = itemgetter(4)))    
print(invoice4)
  #invoice4 = list((map(lambda x: x.append(x(2)*x(3)), invoice4)))
#5. Modify Part (d) to filter the results to invoice values in the range
#$200 to $500.
invoice4 = list(invoice4)
invoice4 = list(map(lambda x : list(x), invoice4))
invoice5 = list(filter(lambda x: x[4]>=200 and x[4]<=500, invoice4))  
print(invoice5)

#6.Calculate the total of all the invoices.
total =0
for item in invoice4:
    total = total + item[4]
print('total is: ', total)
    
