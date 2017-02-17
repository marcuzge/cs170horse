def reverseString(s):
    result = ""
    for c in s:
        print(result)
        if c == "(":
            result= ")"+result
        elif c == ")":
            result = "("+result
        else:
            result = c+result


    return result

def simp(s):
  
    if s [0]=="(":
        s = s[1:]
    index = s.index(")")
    s=s[:index]+s[index+1:]
    left =[]
    right =[]
    result = ""
    first = True
    for i in range(len(s)):
        
        if s[i]=="(":
            if first:
                result +=s[0:i+1]
                first = False
            left.append(i)
        if s[i] ==")":
            right.append(i)
            if len(left) == len(right):
                le = left[0]
                sub = s[le+1:i]
                newsub = simp(sub)
                result +=newsub
                left=[]
                right = []
    if first:
        return s
    return result
import sys
filename= "input002.txt"
lines = [line.rstrip('\n') for line in open(filename)]
for line in lines:
    print line
    segs = line.split("/")
    if len(segs)==1:
        print seg[0]
    else:
        inp = segs[0]
        act = segs[1]
        for c in act:
            print("input: "+inp+" "+act)
            if act =='R':
                inp = reverseString(inp)
            if act == 'S':
                inp = simp(inp)
        print input