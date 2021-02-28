import psycopg2
import random
import sys
import time

#genera una stringa casuale
def randstring(length=50):
    valid_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join((random.choice(valid_letters) for i in range(length)))

#genera un id casuale univoco
def randid(l):
    while len(l)<=1000000:
        numeroid=random.randint(1, 1000000)
        if numeroid not in l:
            l.append(numeroid)
            return numeroid

#genera un'altezza casuale univoca
def randheight():
    m=[]
    while len(m)<=1000000:
        altezza=random.uniform(140.000, 220.000)
        if altezza not in m and altezza!=185:
            m.append(altezza)
            return altezza

#genera un cid casuale univoco
def randcid():
    n=[]
    while len(n)<=1000000:
        cid=randstring(25)
        if cid not in n:
            n.append(cid)
            return cid
        
def operazione_1(cursor):
    cursor.execute("""DROP TABLE IF EXISTS "Professor" CASCADE;""")
    cursor.execute("""DROP TABLE IF EXISTS "Course";""")

def operazione_2(cursor):
    cursor.execute("""CREATE TABLE "Professor" (id INT PRIMARY KEY NOT NULL, name CHAR (50) NOT NULL, address CHAR (50) NOT NULL, age INT NOT NULL, height FLOAT NOT NULL);""")
    cursor.execute("""CREATE TABLE "Course" (cid CHAR (25) PRIMARY KEY NOT NULL, title CHAR (50) NOT NULL, area CHAR (30) NOT NULL, instructor INT NOT NULL, FOREIGN KEY (instructor) REFERENCES "Professor" (id));""")

def operazione_3(cursor, l):
    for i in range (999999):
        cursor.execute("""INSERT INTO "Professor" (id, name, address, age, height) VALUES (%s, %s, %s, %s, %s);""", (randid(l), randstring(), randstring(), random.randint (23, 80), randheight()))
    cursor.execute("""INSERT INTO "Professor" (id, name, address, age, height) VALUES (%s, %s, %s, %s, %s);""", (randid(l), randstring(), randstring(), random.randint (23, 80), 185))

def operazione_4(cursor, l):
    for i in range (1000000):
        cursor.execute("""INSERT INTO "Course" (cid, title, area, instructor) VALUES (%s, %s, %s, %s);""", (randcid(), randstring(), randstring(30), random.choice(l)))

def operazione_5(cursor):
    cursor.execute("""SELECT p.id FROM "Professor" p;""")
    rows=cursor.fetchall()
    print(rows, file=sys.stderr)
    
def operazione_6(cursor):
    cursor.execute("""UPDATE "Professor" SET height=200 WHERE height=185;""")

def operazione_7(cursor):
    cursor.execute("""SELECT p.id, p.address FROM "Professor" p WHERE p.height=200;""")
    rows2=cursor.fetchall()
    print(rows2, file=sys.stderr)

def operazione_8(cursor):
    cursor.execute("""CREATE INDEX albero ON "Professor" (height);""")

def operazione_9(cursor):
    cursor.execute("""SELECT p.id FROM "Professor" p;""")
    rows3=cursor.fetchall()
    print(rows3, file=sys.stderr)

def operazione_10(cursor):
    cursor.execute("""UPDATE "Professor" SET height=210 WHERE height=200;""")

def operazione_11(cursor):
    cursor.execute("""SELECT p.id, p.address FROM "Professor" p WHERE p.height=210;""")
    rows4=cursor.fetchall()
    print(rows4, file=sys.stderr)

def main():
    #connessione al database
    connection=psycopg2.connect(user = "db_050",
                                password = "secret_050",
                                host = "192.168.131.7",
                                database = "db_050")
    cursor=connection.cursor()
    l=[]

    #operazioni
    start=time.time_ns()
    operazione_1(cursor)
    end=time.time_ns()
    timer=end-start
    print("Step 1 needs", timer, file=sys.stdout, end=" ns\n")

    start=time.time_ns()
    operazione_2(cursor)
    end=time.time_ns()
    timer=end-start
    print("Step 2 needs", timer, file=sys.stdout, end=" ns\n")

    start=time.time_ns()
    operazione_3(cursor, l)
    end=time.time_ns()
    timer=end-start
    print("Step 3 needs", timer, file=sys.stdout, end=" ns\n")

    start=time.time_ns()
    operazione_4(cursor, l)
    end=time.time_ns()
    timer=end-start
    print("Step 4 needs", timer, file=sys.stdout, end=" ns\n")
    
    start=time.time_ns()
    operazione_5(cursor)
    end=time.time_ns()
    timer=end-start
    print("Step 5 needs", timer, file=sys.stdout, end=" ns\n")

    start=time.time_ns()
    operazione_6(cursor)
    end=time.time_ns()
    timer=end-start
    print("Step 6 needs", timer, file=sys.stdout, end=" ns\n")
    
    start=time.time_ns()
    operazione_7(cursor)
    end=time.time_ns()
    timer=end-start
    print("Step 7 needs", timer, file=sys.stdout, end=" ns\n")
    
    start=time.time_ns()
    operazione_8(cursor)
    end=time.time_ns()
    timer=end-start
    print("Step 8 needs", timer, file=sys.stdout, end=" ns\n")
   
    start=time.time_ns()
    operazione_9(cursor)
    end=time.time_ns()
    timer=end-start
    print("Step 9 needs", timer, file=sys.stdout, end=" ns\n")
    
    start=time.time_ns()
    operazione_10(cursor)
    end=time.time_ns()
    timer=end-start
    print("Step 10 needs", timer, file=sys.stdout, end=" ns\n")
    
    start=time.time_ns()
    operazione_11(cursor)
    end=time.time_ns()
    timer=end-start
    print("Step 11 needs", timer, file=sys.stdout, end=" ns\n")
    
    #commit
    connection.commit()

    #chiudi connessione
    if(connection):
        cursor.close()
        connection.close()

if __name__=="__main__":
    main()
