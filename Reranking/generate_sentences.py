import random
mf=1
ff='5.txt'
fft='6.txt'
f=open(ff,'r')
fp=open(fft,'r')
fw=open('5testod.txt','w')
fw2=open('5testmd.txt','w')
v=dict()
u=0
v2=dict()
u2=0
for line in f:
    line=line.replace("?",",")
    line=line.replace("!",",")
    line=line.replace(".",",")
    line=line.rstrip().lstrip().split()
    line2=fp.readline()
    line2=line2.rstrip().lstrip().split()
    for k in range(len(line2)):
        if line2[k]=='CC':
            line[k]=","
    strr=""
    vq=0
    for k in range(len(line)):
        if line[k]==",":
            strr=strr.rstrip().lstrip()
            if len(strr)>10 and len(strr)<50:
                if vq==1:
                    v[u]=strr
                    u=u+1
                else:
                    v2[u2]=strr
                    u2=u2+1
            strr=""
            vq=0
        else:
            strr=strr+' '+line[k]
        if line2[k][0]=='V':
            vq=1
f.close()
fp.close()
f=open(ff,'r')
fp=open(fft,'r')
for line in f:
    line=line.replace("?",",")
    line=line.replace("!",",")
    line=line.replace(".",",")
    line=line.rstrip().lstrip().split()

    line2=fp.readline()
    line2=line2.rstrip().lstrip().split()
    cl=[]
    vvv=[]
    vvq=0
    for k in range(len(line)):
        if line2[k] ==',' or line2[k] =='.' or line2[k] =='CC':
            cl.append(line[k])
            line[k]='.'
            vvv.append(vvq)
            vvq=0
        if line2[k][0]=='V':
            vvq=1
    vvv.append(vvq)
    line=' '.join(line)
    line=line.split('.')
    v2o=""
    if len(line[-1])==0:
        line=line[:-1]
        cl=cl[:-1]    
    for k in range(len(line)-1):
        v2o=v2o+line[k].rstrip().lstrip()+' '+cl[k]+' '
    v2o=v2o+line[-1].rstrip().lstrip()
    if len(line)>-1:
        fw.write(v2o.rstrip().lstrip()+" .\n")
    if len(line)>1:
        for sss in range(5*mf):
            linee=line.copy()
            
            rrw=random.randint(0,len(line)-1)
            ppa=0
            while len(linee[rrw])<2:
                rrw=random.randint(0,len(line)-1)
                ppa=ppa+1
                if ppa>50:
                    break
            
            if vvv[rrw]==1:
                linee[rrw]=v[random.randint(0,len(v)-1)]
            else:
                linee[rrw]=v2[random.randint(0,len(v2)-1)]
            v2m=""
            for k in range(len(line)-1):
                v2m=v2m+linee[k].rstrip().lstrip()+' '+cl[k]+' '
            v2m=v2m+linee[-1].rstrip().lstrip()
            fw2.write(v2m.rstrip().lstrip()+" .\n")
f.close()
fp.close()

dd=dict()
ddc=dict()
for line in ['CD','DT','FW','IN','JJ','MD','NN','PDT','PRP','PRP$','RB','RP','VB','WDT','WP','WRB']:
    dd[line]=dict()
    ddc[line]=0
u=0
f=open(ff,'r')
fp=open(fft,'r')
for line in f:
    line=line.rstrip().lstrip()
    line=line.replace("?",",")
    line=line.replace("!",",")
    line=line.replace(".",",")
    line=line.split(' ')
    line2=fp.readline()
    line2=line2.rstrip().lstrip().split()
    if line[-1]==',':
        line=line[:-1]
    for k in range(len(line)):
        if line2[k]=='NNS' or line2[k]=='NNP' or line2[k]=='NNPS':
            line2[k]='NN'
        if line2[k]=='VBD' or line2[k]=='VBG' or line2[k]=='VBN'or line2[k]=='VBP'or line2[k]=='VBZ':
            line2[k]='VB'
        if line2[k]=='RBR' or line2[k]=='RBS':
            line2[k]='RB'
        if line2[k]=='JJS' or line2[k]=='JJR':
            line2[k]='JJ'
        if line2[k] in dd:
            dd[line2[k]][ddc[line2[k]]]=line[k]
            ddc[line2[k]]=ddc[line2[k]]+1    
f.close()
fp.close()
f=open(ff,'r')
fp=open(fft,'r')
for line in f:
    line=line.rstrip().lstrip()
    line=line.replace("?",",")
    line=line.replace("!",",")
    line=line.replace(".",",")
    line=line.split(' ')
    line2=fp.readline()
    line2=line2.rstrip().lstrip().split()
    if line[-1]==',':
        line=line[:-1]
    for k in range(len(line)):
        for kk in range(1*mf):
            if line2[k]=='NNS' or line2[k]=='NNP' or line2[k]=='NNPS':
                line2[k]='NN'
            if line2[k]=='VBD' or line2[k]=='VBG' or line2[k]=='VBN'or line2[k]=='VBP'or line2[k]=='VBZ':
                line2[k]='VB'
            if line2[k]=='RBR' or line2[k]=='RBS':
                line2[k]='RB'
            if line2[k]=='JJS' or line2[k]=='JJR':
                line2[k]='JJ'
            if line2[k] in dd:
                linee=line.copy()
                linee[k]=dd[line2[k]][random.randint(0,len(dd[line2[k]])-1)]
                v2m=" ".join(linee)
                if random.random()<0.5:
                    fw2.write(v2m.rstrip().lstrip()+" .\n")
f.close()
fp.close()
