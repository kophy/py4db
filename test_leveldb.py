#!/usr/bin/env python

import leveldb
import os, sys

def initialize():
	db = leveldb.LevelDB("students");
	return db;

def insert(db, sid, name):
	db.Put(str(sid), name);

def delete(db, sid):
	db.Delete(str(sid));

def update(db, sid, name):
	db.Put(str(sid), name);

def search(db, sid):
	name = db.Get(str(sid));
	return name;

def display(db):
	for key, value in db.RangeIter():
		print (key, value);

db = initialize();

print "Insert 3 records."
insert(db, 1, "Alice");
insert(db, 2, "Bob");
insert(db, 3, "Peter");
display(db);

print "Delete the record where sid = 1."
delete(db, 1);
display(db);

print "Update the record where sid = 3."
update(db, 3, "Mark");
display(db);

print "Get the name of student whose sid = 3."
name = search(db, 3);
print name;

os.system("rm -r students");
