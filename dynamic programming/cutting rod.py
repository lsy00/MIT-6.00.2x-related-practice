def cutting_rod(length,price,memo={}):
    ans = 0
    for i in length:
        for j in range(i):
            diff = i-j
            if diff in memo and price[j-1]+memo[diff] > ans:
                ans = price[j-1]+memo[diff]
            elif diff in length and price[diff-1]>ans:
                ans = price[diff-1]
        memo[i] = ans
    return ans
            
length = [1,2,3,4,5,6,7,8]
price = [3,5,8,9,10,17,17,20]
result = cutting_rod(length,price)
