import random

#input is the file we are trying to work on
#output is the output and where we keep track of our current best
#times is how many times we run this

def func(input, output, times):
	lines = [line.rstrip('\n') for line in open("cs170_final_inputs/"+input)]
	n = int(lines[0])
	friendships = {}
	values = []
	lines = lines[1:]
	for i in range(len(lines)):
		row = lines[i].split(" ")
		temp = []
		for j in range(len(row)):
			if j == i:
				values.append(int(row[j]))
			if row[j] == "1":
				temp.append(j)
			friendships[i] = temp
	worst = sum(values)
	best = worst * n

	try:
		curr_best = [line.rstrip('\n') for line in open("david_test/"+output)][0]
		curr_best = grade(curr_best, values)
	except IOError:
		curr_best = 0

	updateBool = False
	if curr_best < best:
		now_best = bogo(times, n, friendships, values, best)
		now_best_val = grade(now_best, values)
		if now_best_val > curr_best:
			with open("david_test/"+output, 'w') as f:
				f.write(now_best) 
				print(output[:len(output)-4] + " completed and UPDATED. Improvement: " + str(now_best_val-curr_best))
				updateBool = True
	if (not updateBool):
		print(input[:len(input)-3] + " completed.")

def grade(sequence, values):
	arr = sequence[:len(sequence)-1]
	arr = arr.split("; ")
	if len(arr) == 1:
		return sum(values)*len(sequence)
	for i in range(len(arr)):
		arr[i] = arr[i].split(" ")
		arr[i] = list(map(int, arr[i]))
	score = 0
	for i in arr:
		temp = 0
		for j in i:
			temp += values[j]
		score += (temp * len(i))
	return score

def bogo(times, n, friendships, values, best):
	ans = {}
	seen = []
	for i in range (times):
		seen = []
		friendships2 = friendships.copy()
		node = int(random.random()*n)
		path = ""
		while len(seen) < n:
			while node in seen:
				node = int(random.random()*n)
			seen.append(node)
			path += str(node)
			delete(friendships2, node)
			while len(friendships2[node]) > 0:
				while node in seen:
					r = int(random.random()*len(friendships2[node]))
					node = friendships2[node][r]
				seen.append(node)
				path += (" "+str(node))
				delete(friendships2, node)
			path += "; "
		path = path[:len(path)-2]
		path += "."
		ans[path] = grade(path, values)
		if ans[path] == best:
			return path
	return max(ans, key=ans.get)

def delete(friend, x):
	for i in friend:
		friend[i] = [z for z in friend[i] if z != x]

def test(start, end, times):
	for i in range(start, end+1):
		a = str(i) + ".in"
		b = str(i) + ".out"
		func(a, b, times)

test(356,600,500)

