 
#Programmingtask 2
from sets import  Set            #importing set to get unique
from collections import Counter  #importing counter to count
def crimecount():
	fin= open("Crime.csv")  #opening file
	count= Counter()
	count_crime=[]     #a list to  get all crimes
	count_cid= []      # a list to get crime ids
#	set1={}
	for line in fin:	
		line=line.strip()
		line=line.split(",")
		count_crime.append(line[-1])   #appending the last column(crime name)
		count_cid.append(line[-2]) #appending second last column(crime id)
	unicount_crime=sorted(set(count_crime)) #converting to set to get unique valvues
	unicount_cid=sorted(set(count_cid))  # unique ids & sorting
	print("\n  CRIME       ID \n")
	print(unicount_cid)
	print("\n----------------------------------------------------------------\n")
	print("\n  CRIME 	  NAME\n")
	print(unicount_crime)
	print("\n")
#	for i in countc:
#		if i[0] == "RUCR_EXT_D":
#			del i[0]
	print("\n-------------------------------------------------------------------\n")
	print("\n  CRIME     COUNT      \n")
	for i in count_crime:        #counting the crimes
			c=i[0]
			count[i]+=1
	print(count) #printing the number of  crimes
	print("-------------------------------------------------------------------------------------\n")

crimecount()










