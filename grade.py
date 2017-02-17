class horseGraph:
	def __init__(self,filename):
		lines = [line.rstrip('\n') for line in open(filename)]
		n = int(lines[0].strip())
		self.neigh={}
		self.values={}
		lines=lines[1:]
		self.paths={}
		self.lpc={}
		self.sums={}
		for i in range(len(lines)):
			row = lines[i].split(" ")
			temp = []
			for j in range(len(row)):
				if j ==i:
					self.values[j]= int(row[j])
				elif row[j]=="1":
					temp.append(j)
			self.neigh[i]=temp
	def grade(self,paths):
		sumt =0 
		temp = []
		arr = paths.split("; ")
		for p in arr:
			word = p.split();
			for w in word:
				temp.append(self.values[int(w)])
			sumt+=sum(temp)*len(temp)
			temp=[]
		return sumt
		# for s in word:
		# 	s=s.strip()
		# 	if s == " ":
		# 		continue
		# 	elif ";" in s:
		# 		s = s[:-1]
		# 		s = s.split()
		# 		temp.append(self.values[int(s)])
		# 		sumt+=sum(temp)*len(temp)
		# 		# print(temp)
		# 		temp=[]
		# 	elif "." in s:
		# 		s = s[:-1]
		# 		temp.append(self.values[int(s)])
		# 		sumt+=sum(temp)*len(temp)	
		# 		return sumt
		# 	else:
		# 		temp.append(self.values[int(s)])
		# sumt+=sum(temp)*len(temp)
		# return sumt
def converpath(spath):
	result = [[]]
	temp = []
	for s in spath:
		if s == " ":
			continue
		elif s == ";":
			result.append(temp)

			temp =[]
		elif s == ".":
			result.append(temp)
			result = result[1:]
			return result
		else:
			temp.append(s)



filen = "bogoall.out"
lines = [line.rstrip('\n') for line in open(filen)]
sfilen = "sam.out"
slines = [line.rstrip('\n') for line in open(sfilen)]

total = 0
import os
os.remove("bogogrades.txt")
gradebook = open("bogogrades.txt","w")
samGradeBook= open("samgrades.txt","w")
bestSolution = open("best.txt","w")
grade=open("grades.txt","w")

# gradebook.write("\n")
# print()
bogo =0 
sam =0 
tie = 0 
for i in range(0,len(lines)):
	input = "cs170_final_inputs/"+str(i+1)+".in"
	fg = horseGraph(input)
	bogopath = lines[i]
	bogopath=bogopath.replace(".","")
	sampath = slines[i]

	bogogd = fg.grade(bogopath)
	samgd = fg.grade(sampath)

	singleOutput=open("bestOutputs/"+str(i+1)+".out","w")

	if bogogd>=samgd:

		if bogogd == samgd:
			bogo-=1
			tie+=1
		# if i == 211:
		# 	print(bogopath)

		bestSolution.write(bogopath+"\n")
		singleOutput.write(bogopath+"\n")
		# if bogogd == samgd:
		# 	tie+=1
	
		bogo+=1
	else:
		# if i == 211:
		# 	print(bogopath)
		# 	print(sampath)
		bestSolution.write(sampath+"\n")
		singleOutput.write(sampath+"\n")
		sam+=1
	total+=max(bogogd,samgd)
	grade.write(str(max(bogogd,samgd))+"\n")
	gradebook.write(str(bogogd)+"\n")
	samGradeBook.write(str(samgd)+"\n")

gradebook.close()
samGradeBook.close()
print(total)
print("bogo wins "+str(bogo))
print("sam wins "+ str(sam))
print("tie "+str(tie))


