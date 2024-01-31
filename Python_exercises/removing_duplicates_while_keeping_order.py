# to find out about the problem statement, visit the URL below:
# URL = "https://www.hackerrank.com/challenges/merge-the-tools/problem"
#source: "HackerRank"

#initializing variables:
string = "ABCAAABVHBBH"
k = 3
listcount = len(string) / k
listcount = int(listcount)


#creating the list fuction:
def ToList(string,k):
    s = str(string)
    listcount = len(s) / k
    L = []*int(listcount)   
    
    for i in range(0,len(s)):
        if i%3 == 0:
            L.append(s[i:i+3])
            
    print (L)
    return L
    
#removing duplicates while keeping order
def removeduplicates(obj):
   for i in obj:
       #print (i)
       if obj.count(i) > 1:
           #print (obj.count(i))
           obj = obj[:obj.rfind(i)]+obj[obj.rfind(i)+1:len(obj)]
   print (obj)
   return obj


#combining element and creating new list as the final answer
def creatLnew():
    Lnew=[]
    for i in range(0,listcount):
        Lnew.append(removeduplicates(L[i]))
    
    return Lnew


#running the code
L = ToList(string,k)
print (creatLnew())