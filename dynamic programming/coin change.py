def coinchange(n,s):
    
    def compare(n,coin,memo):
        value = n-coin
        if value in memo:
            return memo[value] + [coin]
        elif value == 0:
            return [coin]
        elif value < 0:
            return [value]*n
    
    memo = {}
    for num in range(1,n+1):
        ans =min(compare(num,s[0],memo),compare(num,s[1],memo),compare(num,s[2],memo),key=len)
        memo[num]=ans
    return memo[n]
result= coinchange(10,[5,6,2,3])

            
