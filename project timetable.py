import mysql.connector


myconn=mysql.connector(host="localhost",user='root',password="khushipal08")
myconn.close()
#creating database and table
mycursor=myconn.cursor()
mycursor.execute("create database if not exists timetable_manage")
mycursor.execute("use timetable_manage")
mycursor.execute("create table if not exists timetable(timetable_id int,Day varchar(20),period varchar(20),subject varchar(50),teacher varchar (50))")

#teacher table 1
mycursor=myconn.cursor()
mycursor.execute("create database if not exists timetable_manage")
mycursor.execute("use timetable_manage")
mycursor.execute("create table if not exists teachers_table1(teacher_name varchar(20),Day varchar(20),period varchar(20),schedule varchar (10))")    
myconn.commit()
    
#teacher table 2
mycursor.execute("use timetable_manage")
mycursor.execute("create table if not exists teachers_table2(teacher_name varchar(20),Day varchar(20),period varchar(20),schedule varchar (10))")    
myconn.commit()
    
#teacher table 3
mycursor.execute("use timetable_manage")
mycursor.execute("create table if not exists teachers_table3(teacher_name varchar(20),Day varchar(20),period varchar(20),schedule varchar (10))")    
myconn.commit()
    
#teacher table 4
mycursor.execute("use timetable_manage")
mycursor.execute("create table if not exists teachers_table4(teacher_name varchar(20),Day varchar(20),period varchar(20),schedule varchar (10))")    
myconn.commit()
    

#teacher table 5
mycursor.execute("use timetable_manage")
mycursor.execute("create table if not exists teachers_table5(teacher_name varchar(20),Day varchar(20),period varchar(20),schedule varchar (10))")    
myconn.commit()
    

#teacher table 6
mycursor.execute("use timetable_manage")
mycursor.execute("create table if not exists teachers_table6(teacher_name varchar(20),Day varchar(20),period varchar(20),schedule varchar (10))")    
myconn.commit()
    

#teacher table 7
mycursor.execute("use timetable_manage")
mycursor.execute("create table if not exists teachers_table7(teacher_name varchar(20),Day varchar(20),period varchar(20),schedule varchar (10))")    
myconn.commit()
    
    
#teacher table 8
mycursor.execute("use timetable_manage")
mycursor.execute("create table if not exists teachers_table8(teacher_name varchar(20),Day varchar(20),period varchar(20),schedule varchar (10))")    
myconn.commit()
    

#teacher table 9
mycursor.execute("use timetable_manage")
mycursor.execute("create table if not exists teachers_table9(teacher_name varchar(20),Day varchar(20),period varchar(20),schedule varchar (10))")    
myconn.commit()
    

#teacher table 10
mycursor.execute("use timetable_manage")
mycursor.execute("create table if not exists teachers_table10(teacher_name varchar(20),Day varchar(20),period varchar(20),schedule varchar (10))")    
myconn.commit()

#arrangement table         
mycursor.execute("use timetable_manage")
mycursor.execute("create table if not exists arrangement(arrange_id int,Day varchar(20),period varchar(20),teacher varchar (50))")




display_option='''Please Enter your Choice:
1. To insert Record.
2. To Display Record.
3. To update Record.
4. Arrangement
5. To display arrangement
6. To display time
'''


print(display_option)
choosed_option=input()
if(choosed_option == '1'):
    
     
    day=input("Please Enter Day Name:")
    period=input("Please Enter period:")
    subject=input("Please Enter subject Name:")
    teacher=input("Please Enter teacher Name:")
    insert_qry="Insert into timetable (Day ,period ,subject ,teacher) values('"+day+"','"+period+"','"+ subject  +"','" +teacher+"')"
    mycursor.execute(insert_qry)
    print("Record Insert Successfully")
    myconn.commit()
if (choosed_option == '2'):
    day=input("Please Enter Day Name:")


    display_qry="SELECT * FROM timetable WHERE day='"+day+"'"
    mycursor.execute(display_qry)
    v=mycursor.fetchall()
    print(v)
    myconn.commit()
     
if (choosed_option == '3') :
      
    day=input("Please Enter Day Name:")
    period=input("Please Enter period:")
    subject=input("Please Enter subject Name:")
    teacher=input("Please Enter teacher Name:")
    timetable_id=(input('please enter timetable_id:'))
    
    update_qry ="UPDATE  timetable SET day='"+day +"',period='"+period+"',subject='"+subject+"',teacher='"+teacher+"'WHERE timetable_id='"+timetable_id+"'" 
    mycursor.execute(update_qry )
    print("Record updated Successfully")
    myconn.commit()
    

if(choosed_option == '4'):
    day=input("Please Enter Day Name:")
    period=input("Please Enter period:")

    display_qry1="SELECT teacher_name FROM teachers_table1 WHERE period='"+period+"' and day='"+day+"'and schedule is Null"
    mycursor.execute(display_qry1)
    v1=mycursor.fetchall()
    print(v1)

    display_qry2="SELECT teacher_name FROM teachers_table2 WHERE period='"+period+"' and day='"+day+"'and schedule is Null"
    mycursor.execute(display_qry2)
    v2=mycursor.fetchall()
    print(v2)
    
    display_qry3="SELECT teacher_name FROM teachers_table3 WHERE period='"+period+"' and day='"+day+"'and schedule is Null"
    mycursor.execute(display_qry3)
    v3=mycursor.fetchall()
    print(v3)

    display_qry4="SELECT teacher_name FROM teachers_table4 WHERE period='"+period+"' and day='"+day+"'and schedule is Null"
    mycursor.execute(display_qry4)
    v4=mycursor.fetchall()
    print(v4)

    display_qry5="SELECT teacher_name FROM teachers_table5 WHERE period='"+period+"' and day='"+day+"'and schedule is Null"
    mycursor.execute(display_qry5)
    v5=mycursor.fetchall()
    print(v5)

    display_qry6="SELECT teacher_name FROM teachers_table6 WHERE period='"+period+"' and day='"+day+"'and schedule is Null"
    mycursor.execute(display_qry6)
    v6=mycursor.fetchall()
    print(v6)

    display_qry7="SELECT teacher_name FROM teachers_table7 WHERE period='"+period+"' and day='"+day+"'and schedule is Null"
    mycursor.execute(display_qry7)
    v7=mycursor.fetchall()
    print(v7)

    display_qry8="SELECT teacher_name FROM teachers_table8 WHERE period='"+period+"' and day='"+day+"'and schedule is Null"
    mycursor.execute(display_qry8)
    v8=mycursor.fetchall()
    print(v8)

    display_qry9="SELECT teacher_name FROM teachers_table9 WHERE period='"+period+"' and day='"+day+"'and schedule is Null"
    mycursor.execute(display_qry9)
    v9=mycursor.fetchall()
    print(v9)

    display_qry10="SELECT teacher_name FROM teachers_table10 WHERE period='"+period+"' and day='"+day+"'and schedule is Null"
    mycursor.execute(display_qry10)
    v10=mycursor.fetchall()
    print(v10)

    myconn.commit()

    s=input("select teacher:")

    arrange_qry="UPDATE arrangement SET teacher='"+s+"'WHERE day='"+day +"'and period='"+period+"'"
    mycursor.execute(arrange_qry)
    myconn.commit()

#display the arrangement
if(choosed_option == '5'):
    day=input("Please Enter Day Name:")
    
    display_arrange_qry="SELECT * FROM arrangement WHERE day='"+day+"'"
    mycursor.execute(display_arrange_qry)
    V=mycursor.fetchall()
    print(V)
    myconn.commit()  

if(choosed_option == '6'):
    prayer_e =input('assembly ends:')
    prayer_time=int(input('assembly duration:'))
    if prayer_time>20:
        a=180-prayer_time
        period_time=int(a/4)
    print(period_time)  
    b=int(prayer_e[0])
    x= int(prayer_e[2::])
    y=x+period_time
    if y>=60:
        b+=1
        y=y-60
    firstp=(str(b)+':'+str(y))
    y=y+period_time
    if y>=60:
        b+=1
        y=y-60
    secondp=(str(b)+':'+str(y))
    y=y+period_time
    if y>=60:
        
        b+=1
        y=y-60
    thirdp=(str(b)+':'+str(y))
    print("assembly time",'=','7:30','-',prayer_e)
    print("1st period",'=',prayer_e,'-',firstp)
    print("2nd period",'=',firstp,'-',secondp)
    print("3rd period",'=',secondp,'-',thirdp)
    print("4th period",'=',thirdp,'-','10:30')
    print("RECESS",'=','10:30','-','11:00')
    print("5th period",'=','11:00','-','11:40')
    print("6th period",'=','11:40','-','12:20')
    print("7th period",'=','12:20','-','1:00')
    print("8th period",'=','1:00','-','1:40')
 



