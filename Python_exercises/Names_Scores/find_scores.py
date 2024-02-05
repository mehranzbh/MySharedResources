#import re
#new_string = re.sub('character_to_remove', '', original_string)

#reading file and initiating variables
f = open("C:\\My-files\\Codes\\Python Codes\\Names_Scores\\names.txt", "r")
ss = f.read()
chTotalScore = 0
Scores={}
counter = 0

# The list will look like this:
# L = ['"MARY"', '"PATRICIA"', '"LINDA"', '"BARBARA"', '"ELIZABETH"', '"JENNIFER"']

#creating a list from the text
L = ss.split(",")

#calculating the scores based on the word score and the place of the word in the sheet
for i in L:
    i = i[1:-1]    
    #print (i)
    for ch in i: #ch stands for character in a word - calculating the word score
        if 64 < ord(ch) < 98:
            chScore = ord (ch) - 65 + 1
            #print ("character score is :",chScore)
            chTotalScore += chScore
            #print ("is increasing: ",chTotalScore)
    # calculating word score = word * order    
    Scores[i]= chTotalScore * counter
    #print(Scores)
    counter += 1
    chTotalScore = 0


print(Scores)


