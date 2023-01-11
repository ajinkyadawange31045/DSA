n = 50
# s = 0
# for i in range(1,n):
#     if i%3 == 0 or i%5 ==0:
#         s = s+i
        
# print(s)

# now again use formulae from arithmetic algorithms
# s1 = 3+ 6+9+12+15+18+21+24+27......
# s2 = 5+10+15+20+......
# s3 = 15+30 + 45 ....
# sum = n x (2a + (n-1)d)/2  #using arithmetic means

# 3 ke kitne multiples honge, 50 ke under so 49//3 = 16, i.e. (n-1)//3 or n-1//5
# 15 are added twice, so , we need to subtract the sum of multiple of 15

n = 50
n1 = (n-1) // 3
n2 = (n-1) // 5
n3 = (n-1)//15

s1 = n1*(2*3+(n1-1)*3)//2 
s2 = n2*(2*5+(n2-1)*5)//2 
s3 = n3*(2*15+(n3-1)*15)//2 

print(s1+s2-s3) #with time complexity  O(1)