#code input - names to be ordered
ttinput = """
3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F
"""

#lisitng the text, each line becomes an item in the list
def create_list(text):
    text_stripped = text.strip()
    
    # Next, split the stripped text into lines based on the newline character
    lines = text_stripped.split('\n')
    #print (lines)
    return lines

# from each item, a list is created which contains name, age, gender
def extractinfo(ll):
    itemslist=[]
    for item in ll:
        splitted_ll = item.split(' ')
        item.strip()
        itemsex = splitted_ll[-1:]
        itemsex = itemsex[0]
        itemage = splitted_ll[-2:-1]
        itemname = splitted_ll [:-2]
        itemname = ' '.join(itemname)
        itemlist = [1]*3
        itemlist[0] = itemname
        itemlist [1] = int(itemage[0])
        itemlist [2] = itemsex
               
        itemslist.append(itemlist)
    
    #print (itemslist)
    return itemslist


#sorting the items based on the age and printing the final output
sorted_itemslist = sorted(itemslist, key=lambda x:x[1])
#print (sorted_itemslist)
for item in sorted_itemslist:
    if item[2] == 'M':
        print ('Mr.',item[0])
    elif item[2] == 'F':
        print ('Mrs.',item[0])

mainlist = create_list(ttinput)
mainlist = mainlist [1:]
itemslist = extractinfo (mainlist)
