def increase_seq(l):
    '''
    print out the longest increasing subsequence
    '''
    ans = [[l[0]]]
    minimum = l[0]
    for num in l:
        if num < minimum and len(ans[-1]) == 1:
            ans.append([num])
            minimum = num
        if num > (ans[-1][-1]):
            ans[-1].append(num)
    return max(ans,key=len)

def len_increase_seq(l):
    '''
    find out length of LIS
    '''
    minimum = l[0]
    maximum = l[0]
    length = 1
    for num in l:
        if num < minimum and length == 1:
            minimum = num
            maximum = num
        if num > maximum:
            length += 1
            maximum = num
    return length

a = [50,8,10,7,40,80]
result = increase_seq(a)
re = len_increase_seq(a)
    


