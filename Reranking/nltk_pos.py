import nltk
fw=open('5.txt','w')
fw2=open('6.txt','w')
nltk.data.path=['/scratch/cluster/nltk/']
f=open('/scratch/cluster/1.txt','r')
for line in f:
    a=nltk.pos_tag(nltk.word_tokenize(line))
    if len(a)>0:
        for l in range(len(a)-1):
            fw.write(a[l][0]+' ')
            fw2.write(a[l][1]+' ')
        
        fw.write(a[len(a)-1][0]+'\n')
        fw2.write(a[len(a)-1][1]+'\n')
    else:
        fw.write('<b>\n')
        fw2.write('<b>\n')