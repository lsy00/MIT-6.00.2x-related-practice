def repeated_seq(str1):
    ans = ''
    for i in str1:
        first_position = str1.find(i)
        temp = str1[first_position+1:]
        if i in temp and temp.count(i)==1 and i not in ans:
            has_found = True
            ans += i
    return ans
ans = repeated_seq('acab')
        
        
