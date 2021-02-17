#Best Time to Buy and Sell Stock II

'''
Say you have an array prices for which the ith element is
 the price of a given stock on day i.
Design an algorithm to find the maximum profit.
 You may complete as many transactions as you like 
 (i.e., buy one and sell one share of the stock multiple times).
'''
'''
nota: subarreglos de diferencia maxima
'''


def maxProfit(prices):
	totprofit=0
	for i in range(len(prices)-1):
		if prices[i+1]>prices[i]: # means it is a peak
			totprofit+=prices[i+1]-prices[i]
	return totprofit
