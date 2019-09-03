from config import *

def insert(username,name,password):
	conn,cursor=connect_to_database()
	# print("conn:::",conn)
	# print("cursor:::",cursor)
	# # sql = "insert into user_info (name) values(folder_name)"
	sql = "INSERT INTO user_info (name,username,password) VALUES ('%s','%s','%s')" % (name,username,password)
	print(sql)
	result = cursor.execute(sql)
	# name = cursor.fetchone()
	cursor.close()
	conn.commit()
	return result


def check_username(username):
	conn,cursor=connect_to_database()
	sql = "select username from user_info where username='%s'"%(username)
	b =cursor.execute(sql)
	# print("return of check_username:::",b)
	return b


def check_username_password(username,password):
	conn,cursor=connect_to_database()
	sql = "select * from user_info where username='%s' and password='%s'"%(username,password)
	b =cursor.execute(sql)
	# print("return of check_username_password:::",b)
	return b

def student_info_table():
	conn,cursor=connect_to_database()
	sql = "select * from student_info"
	cursor.execute(sql)
	b = cursor.fetchall()
	return b


def insert_student_info(name,roll):
	conn,cursor=connect_to_database()
	sql = "INSERT INTO student_info (name,roll) VALUES ('%s','%s')" % (name,roll)
	result = cursor.execute(sql)
	# name = cursor.fetchone()
	cursor.close()
	conn.commit()
	return result

def check_roll(roll):
	conn,cursor=connect_to_database()
	sql = "select roll from student_info where roll='%s'"%(roll)
	b =cursor.execute(sql)
	return b

def get_element_by_roll(roll):
	conn,cursor=connect_to_database()
	sql = "select * from student_info where roll='%s'"%(roll)
	# print(sql)
	b =cursor.execute(sql)
	info = cursor.fetchone()
	return info

def update_student_info(name,roll,uid): 
	conn,cursor=connect_to_database()
	sql = "update student_info set name='%s', roll='%s' where id='%s'"%(name,roll,uid)
	try:
		b =cursor.execute(sql)
		conn.commit()
	except:
		b =0
	return b


def get_roll_by_id(uid):
	conn,cursor=connect_to_database()
	sql = "select Distinct roll from student_info where id='%s'"%(uid)
	b =cursor.execute(sql)
	info = cursor.fetchone()
	return info[0]


def get_name_by_id(uid):
	conn,cursor=connect_to_database()
	sql = "select Distinct name from student_info where id='%s'"%(uid)
	b =cursor.execute(sql)
	info = cursor.fetchone()
	return info[0]


def delete_info_by_name(nam):
	conn,cursor=connect_to_database()
	sql = "delete from student_info where name='%s'"%(nam)
	print(sql)
	b =cursor.execute(sql)
	conn.commit()
	print("delete record::",b)
	return b

def check_name(name):
	conn,cursor=connect_to_database()
	sql = "select name from student_info where name='%s'"%(name)
	print(sql)
	b =cursor.execute(sql)
	print("attendace theory value:::",b)
	return b
