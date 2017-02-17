# filename = "1-50.out"
# lines = [line.rstrip('\n') for line in open(filename)]
import os
try:
	os.remove("bogoall.out")
except OSError:
	print("")
target=open("bogoall.out","w")
# samTarget=open("sam.out","w")
for i in range(1,601):
	filename = "david_test/"+str(i)+".out"
	line = [line.rstrip('\n') for line in open(filename)][0]
	target.write(line+"\n")
	# filename = "sam_outputs/"+str(i)+".out"
	# line = [line.rstrip('\n') for line in open(filename)][0]
	# samTarget.write(line+"\n")
target.close()
# target.write("\n")
# for line in lines:
# 	line= line.replace(".","")
# 	target.write(line+"\n")
# filename = "51-150.out"
# lines = [line.rstrip('\n') for line in open(filename)]
# for line in lines:
# 	line= line.replace(".","")
# 	target.write(line+"\n")

# filename = "151-250.out"
# lines = [line.rstrip('\n') for line in open(filename)]
# for line in lines:
# 	line= line.replace(".","")
# 	target.write(line+"\n")
# filename = "251-350.out"
# lines = [line.rstrip('\n') for line in open(filename)]
# for line in lines:
# 	line= line.replace(".","")
# 	target.write(line+"\n")
# filename = "351-400.out"
# lines = [line.rstrip('\n') for line in open(filename)]
# for line in lines:
# 	line= line.replace(".","")
# 	target.write(line+"\n")
# filename = "401-500.out"
# lines = [line.rstrip('\n') for line in open(filename)]
# for line in lines:
# 	line= line.replace(".","")
# 	target.write(line+"\n")

# filename = "501-600.out"
# i = 501
# lines = [line.rstrip('\n') for line in open(filename)]
# for line in lines:
# 	if i == 581:
# 		line = [line.rstrip('\n') for line in open("591-600.out")][0]
# 		line= line.replace(".","")
# 		target.write(line+"\n")
# 	else:
# 		line= line.replace(".","")
# 		target.write(line+"\n")
# 	i+=1

# filename = "582-600.out"
# lines = [line.rstrip('\n') for line in open(filename)]
# for line in lines:
# 	line= line.replace(".","")
# 	target.write(line+"\n")
# target.close()
	
# 	