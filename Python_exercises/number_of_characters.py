#this code counts the number of characters in a given string and provides the character as well as the count.

#ss = "lkjfgw09349utv t89034uglkdnf iieraio"        #for testing purposes

#---------------------------------------------------------#

# getting the text from the user
ss = input ("please enter the string")  # ask for a character from the user

##initiaitig the variables
dic={}
unique = []

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
