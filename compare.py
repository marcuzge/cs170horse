

target = open("compare.txt","w")
olds = [line.rstrip('\n') for line in open("grades.txt")]
sams = [line.rstrip('\n') for line in open("samgrades.txt")]
news = [line.rstrip('\n') for line in open("bogogrades.txt")]
for i in range(len(olds)):
	old=olds[i]
	new = news[i]
	target.write(str(new)+" "+str(old)+"\n")
target.close()