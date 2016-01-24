#!/usr/bin/env python
#-*-coding:utf-8 -*-

import sqlite3
import os, sys

def initialize(conn):
	c = conn.cursor();
	c.execute("CREATE TABLE students (sid INTEGER PRIMARY KEY, name TEXT)");
	conn.commit();

def insert(conn, sid, name):
	c = conn.cursor();
	t = (sid, name);
	c.execute("INSERT INTO students VALUES (?, ?)", t);
	conn.commit();

def delete(conn, sid):
	c = conn.cursor();
	t = (sid, );
	c.execute("DELETE FROM students WHERE sid = ?", t);
	conn.commit();

def update(conn, sid, name):
	c = conn.cursor();
	t = (name, sid);
	c.execute("UPDATE students SET name = ? WHERE sid = ?", t);
	conn.commit();

def display(conn):
	c = conn.cursor();
	c.execute("SELECT * FROM students");
	print c.fetchall();

db_name = ":memory:";
conn = sqlite3.connect(db_name);

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

conn.close();
