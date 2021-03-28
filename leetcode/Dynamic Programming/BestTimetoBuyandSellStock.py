#Leet Code 
# Best Time to Buy and Sell Stock

# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction 
# (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.

# #EXAMPLE:
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

#brut force
def btbss(l):
    m = 0
    for i in range(len(l)-1):
        for j in range(i+1,len(l),1):
            if l[j]>l[i]:
                m= max(m,(l[j]-l[i]))
    return m
    
input = [7,1,5,3,6,4]
i=[1,2]
w= [7,6,4,3,1]
print(btbss(i))

# solution2: max peak and min valley
def buyAndSell(prices):
    cheapest=float('inf')
    maxprofit=0
    for i in range(len(prices)):
        cheapest=min(cheapest,prices[i])
        maxprofit=max(prices[i]-cheapest,maxprofit)
    return maxprofit

print(buyAndSell(i))





