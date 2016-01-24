#!/usr/bin/env python
#-*-coding: utf-8-*-

import MySQLdb
import os, sys

def initialize(conn):
	c = conn.cursor();
	c.execute('''CREATE TABLE IF NOT EXISTS students (
				 sid INT(4) PRIMARY KEY, name VARCHAR(10)
				 )''');
	conn.commit();

def insert(conn, sid, name):
	c = conn.cursor();
	t = (sid, name);
	c.execute("INSERT INTO students VALUES (%s, %s)", t);
	conn.commit();

def delete(conn, sid):
	c = conn.cursor();
	t = (sid, );
	c.execute("DELETE FROM students WHERE sid = %s", t);
	conn.commit();

def update(conn, sid, name):
	c = conn.cursor();
	t = (name, sid);
	c.execute("UPDATE students SET name = %s WHERE sid = %s", t);
	conn.commit();

def display(conn):
	c = conn.cursor();
	c.execute("SELECT * FROM students");
	print c.fetchall();

try:
	conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "");
except Exception, e:
	print e;
	sys.exit();

c = conn.cursor();
c.execute("CREATE DATABASE IF NOT EXISTS test");
conn.commit();
conn.select_db("test");

initialize(conn);

print "Insert 3 records."
insert(conn, 1, "Alice");
insert(conn, 2, "Bob");
insert(conn, 3, "Peter");
display(conn);

print "Delete the record where sid = 1."
delete(conn, 1);
display(conn);

print "Update the record where sid = 3."
update(conn, 3, "Mark");
display(conn);

c.execute("DROP DATABASE test");
conn.commit();
conn.close();
