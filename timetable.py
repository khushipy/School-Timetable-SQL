#timetable
prayer_s=input('prayer starts:')
prayer_e=input('prayer ends:')

b=int(prayer_e[0])
x= int(prayer_e[2::])

prayer_time=int(input("prayer time"))
#period_time=40
#recess=30
if prayer_time >20:
  a=340-prayer_time
  period_time=int(a/8)
print("each period is of",period_time)  
y=x+period_time

if y>60:
  b+=1
  y=y-60
firstp=(str(b)+':'+str(y))

b=int(firstp[0])
x= int(firstp[2::])
y=int(x+period_time)

if y>60:
  b=int(b)
  b+=1
  y=y-60
secondp=(str(b)+':'+str(y))


if int(b)%10>=0:
  x= int(secondp[2::])
else:
  
  x= int(secondp[1::])
print(x)  
b=int(secondp[0:1])
y=int(x+period_time)

if y>60:
  b=int(b)
  b+=1
  y=y-60
thirdp=(str(b)+':'+str(y))
if int(b)%10>=1:
  x= int(thirdp[2::])
else:
  
  x= int(thirdp[3::])
print(x)
b=int(thirdp[0:2])


y=int(x+period_time)

if y>60:
  b=int(b)
  b+=1
  y=y-60
forthp=(str(b)+':'+str(y))
if int(b)%10>=1:
  x= int(forthp[2::])
else:
  
  x= int(forthp[3::])

b=int(forthp[0:2])


y=int(x+30)
if y>60:
  b=int(b)
  b+=1
  y=y-60
recess=(str(b)+':'+str(y))
if int(b)%10>=1:
  x= int(recess[3::])
else:
  
  x= int(recess[2::])



b=int(recess[0:2])


y=int(x+period_time)

if y>60:
  b=int(b)
  b+=1
  y=y-60
fifthp=(str(b)+':'+str(y))
if int(b)%10>=1:
  x= int(fifthp[3::])
else:
  
  x= int(fifthp[2::])


b=int(fifthp[0:2])



y=int(x+period_time)

if y>60:
  b=int(b)
  b+=1
  y=y-60
sixthp=(str(b)+':'+str(y))
if int(b)%10>=1:
  x= int(sixthp[3::])
else:
  
  x= int(sixthp[2::])

b=int(sixthp[0:2])



y=int(x+period_time)

if y>60:
  b=int(b)
  b+=1
  y=y-60
seventhp=(str(b)+':'+str(y))
if int(b)%10>=1:
  x= int(seventhp[3::])
else:
  
  x= int(seventhp[2::])
b=int(seventhp[0:2])
y=int(x+period_time)

if y>60:
  b=int(b)
  b+=1
  y=y-60
eighthp=(str(b)+':'+str(y))  


print("prayer",'=',prayer_s,'-',prayer_e)
print("1st period",'=',prayer_e,'-',firstp)
print("2nd period",'=',firstp,'-',secondp)
print("3rd period",'=',secondp,'-',thirdp)
print("4th period",'=',thirdp,'-',forthp)
print('RECESS','=',forthp,'-',recess)
print('5th period','=',recess,'-',fifthp)
print('6th period','=',fifthp,'-',sixthp)
print('7th period','=',sixthp,'-',seventhp)
print('8th period','=',seventhp,'-',eighthp)






