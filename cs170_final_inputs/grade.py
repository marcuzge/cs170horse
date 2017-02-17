class horseGraph:
	def __init__(self,filename):
		lines = [line.rstrip('\n') for line in open(filename)]
		n = int(line[0])
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
		sum =0 
		for path in paths:
			temp = 0
			for p in path:
				temp+=self.values[p]
			sum+=temp*len(path)
		return sum
filen = "all.out"
lines = [line.rstrip('\n') for line in open(filen)]
total = 0
gradebook = open("grades.txt","w")
gradebook.write("\n")
for i in range(1,len(lines)):
	input = "cs170_final_inputs/"+str(i)+".in"
	fg = horseGraph(input)
	path = lines[i]
	gd = fg.grade(path)
	print gd
	total+=gd
	gradebook.write(str(gd)+"\n")
gradebook.close()



