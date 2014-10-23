#!/usr/bin/python
import psycopg2 as dbapi2
from config import *
#import ConfigParser
#import io
#import config

db = dbapi2.connect (host=dbhost, database=dbname, user=dbuser, password=dbpass)
cur = db.cursor()

def testSql():
    #cur = db.cursor()
    cur.execute ("SELECT * FROM employees")
    rows = cur.fetchall()
    for i, row in enumerate(rows):
        print "Row", i, "value = ", row

def insertPunch(employee_id):
    print employee_id
    cur.execute ("SELECT * FROM employees")
    rows = cur.fetchall()
    for i, row in enumerate(rows):
        print "Row", i, "value = ", row

def checkPunches():
    print "derp"


testSql()
insertPunch("9999")

