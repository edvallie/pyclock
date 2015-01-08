# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4


import psycopg2 as dbapi2
from config import *
import datetime



try:
    db = dbapi2.connect (host=dbhost, database=dbname, user=dbuser, password=dbpass)
    cur = db.cursor()
except:
    pass

def testSql():
    try:
        cur.execute ("SELECT * FROM employees")
        rows = cur.fetchall()
        for i, row in enumerate(rows):
            print "Row", i, "value = ", row
    except:
        pass
def insertPunch(employee_id):
    try:
        sql = "INSERT INTO timestamps (employee_id, timestamp) VALUES('" + employee_id + "', NOW())"
        print sql
        cur.execute (sql)
        db.commit ()
        print "Entered timestamp for employee_id: ", employee_id
        return True
    except:
        return False

def getName(employee_id):
    try:
        sql = "SELECT full_name from employees where employee_id = '" + employee_id + "'"
        cur.execute (sql)
        row = cur.fetchone()
        if row:
            employee_name = row[0]
        else:
            return ''
    except:
        return ''

def getPunches():
    try:
        employeesOut = []
        employeesIn = []
        i = datetime.date.today()
        today = i.isoformat()
        sql = "SELECT employee_id, COUNT(*) FROM timestamps WHERE timestamp > '" + today + "' GROUP BY employee_id"
        cur.execute (sql)
        rows = cur.fetchall()
        for i, row in enumerate(rows):
            eid = row[0]
            IntPunches = row[1]
            sql = "SELECT full_name, timestamp FROM employees, timestamps where employees.employee_id = timestamps.employee_id AND timestamps.employee_id = '" + str(eid) + "' ORDER BY timestamps.timestamp DESC LIMIT 1"
            cur.execute(sql)
            entry = cur.fetchone()
            name = entry[0]
            time = entry[1]
            now = datetime.datetime.now()
            tdelta = now - time
            td = str(tdelta)[:-10]
            output = name + " " + td

            if IntPunches%2 == 0:
                employeesOut.append( output )
            else:
                employeesIn.append( output )
        employeesIn.sort()
        employeesOut.sort()
        print employeesIn
        print employeesOut
        return employeesIn, employeesOut
    except:
        return ['Database Error'], ['Database Error']
