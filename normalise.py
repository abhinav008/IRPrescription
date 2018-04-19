import os,sys

def calculatemax(l):
    myMax = l[0]
    for num in l:
        if myMax < num:
            myMax = num
    return myMax


def normalisescores():
	diseaseScoreList = {}
	diseaseList = os.listdir("diseaseSym_dataset_2.0/")
	counter=0;
	for filename in diseaseList:
		print(filename),
		diseaseName = filename.split('.')[0]
		disease= open("diseaseSym_dataset_2.0/" + filename)
		symptomList = disease.readlines()
		scorelist=[]
		symlist=[]
		somelist=[]
		actuallist=[]
		writelist=[]
		for symptom in symptomList:
			symptom = symptom.split(";")
			scorelist.append(float(symptom[2]))
			symlist.append(symptom[0])
			somelist.append(symptom[1])
			actuallist.append(symptom[2])
		Max=calculatemax(scorelist)
		#normalise scorelist using Max
		for i in range(len(scorelist)):
			scorelist[i]=scorelist[i]/Max;
		count=0;
		#updating the file using new scorelist
		for symptom in symptomList:
			symptom = symptom.split(";")
			writelist.append(str(symptom[0])+","+str(symptom[1])+", "+str(scorelist[count])+"\n")
			count=count+1;
		disease.close()
		disease= open("diseaseSym_dataset_2.0/" + filename,'w')
		counter=counter+1
		print(counter)
		disease.writelines(writelist)		
if __name__=="__main__" :
	normalisescores();
