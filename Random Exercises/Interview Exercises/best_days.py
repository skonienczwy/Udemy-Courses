# You are given a list of flight prices for consecutive days. For every sliding window of k days, 
# determine which day has the lowest price.

# Input:
# An array of integers representing prices for each day.

# An integer k representing the window size.

# Output:
# A list of day numbers (1-based) that correspond to the cheapest day in each window.

# Example
# text
# Days:    [1, 2, 3, 4, 5, 6, 7]
# Prices:  [120, 100, 140, 90, 110, 80, 95]
# Window size (k): 3
# Expected output (cheapest day in each window):
# [2, 4, 4, 6, 6]
# 💡 Your challenge: Write a function that takes (prices, k) and returns this list.
# First, try the straightforward approach (loop through each window).
# Then, if you want to push yourself, attempt an optimized sliding window solution.


# def cheapest_days(prices, k):
# """ Given a list of prices and a window size k, return the day numbers (1-based) of the cheapest day in each window. """ 
# # Step 1: Pair each price with its day number # Example: [(1, 120), (2, 100), (3, 140), ...] 
# # # Step 2: Slide a window of size k across the list 
# # # Step 3: For each window, find the minimum price and its day 
# # # Step 4: Collect the day numbers into a result list 

# return []

#Basic Approach
# days = [1, 2, 3, 4, 5, 6, 7]
# prices =  [120, 100, 140, 90, 110, 80, 95]
# window_of_days = 3
# def cheapest_days(days, prices, window_of_days ):
#     best_days = []
#     for i in range(len(days) - window_of_days + 1):
#         list_of_prices = prices[i: i + window_of_days]
#         list_of_days= days[i: i + window_of_days]
#         best_days.append(list_of_days[list_of_prices.index(min(list_of_prices))])
#     return best_days

# print(cheapest_days(days, prices, window_of_days))



#Using hashmap the way booking asked during interview.
#Based in a calendar of 20 days
# def best_days(start_date, end_date, range_of_days) -> dict:
#     prices = {}
    
#     pass

prices = {
    1: 220,  2: 180,  3: 250,  4: 300,  5: 210,
    6: 190,  7: 260,  8: 240,  9: 280, 10: 230,
   11: 200, 12: 270, 13: 310, 14: 290, 15: 260,
   16: 225, 17: 195, 18: 245, 19: 275, 20: 260,
   21: 210, 22: 235, 23: 255, 24: 285, 25: 305,
   26: 265, 27: 240, 28: 220, 29: 250, 30: 270,
   31: 230
}
start_date = 1
end_date =  3   



for i in prices:
    print(list(prices.keys()))


#Zip + Lambda
# data = list(zip(days, prices))
# window_size = 3
# best_days = []
# for i in range(len(data) - window_size + 1):
#     window = data[i:i+window_size]
#     min_day, min_price = min(window, key=lambda x: x[1])
#     best_days.append(min_day)
    
# print(best_days)



  
  






