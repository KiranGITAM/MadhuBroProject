#this is the file in which the data before modifiaction exists ie 1986
#see that this python file and the txt file must be in same folde

filePointer = open("ModifyLine2.txt", "rt")

data = filePointer.read()
#now data is a variable which contain all the lines present in th file

print("the entire data in files before modification  is \n",data)
#here we are replacing the 1986 to 2020

data = data.replace('1986', '2020')

print("the entire data in files after  modification  is\n",data)

filePointer.close()
# now again we are opening the file in wt- mode which mean write text mode
filePointer = open("ModifyLine2.txt", "wt")

#now we are wring the data into the same file
filePointer.write(data)
#finally closing the file
filePointer.close()



"""


Method 2 This is the approach that we discussed during our phone conversation


# with is like your try .. finally block in this case
with open('ModifyLine2.txt', 'r') as file:
    # read a list of lines into data
    data = file.readlines()



# now change the 2nd line, note that you have to add a newline
data[1] = 'siva 2020'

# and write everything back
with open('ModifyLine2.txt', 'w') as file:
    file.writelines( data )



"""