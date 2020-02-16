#this is the file in which the data before modifiaction exists
#see that this python file and the txt file must be in same folder

filePointer = open("data_NA.txt", "rt")

data = filePointer.read()
#now data is a variable which contain all the lines present in th file

#print("the entire data in files before modification  is \n",data)
#here we are replacing the "N.A" -> "" i.e removing N.A

data = data.replace('N.A', '')

print("the entire data in files after  modification  is\n",data)

filePointer.close()
# now again we are opening the file in wt- mode which mean write text mode
filePointer = open("data_NA.txt", "wt")

#now we are wring the data into the same file
filePointer.write(data)
#finally closing the file
filePointer.close()