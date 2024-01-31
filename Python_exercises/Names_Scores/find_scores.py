#the image file in the root folder explained the problem
#the names are extracted from the names.txt file in the same folder


#reading the file
f = open(".\\names.txt", "r")   #first argument gets the text file path
ss = f.read()

#initiating the variables
chTotalScore = 0
Scores={}

#L = ['"MARY"', '"PATRICIA"', '"LINDA"', '"BARBARA"', '"ELIZABETH"', '"JENNIFER"']   #for debugging puposes

#creating a list from the string
L = ss.split(",")

#calculating the score
for i in L:
    i = i[1:-1]
    #print (i)
    for ch in i:
        if 64 < ord(ch) < 98:
            chScore = ord (ch) - 65 + 1
            #print ("character score is :",chScore)
            chTotalScore += chScore
            #print ("is increasing: ",chTotalScore)
    #Scores.append(chTotalScore)
    Scores[i]=chTotalScore
    #print(Scores)
    
    chTotalScore = 0

#printing the names with their respective scores
print(Scores)
