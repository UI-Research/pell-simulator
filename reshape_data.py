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

def formatter(row, header, precision):
	if precision == 0:
		return str(int(float(row[h[header]])))
	else:
		return str(round(float(row[h[header]]),precision))

for row in cr:
	rh = ""

# TO BE REMOVED
	# if(row[h["a"]] != "4000" and row[h["a"]] != "6000"):
	# 	continue
#################

	if row[h["b"]] == "":
		rh = "s1" + row[h["a"]]
	else:
		rh = "s2" + row[h["a"]] + formatter(row, "b", 1) + formatter(row, "c", 1)
		

	# print rh
	rHead.append(rh + "p")
	rHead.append(rh + "d")
	if row[h["a"]] == "4000" and row[h["b"]] == "":
		rHead.append(rh + "pb")
		rHead.append(rh + "db")

	reshaped[rh] = {}

	for r in rows:
		if r[2] == "1yr":
			r.append(formatter(row, "pell_cost_1year", 2))
			r.append(formatter(row, "pell_cost_1year", 2))
			if row[h["a"]] == "4000" and row[h["b"]] == "":
				r.append(formatter(row, "pell_cost_1year_baseline", 2))
				r.append(formatter(row, "pell_cost_1year_baseline", 2))
		elif r[2] == "10yr":
			r.append(formatter(row, "pell_cost_10year", 2))
			r.append(formatter(row, "pell_cost_10year", 2))
			if row[h["a"]] == "4000" and row[h["b"]] == "":
				r.append(formatter(row, "pell_cost_10year_baseline", 2))
				r.append(formatter(row, "pell_cost_10year_baseline", 2))
		elif r[2] == "avg":
			r.append(formatter(row, "receive_pell", 3))
			r.append(formatter(row, "pell_avg", 0))
			if row[h["a"]] == "4000" and row[h["b"]] == "":
				r.append(formatter(row, "receive_pell_baseline", 3))
				r.append(formatter(row, "pell_avg_baseline", 0))
		else:
			r.append(formatter(row, "receive_pell" + r[2] , 3))
			r.append(formatter(row, "pell_avg" + r[2] , 0))
			if row[h["a"]] == "4000" and row[h["b"]] == "":
				r.append(formatter(row, "receive_pell" + r[2] + "_baseline", 3))
				r.append(formatter(row, "pell_avg" + r[2] + "_baseline", 0))
	# r.append()

# print rHead
cw.writerow(rHead)

for r in rows:
	cw.writerow(r)
