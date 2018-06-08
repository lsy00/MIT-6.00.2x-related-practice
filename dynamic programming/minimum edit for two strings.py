def minimum_edit(s1,s2):
    insert = 0
    delete = 0
    replace = 0
    if len(s1) > len(s2):
        delete = len(s2)-len(s1)
    elif len(s1) < len(s2):
        insert = len(s1)-len(s2)
    for i in s1:
        if i not in s2:
           replace += 1
    edit = delete + insert + replace
    return edit

result = minimum_edit('cat','cut')

def minimum_edit_2(str1,str2,i,j,memo={}):
    if (i,j) in memo:
        result = memo[(i,j)]
    if i == 0:
        result = j
    elif j==0:
        result = i
    elif str1[i-1]==str2[j-1]:
        result = minimum_edit_2(str1,str2,i-1,j-1,memo)
    else:
        result= 1+min(minimum_edit_2(str1,str2,i-1,j,memo),\
                      minimum_edit_2(str1,str2,i,j-1,memo),\
                     minimum_edit_2(str1,str2,i-1,j-1,memo))
    memo[(i,j)] = result
    return result

ans = minimum_edit_2('bea','spe',2,2)
    
