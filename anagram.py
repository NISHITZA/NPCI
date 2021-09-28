str1 = "care"
str2 = "race"
str3 = "erca"

str1 = ''.join(sorted(str1))
str2 = ''.join(sorted(str2))
str3 = ''.join(sorted(str3))


print(str1)
print(str2)
print(str3)

index = 0
flag = 0
len1 = len(str1)
len2 = len(str2)
len3 = len(str3)

if( len1!=len2 or len2!=len3 or len3!=len1):
    flag=1
else:
    for i in range(0,len(str1)):
        if(str1[i]!=str2[i] or str2[i]!=str3[i] or str3[i]!=str1[i]):
            flag=1 
            break

if(flag==1):
    print('They are not an anagram')
else:
    print('They are anagram')

