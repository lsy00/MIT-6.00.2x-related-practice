def common_seq(str1,str2):
	x,y = 0,0
	ans = ''
	while x <=(len(str1)-1):
		if str2[x] in str1[y:]:
			ans  += str2[x]
			y = str1.find(str2[x])+1
		x+=1
	return ans
ans = common_seq('abc','dac')

def common_seq2(s1,s2，memo):
        if s1 == '' or s2 == '':
                return 0
        elif s1[-1] == s2[-1]:
                return 1+common_seq2(s1[:-1],s2[:-1])
        else:
                return max(common_seq2(s1[:-1],s2),common_seq2(s1,s2[:-1]))
result = common_seq2('gttahx','atbchgx')
