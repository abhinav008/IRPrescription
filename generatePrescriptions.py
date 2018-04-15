import os
import re
import sys
import operator

query = sys.argv[1]

regex_name = re.compile(r"1. Name:  (.*)\n")
regex_group = re.compile(r"2. Groups:  (.*)\n")
regex_ind = re.compile(r"4. Indication:  (.*)\n")

groupScore = {"Approved":"5", "Experimental":"-3", "Nutraceutical":"0", "Investigational":"-1", "Withdrawn":"-2", "Illicit":"-6", "Vet approved":"-4"}

def getDiseaseScores(sympList, N):
	diseaseScoreList = {}
	diseaseList = os.listdir("diseaseSym_dataset/")
	for filename in diseaseList:
		diseaseName = filename.split('.')[0]
		try:
			with open("diseaseSym_dataset/" + filename) as disease:
				symptomList = disease.readlines()
				# print(symptomList[:5])
				for symptom in symptomList:
					symptom = symptom.split(",")
					# print(symptom)
					if symptom[0].lower() in sympList:
						try:
							diseaseScoreList[diseaseName] += float(symptom[2])
						except:
							diseaseScoreList[diseaseName] = float(symptom[2])
		except:
			print(filename)
			print(diseaseList.index(filename))
	sorted_diseaseScoreList = sorted(diseaseScoreList.items(), key=operator.itemgetter(1))
	sorted_diseaseScoreList.reverse()
	print(sorted_diseaseScoreList[:N])
	retrievedDiseaseTuples = sorted_diseaseScoreList[:N]
	return retrievedDiseaseTuples

def generatePrescription(retrievedDiseaseTuples, query):
	for diseaseTuple in retrievedDiseaseTuples:
		with open("prescription/" + "Prescription_" + diseaseTuple[0] + ".html", "w") as f:
			htmlLines = []
			htmlLines.append("<! DOCTYPE = html>\n<html>\n<title>CS657 - Prescription</title>\n<style>\ndiv.container {\n\t\twidth: 100%;\n\t\tborder: 1px solid gray;\n}\n\nheader{\n\t\tpadding: 0.5em;\n\t\t#color: black;\n\t\tbackground-color: orange;\n\t\tclear: left;\n\t\ttext-align: center;\n}\n.footer{\n\t\tpadding : 1em;\n\t\tbackground-color: orange;\n\t\ttext-align: center;\n\t\t<!--- position: fixed;>\n\t\tbottom : 0;\n\t\twidth : 100%;\n}\n\nnav {\n\t\tfloat: left;\n\t\tmax-width: 160px;\n\t\tmargin: 0;\n\t\tpadding: 1em;\n}\n\nnav ul {\n\t\tlist-style-type: none;\n\t\tpadding: 0;\n}\n\t \nnav ul a {\n\t\ttext-decoration: none;\n}\n\narticle {\n\t\tmargin-left: 170px;\n\t\tborder-left: 1px solid gray;\n\t\tpadding: 1em;\n\t\toverflow: hidden;\n}\ntable {\n\t\tfont-family: arial, sans-serif;\n\t\tborder-collapse: collapse;\n\t\twidth: 80%;\n}\n\ntd, th {\n\t\tborder: 4px solid #000000;\n\t\ttext-align: middle;\n\t\tpadding: 8px;\n}\n\ntr:nth-child(even) {\n\t\tbackground-color: #eeeeee;\n}\t\n\ndiv.box {\n\t\tbackground-color: white;\n\t\twidth: 300px;\n\t\tborder: 2px solid green;\n\t\tpadding: 10px;\n\t\tmargin: 25px;\n}\n</style>\n<body>\n<div class=\"container\">\n\t<header><h1>\n\t\tIIT Kanpur Medical Labs</h1>\n\t</header>\n\t<hr>")
			# Output Query
			htmlLines.append("\t<h2> Precription for the query: </h2>\n\t<div class=\"box\">\n\t"+query+"\n\t</div>\n\t<hr>")
			# Output Disease
			htmlLines.append("\t<h2>\n\t\tIdentified Disease: </h2>\n\t<div class=\"box\">\n\t"+diseaseTuple[0]+"\n\t</div>\n\t<hr>")
			# Output Symptom
			otherSymptomList = open("diseaseSym_dataset/" + diseaseTuple[0] + ".txt", "r")
			lines = otherSymptomList.readlines()
			lines = sorted(lines, key=operator.itemgetter(2))[:5]
			otherSymptomList.close()
			otherSymptoms = ""
			lineIdx = 0
			while (lineIdx < (len(lines) - 1)):
				otherSymptoms += lines[lineIdx].split(", ")[0]
				otherSymptoms += ", "
				lineIdx += 1
			otherSymptoms += lines[lineIdx].split(", ")[0]
			htmlLines.append("\t<h2>More Symptoms: </h2>\n\t<div class=\"box\">\n\t"+otherSymptoms+"\n\t</div>\n\t\t<hr>")
			# Output Medication
			htmlLines.append("<h2>\nMedication:</h2>\n<table>\n\t<tr>\n\t\t<th>Serial No</th>\n\t\t<th>Drug Name</th>\n\t\t<th>Group</th>\n\t\t<th>Indication</th>\n\t</tr>")
			drugsList = []
			# vetApprovedDrugs = []
			# illicitDrugs = []
			drugs = open("disease_dataset/" + diseaseTuple[0] + ".txt", "r")
			lines = drugs.readlines()
			drugs.close()
			linesCount = len(lines)
			lineIdx = 0
			while (lineIdx < linesCount):
				# print(lines[lineIdx+2])
				drugGroup = re.sub(regex_group, r"\1", lines[lineIdx+2])
				drugName = re.sub(regex_name, r"\1", lines[lineIdx+1])
				drugInd = re.sub(regex_ind, r"\1", lines[lineIdx+4])
				drug = {"Name" : drugName, "Group" : drugGroup, "Indication" : drugInd}
				# print(drugGroup)					
				groups = drugGroup.split(", ")
				# print(groups)					
				# if not "Illicit" in drugGroup and not "Vet approved" in drugGroup:
				score = sum([int(groupScore[x]) for x in groups])
				drugsList.append((drug, score))
				lineIdx += 5
			sorted_drugsList = sorted(drugsList, key=operator.itemgetter(1))
			sorted_drugsList.reverse()
			for drug in sorted_drugsList:
				# Output Drug
				htmlLines.append("\t<tr>\n\t\t<td>"+str(sorted_drugsList.index(drug)+1)+".</td>\n\t\t<td>"+drug[0]["Name"]+"</td>\n\t\t<td>"+drug[0]["Group"]+"</td>\n\t\t<td>"+drug[0]["Indication"]+"</td>\n\t</tr>")
			htmlLines.append("</table>\n<div class=\"footer\"> Copyright &copy : IIT Kanpur\n</div>\t\n</div>\n</body>\n</html>")
			f.writelines(htmlLines)

N = 5
sympList = query.split(", ")
retrievedDiseaseTuples = getDiseaseScores(sympList, N)
generatePrescription(retrievedDiseaseTuples, query)