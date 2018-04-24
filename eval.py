#!/usr/bin/env python
import os,sys
def evaluate():

	f=open(sys.argv[1],'r')
	f1=open(sys.argv[2],'r')
	symptomdetected=sys.argv[3]
	symptomdetected=symptomdetected.split(";")
	groundTruth=f1.readlines()
	l=f.readlines()
	#print(symptomdetected)
	retrievedList=[]
	for i in range(0,len(l)-1):
		retrievedList.append(l[i].split("_")[2])
		retrievedList[i]=retrievedList[i].split("\n")[0]
	#print(retrievedList)

	symlist=[]
	for i in range(len(groundTruth)):
		symlist.append(groundTruth[i].split("_")[0])
	scores=[]
	#print(symlist)
	for i in range(len(symlist)):
		scores.append(0)
		for j in range(len(symptomdetected)):
			if(symlist[i]==symptomdetected[j]):
				print(groundTruth[i])
				tmp=groundTruth[i].split("_")[1]
				truediseaselist=[]
				truediseaselist=tmp.split(";;")
				#print(i,j,truediseaselist)
				for element in retrievedList:
					if element in truediseaselist:
						scores[i]=scores[i]+1

	scores=[i for i in scores if i > 0]
	Final_Precision=0.0
	if(sum(scores)>0):
		Final_Precision = sum(scores)/len(scores)*5
	print("Precision of retrieval is "+str(Final_Precision)+"%")



if __name__== "__main__":
	evaluate();