import csv
tb=open('timet.csv','a')
n=int(input("no of periods per day"))
o=['D/P',1,2,3,4,5,6,7,8]
writer=csv.writer(tb)
writer.writerow(o)
def d(k):
  l.append(k)
  for i in range(n):
    l.append('')
l,msub_list,esub_list=[],[],[]
l1=['monday','tuesday','wednesday','thursday','friday','saturday']
for i in l1:
  k=i
  d(k)
msub=int(input('How many main subjects?'))
esub=int(input('How many other subjects?'))
print('ENTER THE MAIN SUBJECTS')
for i in range(msub):
  mb=input()
  msub_list.append(mb)
print('ENTER THE EXTRA SUBJECTS (expect-games/practical)')  
for i in range(esub):
  eb=input()
  esub_list.append(eb)  
s=l.index('tuesday') 
mon,tue,wed,thur,fri,sat=l[:s:],l[s:2*s:],l[2*s:3*s:],l[3*s:4*s:],l[4*s:5*s:],l[5*s:6*s:]
B=[mon,tue,wed,thur,fri,sat]
h1=msub_list[:len(msub_list)//2:]
h2=msub_list[len(msub_list)//2::]
if len(h2)>=len(h1):
  for i in B:
    i[1],i[2],i[3]=h2[0],h2[1],h2[2]
    i[5],i[6]=h1[0],h1[1]

for i in B[:-1:]:
  i[-1]='practical'
  i[-2]='practical'
  sat[-2],sat[-1]='games','games'
      
  
for i in B:
  writer=csv.writer(tb)
  writer.writerow(i)

tb.close()
