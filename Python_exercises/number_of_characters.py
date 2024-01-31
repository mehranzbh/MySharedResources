##initiaitig the variables
dic={}
unique = []
#ss = "lkjfgw09349utv t89034uglkdnf iieraio"        #for testing purposes

#---------------------------------------------------------#

ss = input ("please enter the string")  # ask for a character from the user

#counting different character types
ss = str (ss)
counted = []
for i in ss:
    if i not in counted:
        if ss.count(i) > 1:
            dic[i]= ss.count(i)
            counted.append(i) 
        else:
            unique.append(i)

#printing the outputs
print ("to check the number of different character:\n",dic)
print ("unique items are :", unique)