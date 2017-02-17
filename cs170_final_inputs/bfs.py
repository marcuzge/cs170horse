import sys
class horseGraph:
	def __init__(self,filename):
		lines = [line.rstrip('\n') for line in open(filename)]
		# print(lines[0])
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
		self.pathConstruct()
	def pathConstruct(self):
		self.paths={}
		self.lpc={}
		for i in self.values.keys():
			self.paths[i]= self.longestPath(i,[i],{})
			self.lpc[i]=len(self.paths[i])
			if self.lpc[i] == len(self.values.keys()):
				return 


	def longestPath(self,start,path,maps):

		if self.neigh[start]==None or  len(self.neigh[start])==0:
			return [start]
		elif start in maps.keys():
			return maps[start]
		else:
			max = 0
			lp=[]
			for n in self.neigh[start]:
				if n not in path:
					copy = path[:]
					copy.append(n)
					subpath = self.longestPath(n,copy,maps)
					if len(subpath)>max:
						max = len(subpath)
						lp=subpath
						if max == len(self.values.keys()):
							maps[start]=lp
							return lp
			lp.insert(0,start)
			maps[start]=lp
			return lp
	def printLPC(self):
		print self.lpc
	def printLP(self):
		print self.paths
	def remove(self,path):
		if len(path) == len(self.values.keys()):
			self.values={}
			self.neigh={}
			return 
		for i in path:
			self.values.pop(i)
			self.neigh.pop(i,None)
			for k in self.neigh.keys():
				v = self.neigh[k]

				if v:
					if i in v:
						v=v.remove(i)

						self.neigh[k]=v
		self.pathConstruct()
	def getMax(self):
		max=0
		path = []
		for i in self.paths.keys():
			p=self.paths[i]
			if len(p)==len(self.paths.keys()):
				# print(p)
				return p
			if self.sumPath(p)>max:
				max= self.sumPath(p)
				path=p
		
		return p
	def sumPath(self,path):
		# if path in self.sums.keys():
		# 	return self.sums[path]
		
		sum = 0
		for i in path:
			sum += self.values[i]
			# self.sums[path]=sum
		return sum*len(path)



S= sys.stdin
def scoreCom(paths):
	sumS=0
	for path in paths:
		sumS+=(sum(path)*len(path))
	return sumS
def convertPath(paths):
	re=""
	for i in range(len(paths)):
		path  = paths[i]
		for n in range(len(path)):
			p=path[n]
			re+=str(p)
			if n !=len(path)-1:
				re+=" "
		if i !=len(paths)-1:
			re+="; "
		else:
			re+="."
	re+="\n"
	return re
target=open("591-600.out","w")
sums=0
for i in range(581,582):
	d= str(i)+".in"
	
	# for d in data:
	d= d.strip()
	fg = horseGraph(d)
	# fg.printLPC()
	
	maxpath = fg.getMax()
	path=[maxpath]
	fg.remove(maxpath)
	while len(fg.values.keys())>0:
		maxpath=fg.getMax()
		path.append(maxpath)
		fg.remove(maxpath)
	print(d)
	re = convertPath(path)
	target.write(re)
	score =scoreCom(path)
	sums+=score
	print(score)
		# fg.remove(fg.paths[1])
		# print(fg.neigh)
		# print(fg.paths)
print("total score")
print(sums)
target.close()


# lines = [line.rstrip('\n') for line in open('sample4.in')]
# n = int(line[0])
# neigh={}
# values=[]
# lines=lines[1:]
# # for line in lines:
# # 	print(line)
# for i in range(len(lines)):
# 	row = lines[i].split(" ")
# 	temp = []
# 	for j in range(len(row)):
# 		if j ==i:
# 			values.append(int(row[j]))
# 		elif row[j]=="1":
# 			temp.append(j)
# 	neigh[i]=temp

# paths={}
# lpc={}




def longestPath(start,path,maps):

	# path.append(start)
	# print(path)
	if len(neigh[start])==0:
		return [start]
	elif start in maps.keys():
		return maps[start]
	else:
		max = 0
		lp=[]
		for n in neigh[start]:
			if n not in path:
				copy = path[:]
				copy.append(n)
				subpath = longestPath(n,copy,maps)
				if len(subpath)>max:
					max = len(subpath)
					lp=subpath
		lp.insert(0,start)
		maps[start]=lp
		return lp

# for i in range(len(values)):
# 	paths[i]= longestPath(i,[i],{})
# 	lpc[i]=len(paths[i])
# 	li = paths[i]
# 	for i in range(len(li)-1):
	
# 		neighbors= neigh[li[i]]
# 		if li[i+1] not in neighbors:
# 			print li[i+1]
# 	li2=li[:]
# 	li2.sort()
# 	for i in range(len(li2)-1):
# 		if li2[i]==li2[i+1]:
# 			print "crap"
# print(paths)


	
		



