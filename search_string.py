str1='google'
str2='gle'


str1_list=list(str1)

str2_list=list(str2)
#print(str1_list,str2_list[0])

j=len(str2_list)
#for i in len(str1_list):
temp=[]
    

for i in range(len(str1_list)):
    if str2_list[0] in str1_list[i]:
        temp.append(str1_list[i:i+j])
    
    continue
print(temp[0])    
temp_string=''.join(temp[0])
#print(temp_string)

if temp_string in str2:
    print(True)
else:
    print(False) 


#if str2 in str1:
#    print(True)
#else:
#    print(False) 