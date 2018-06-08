def ugly_num(n):
    ugly = []
    ugly.append(1)
    multiple_2 = 2
    multiple_3 = 3
    multiple_5 = 5

    for i in range(1,n):
        val = min(multiple_2,multiple_3,multiple_5)

        if val == multiple_2:
            ugly.append(multiple_2)
            multiple_2*=2
        elif val == multiple_3:
            ugly.append(multiple_3)
            multiple_3 *=3
        elif val == multiple_5:
            ugly.append(multiple_5)
            multiple_5 *=5
            
    return ugly[n-1]
        
                
