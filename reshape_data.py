import csv

cr = csv.reader(open("data/source/all_simulations.csv","rU"))
cw = csv.writer(open("data/data.csv","wb"))

head = cr.next()

h = {}
for i,s in enumerate(head):
	h[s] = i

cats = {"cost":[], "none":[""],"income": ["1", "2", "3", "4", "5"], "parentsEd" : ["6", "7", "8", "9"], "race": ["10","11","12","13","14"], "instType": ["15","16","17","18"], "benefits": ["20","21"], "indep": ["22","23"]}

rows = [["num", "cost", "1yr"], ["num", "cost", "10yr"], ["num","avg",""],["bar","income","1"],["bar","income","2"],["bar","income","3"],["bar","income","4"],["bar","income","5"],["bar","parentsEd","6"],["bar","parentsEd","7"],["bar","parentsEd","8"],["bar","parentsEd","9"],["bar","race","10"],["bar","race","11"],["bar","race","12"],["bar","race","13"],["bar","race","14"],["bar","instType","15"],["bar","instType","16"],["bar","instType","17"],["bar","instType","18"],["bar","benefits","20"],["bar","benefits","21"],["bar","indep","22"],["bar","indep","23"]]

reshaped = {}
rHead = ["type","category","subcategory"]
# for key,val in cats.iteritems():
# 	print key,val

for row in cr:
	rh = ""
	if row[h["b"]] == "":
		rh = "s1_" + row[h["a"]]
	else:
		rh = "s2_" + row[h["a"]] + "_" + row[h["b"]] + "_" + row[h["c"]]

	# print rh
	rHead.append(rh + "_percent")
	rHead.append(rh + "_dollars")
	rHead.append(rh + "_percent_baseline")
	rHead.append(rh + "_dollars_baseline")

	reshaped[rh] = {}

	for r in rows:
		if r[2] == "1yr":
			r.append(row[h["pell_cost_1year"]])
			r.append(row[h["pell_cost_1year"]])
			r.append(row[h["pell_cost_1year_baseline"]])
			r.append(row[h["pell_cost_1year_baseline"]])
		elif r[2] == "10yr":
			r.append(row[h["pell_cost_10year"]])
			r.append(row[h["pell_cost_10year"]])
			r.append(row[h["pell_cost_10year_baseline"]])
			r.append(row[h["pell_cost_10year_baseline"]])
		elif r[2] == "avg":
			r.append(row[h["receive_pell"]])
			r.append(row[h["pell_avg"]])
			r.append(row[h["receive_pell_baseline"]])
			r.append(row[h["pell_avg_baseline"]])
		else:
			r.append(row[h["receive_pell" + r[2] ]])
			r.append(row[h["pell_avg" + r[2] ]])
			r.append(row[h["receive_pell" + r[2] + "_baseline"]])
			r.append(row[h["pell_avg" + r[2] + "_baseline"]])
	# r.append()

# print rHead
cw.writerow(rHead)

for r in rows:
	cw.writerow(r)
