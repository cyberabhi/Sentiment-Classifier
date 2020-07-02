#positive words file
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
#negative words file
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
#strip punctuations
def strip_punctuation(s):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    for i in s:
        if i in punctuation_chars:
             s = s.replace(i,"")
    return s    
#positive words count    
def get_pos(p):
    str = p.split(" ")
    li = []
    for i in str:
        li.append(strip_punctuation(i))
    cnt = 0
    for j in li:
        if j.lower() in positive_words:
            cnt+=1
    return cnt    
#negative words count  
def get_neg(p):
    str = p.split(" ")
    li = []
    for i in str:
        li.append(strip_punctuation(i))
    cnt = 0
    for j in li:
        if j.lower() in negative_words:
            cnt+=1
    return cnt
#reading file and operating
file = open("project_twitter_data.csv","r")
lines = file.readlines()
ls = []
for x in lines:
	ls.append(x.replace("\n","").split(","))
#calculation
for i in ls[1:]:
	i.extend([get_pos(i[0]),get_neg(i[0]),(get_pos(i[0])-get_neg(i[0]))])
	i[-3]=str(i[-3])
	i[-2]=str(i[-2])
	i[-1]=str(i[-1])
com = []
for j in ls[1:]:
	com.append(",".join(j[1:]))
#writing into new csv
outfile = open("resulting_data.csv","w")
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')
for i in range(0,len(com)):
	outfile.write(com[i])
	outfile.write("\n")
outfile.close()
f = open("resulting_data.csv","r")
c = f.read()
print(c)
