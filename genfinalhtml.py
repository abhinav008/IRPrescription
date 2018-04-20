import sys,os
query=sys.argv[1]

def main():
	f= open("gnefinal.html","w+")
	html=[]
	html.append("<! DOCTYPE = html>\n<html>\n<title>CS657 - Prescription</title>\n<style>\ndiv.container {\n\t\twidth: 100%;\n\t\tborder: 1px solid gray;\n}\n\nheader{\n\t\tpadding: 0.5em;\n\t\t#color: black;\n\t\tbackground-color: orange;\n\t\tclear: left;\n\t\ttext-align: center;\n}\n.footer{\n\t\tpadding : 1em;\n\t\tbackground-color: orange;\n\t\ttext-align: center;\n\t\tposition: fixed;\n\t\tbottom : 0;\n\t\twidth : 100%;\n}\n\nnav {\n\t\tfloat: left;\n\t\tmax-width: 160px;\n\t\tmargin: 0;\n\t\tpadding: 1em;\n}\n\nnav ul {\n\t\tlist-style-type: none;\n\t\tpadding: 0;\n}\n\t \nnav ul a {\n\t\ttext-decoration: none;\n}\n\narticle {\n\t\tmargin-left: 170px;\n\t\tborder-left: 1px solid gray;\n\t\tpadding: 1em;\n\t\toverflow: hidden;\n}\ntable {\n\t\tfont-family: arial, sans-serif;\n\t\tborder-collapse: collapse;\n\t\twidth: 80%;\n}\n\ntd, th {\n\t\tborder: 4px solid #000000;\n\t\ttext-align: middle;\n\t\tpadding: 8px;\n}\n\ntr:nth-child(even) {\n\t\tbackground-color: #eeeeee;\n}\t\n\ndiv.box {\n\t\tbackground-color: white;\n\t\twidth: 300px;\n\t\tborder: 2px solid green;\n\t\tpadding: 10px;\n\t\tmargin: 25px;\n}\n</style>\n<body>\n<div class=\"container\">\n\t<header><h1>\n\t\tIIT Kanpur Medical Labs</h1>\n\t</header>\n\t<hr>	<h2> Prescription List for the query: </h2>\n<div class=\"box\">\n"+query+"\n</div>\n<hr>")
	prescriptionList = os.listdir("prescription/")
	for prescription in prescriptionList:
		if not ".html" in prescription:
			prescriptionList.remove(prescription) 	
	rankList = [int(x.split("_")[0]) for x in prescriptionList]
	prescriptionList = [prescription for _,prescription in sorted(zip(rankList,prescriptionList))]	
	for prescription in prescriptionList:
		if ".html" in prescription:
			p = prescription.split('.')[0]		
			print(p)
			html.append("<li>\n<a href=\"file:///home/ankush/terrier-core-4.2/prescription/"+str(p)+".html\">"+str(p)+"</a>\n<hr>\n</li>\n")		
	#print(prescriptionList)
	html.append("</table>\n<div class=\"footer\"> Copyright &copy : IIT Kanpur\n</div>\t\n</div>\n</body>\n</html>")
	f.writelines(html)
if __name__== "__main__":
	main()
