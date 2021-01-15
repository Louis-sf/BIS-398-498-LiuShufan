# 2.12 (7% Investment Return) Some investment advisors say that it’s
#reasonable to expect a 7% return over the long term in the stock market.
#Assuming that you begin with $1000 and leave your money invested,
#calculate and display how much money you’ll have after 10, 20 and 30
#years. Use the following formula for determining these amounts:

       
p=1000
# r needs to be a percentage value
r=.07
for n in range(10,31,10):
    p = p*(1+r/100)**n
    print("In year", n, "the return is: ", p)
        
