
# coding: utf-8

# In[38]:


# myreduce function
def myreduce(IpFunc,IpRange):
    start = IpRange[0]
    end = IpRange[1]
    out = IpFunc(start,end)
    start=out
    count=0
    for i in IpRange:
        count=count+1    
        if count > 2:            
            end = i
            out = IpFunc(start,end)
            start=out            
    return out

# Arithmetic Functions
def func_Add(n1,n2):
    return n1+n2

def func_Subtract(n1,n2):
    return n1-n2

def func_Multiply(n1,n2):
    return n1*n2

# Call myreduce       
IpRange=range(1,5)
print('Input Range: \n\t',IpRange)
print('\nAdd Reduce: \n\t', myreduce(func_Add,IpRange))
print('\nSubtraction Reduce: \n\t', myreduce(func_Substract,IpRange))
print('\nMultiply Reduce: \n\t', myreduce(func_Multiply,IpRange))    


# In[19]:


#myFilter Function
def myfilter(logicFunc,IpRange):    
    Out=[]
    for i in IpRange:
        if logicFunc(i)==True:
            Out.append(i)
    return Out

#Logical Functions
def IsEven(intInput):
    if intInput%2==0:
        return True

def IsOdd(intInput):
    if intInput%2!=0:
        return True

def IsPerfectSquare(intInput):
    intTemp = int(pow(intInput, 1/2))
    intTemp = pow(intTemp, 2)
    if intTemp==intInput:
        return True


# Call myfilter
IpRange = range(1,100)
print('Input Range: \n\t',IpRange)
print('\nEven Number from Range: \n\t', myfilter(IsEven,IpRange))
print('\nOdd Number from Range: \n\t', myfilter(IsOdd,IpRange))   
print('\nPerfect Square Number from Range: \n\t', myfilter(IsPerfectSquare,IpRange))


# In[23]:


print('\nList1')
strIp = 'ACADGILD'
Out=[Letter for Letter in strIp]
print(Out)

print('\nList2')
strIp = 'x,xx,xxx,xxxx,y,yy,yyy,yyyy,z,zz,zzz,zzzz'
Out=[Letter for Letter in strIp.split(',')]
print(Out)

print('\nList3')
strIp = 'x,y,z,xx,yy,zz,xx,yy,zz,xxxx,yyyy,zzzz'
Out=[Letter for Letter in strIp.split(',')]
print(Out)

print('\nList4')
strIp = '234345456'
Out=[[int(Letter)] for Letter in strIp]
print(Out)

print('\nList5')
strIp = [list(range(2,6)),list(range(3,7)),list(range(4,8)),list(range(5,9))]
Out=[Letter for Letter in strIp]
print(Out)

print('\nList6')
strIp = [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
Out=[Letter for Letter in strIp]
print(Out)


# In[37]:


def longestWord(Word):    
    longest_Word = ''    
    for i in Word:        
        if len(longest_Word)<=len(i):
            longest_Word=i
    return longest_Word

#Call the function with a list
strListofWords='India is my country and all Indians are my brothers and sisters'
list_Of_Words=list(strListofWords.split(' '))
print('List of words: \n',lst_Of_Words, '\n')
print('Longest word: \n',longestWord(list_Of_Words))

