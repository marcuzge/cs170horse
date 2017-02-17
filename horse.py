import sys
import random
import os

class horseGraph:
	def __init__(self,filename, brute=False):
		lines = [line.rstrip('\n') for line in open(filename)]
		self.n = int(lines[0])
		self.nodes={}
		self.paths = []
		self.edgeCount = 0
		self.bruteForce = brute
		for i in range(1, len(lines)):
			row = lines[i].split(" ")
			for j in range(len(row)):
				if j ==i-1:
					nd = horseGraph.Node(j,int(row[j]))
					self.nodes[j] = nd

		for i in range(1, len(lines)):
			row = lines[i].split(" ")
			nd = self.nodes[i-1]
			for j in range(len(row)):
				if j != i-1 and row[j]=="1":
					self.edgeCount += 1
					nd.addneigh(self.nodes[j])

	def chooseSource(self):
		min=float('inf')
		minnode=None
		for i in self.nodes.keys():
			node=self.nodes[i]
			if node.incoming<=min:
				if node.incoming == min:
					if node.value>=minnode.value and random.random() * 2 + .5 > 1:
						minnode=node
				else:	
					min=node.incoming
					minnode=node
		return minnode

	def smallGraphSearch(self):
		while len(self.nodes) > 0:
			self.paths.append(self.getMax())
			self.deletePath(self.paths[-1])
			
	def getMax(self):
		max=0
		path = None
		allPaths = self.findAllPaths()
		for i in allPaths:
			sum = self.sumPath(i)
			if i and sum > max:
				max= sum
				path = i
		if not path:
			for i in self.nodes:
				return [self.nodes[i]]
		return path
	
	def findAllPaths(self):
		allPaths = []
		for n in self.nodes.values():
			allPaths.append(self.longestPath(n, []))
		return allPaths
		
	def longestPath(self,start, maps):
		if maps and len(start.neighbors) ==0:
			return [start]
		else:
			max = 0
			maxp = []
			path = [start]
			for n in start.neighbors:
				if n not in maps:
					copy = maps[:]
					copy.append(start)
					subpath = self.longestPath(n,copy)
					if subpath and len(subpath)>max:
						max = len(subpath)
						maxp = subpath
						if max + 1 == len(self.nodes):
							maps.extend(maxp)
							path.extend(maxp)
							return path
			maps.extend(maxp)
			path.extend(maxp)
			return path
		
	def searchPath(self, p=0.5):
		# maybe call searchPath on different start vertices, or diff p value and take the max
		if self.bruteForce:
			self.smallGraphSearch()
			return
		start = self.chooseSource()
		path = []
		pathset = set()
		
		while len(self.nodes) > 0:
			if start is None:
				start = self.chooseSource()
				if start not in pathset:
					path.append(start)
					pathset.add(start)
				else:
					self.paths.append(path)
					self.deletePath(path)
					path = []
					pathset = set()
					start = None
					continue
			elif start not in pathset:
				path.append(start)
				pathset.add(start)
			else:
				self.paths.append(path)
				self.deletePath(path)
				path = []
				pathset = set()
				start = None
				continue
			if start.neighbors == 0 or len(path) == self.n:
				self.paths.append(path)
				self.deletePath(path)
				path = []
				pathset = set()
				start = None
			else:
				bestNeighbor = None
				for neighbor in start.neighbors:
					if (bestNeighbor is None or neighbor.compute() > bestNeighbor.compute()) and neighbor not in pathset:
						bestNeighbor = neighbor
				if bestNeighbor is None:
					self.paths.append(path)
					self.deletePath(path)
					path = []
					pathset = set()
					start = None
				else:
					start = bestNeighbor
			
	def deletePath(self,path):
		if not path:
			return
		for node in path:
			self.nodes.pop(node.id)
			for i in self.nodes.keys():
				nd = self.nodes[i]
				nd.remove(node)
				
	def printLP(self, filename):
		with open(filename, 'a') as f:
			try:
				countP = 0
				countN = 0
				for path in self.paths:
					countP += 1
					for n in path:
						countN += 1
						if countP < len(self.paths) or countN < len(path):
							f.write(str(n.id) + " ")
						else:
							f.write(str(n.id) + ".")
					countN = 0
					if countP < len(self.paths):
						f.write('; ')
				f.write('\n')
			except:
				f.write("FAILED! \n")
				pass
	
	def sumPath(self,path):
		sum = 0
		for i in path:
			sum += i.value
		return sum * len(path)
	
	def finalScore(self, paths):
		score = 0
		nodesVisited = 0
		for path in paths:
			nodesVisited += len(path)
			score += self.sumPath(path)
		if nodesVisited == self.n:
			return score
		else:
			raise Exception()

	class Node:
		def __init__(self, id,value):
			self.id= id
			self.value = value
			self.neighbors = set()
			self.incoming =0
			self.score = -1
		
		def addneigh(self,neigh):
			self.neighbors.add(neigh)
			neigh.incrementInDegree()
		
		def incrementInDegree(self):
			self.incoming+=1
		
		def remove(self,neigh):
			if neigh in self.neighbors:
				self.neighbors.remove(neigh)
				neigh.decrementInDegree()
				if self.score != -1:
					self.score = -1
		
		def decrementNeigh(self,neigh):
			for node in self.neighbors:
				node.decrementInDegree()

		def decrementInDegree(self):
			self.incoming-=1
		
		def compute(self, p=0.5):
			if self.score == -1:
				# re-compute the score because we have removed nodes from the graph
				self.score = self.value*p + len(self.neighbors)*(1-p)
				#self.score += self.scoreOfBestPath(path)
			return self.score
		
		def __repr__(self):
			return str(self.id)
		
# 		def scoreOfBestPath(self, path):
# 			"""
# 			Find the best path starting at this node (self) and going for doing "depth" levels.
# 			Will make sure not to include nodes in the path already.
# 
# 			"""
# 			bestPath = 0
# 			for n in self.neighbors:
# 				if n not in path:
# 					lp = self.longestPath(self, n, path, [])
# 					lp.append(self)
# 					sum = self.sumPath(lp)
# 					if sum > bestPath:
# 						bestPath = sum
# 			return bestPath
# 
# 		def longestPath(self, parent, start, path, lp, depth=2):
# 			"""
# 			Find the best path starting at this node (self) and going for doing "depth" levels.
# 			Will make sure not to include nodes in the path already.
# 
# 			"""
# 			if start is not parent and start not in path and depth > 0:
# 				lp.append()
# 			else:
# 				max = 0
# 				lp=[]
# 				for n in self.neigh[start]:
# 					if n not in path:
# 						copy = path[:]
# 						copy.append(n)
# 						subpath = self.longestPath(n,copy,maps)
# 						if len(subpath)>max:
# 							max = len(subpath)
# 							lp=subpath
# 				lp.insert(0,start)
# 				maps[start]=lp
# 				return lp

if __name__ == "__main__":
	#data = [str(i) for i in range(1, 51)]
	data = ["10"]
	output_file = "sam-test.out"
	open(output_file, 'w').close()
	for d in data:
		f = "cs170_final_inputs/" + d + ".in"
		#f = d + ".in"
        # maybe run it like 3 times and take the best
		fg = horseGraph(f)
		fg.searchPath()
		
		if fg.edgeCount <= 87:
			print fg.edgeCount
			fg2 = horseGraph(f, True)
			fg2.searchPath()
			if fg2.finalScore(fg2.paths) > fg.finalScore(fg.paths):
				fg2.printLP(output_file)
				print fg2.finalScore(fg2.paths)
			else:
				fg.printLP(output_file)
				print fg.finalScore(fg.paths)
		else:
			fg.printLP(output_file)
			print fg.finalScore(fg.paths)
