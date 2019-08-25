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
