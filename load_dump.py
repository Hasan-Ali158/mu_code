import sqlite3 as sq
con=sq.connect("scott.db")
cur=con.cursor()
i=input("select any one of them a,d,s,l,e,n,I,q:")
while i!="q":
    while i=="a":
        dept=(input("enter dept no:"))
        dn=input("enter dept name:")
        l=input("enter location:")
        cur.execute("insert into DEPT(DEPTNO,DNAME,LOC) values(?,?,?)",(dept,dn,l))
        i=input("select any one of them a,d,s,l,e,n,I,q:")
        con.commit()
    while i=="s":
        name=input("enter the name:")
        a=cur.execute("select * from DEPT where DNAME=?",(name,))
        for row in a:
            print(row)
        i=input("select any one of them a,d,s,l,e,n,I,q:")
        con.commit()
    while i=="l":
        a=cur.execute("select * from DEPT")
        for row in a:
            print(row)
        i=input("select any one of them a,d,s,l,e,n,I,q:")
        con.commit()
    while i=="d":
        name=input("enter the name:")
        cur.execute("delete from DEPT where DNAME=?" , (name,))
        i=input("select any one of them a,d,s,l,e,n,I,q:")
        con.commit()
    while i=="n":
        n1=input("enter the name you want to replace:")
        name =input("enter the new name:")
        cur.execute("update DEPT Set DNAME=? where DNAME=?",(name,n1))
        i=input("select any one of them a,d,s,l,e,n,I,q:")
        con.commit()
    while i=="I":
        n1=input("enter the loc you want to replace:")
        name =input("enter the new loc:")
        cur.execute("update DEPT Set LOC=? where LOC=?",(name,n1))
        i=input("select any one of them a,d,s,l,e,n,I,q:")
        con.commit()
    while i=="e":
        n1=input("enter the deptno you want to replace:")
        loc =input("enter the new loc:")
        name =input("enter the new name:")
        no =int(input("enter the new no:"))
        cur.execute("update DEPT Set LOC=?,DNAME=?,DEPTNO=? where DEPTNO=?",(loc,name,no,n1))
        i=input("select any one of them a,d,s,l,e,n,I,q:")
        con.commit()
cur.close()
con.close()
