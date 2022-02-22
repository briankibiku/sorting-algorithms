
# bubble sort 2
numbers_array = [8,3,1,7,2,5]
 

def bsrt(s):
  for i in range(0,len(s)-1):
    for j in range(i+1,len(s)):
      if s[j]<s[i]:
        s[i],s[j]=s[j],s[i]
      pass
  return s
  
  
print(bsrt(numbers_array))