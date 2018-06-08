def subset_sum(L,avail,memo={},result=False):
    if L in memo:
        (result,avail)=memo[L]
    if avail == 0:
        result = True
    elif avail > 0 and L == []:
        result = False
    else:
        if L[0] > avail:
            result = subset_sum(L[1:],avail,memo,result)
        else:
            result = max(subset_sum(L[1:],avail-L[0],memo,result),\
                subset_sum(L[1:],avail,memo,result))
        
    return (result,avail)
        
            
