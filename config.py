import cgi, cgitb 
import pymysql
def connect_to_database():
	conn=pymysql.connect("localhost",'root','root@123','db_face_rec')
	cursor = conn.cursor()
	return conn,cursor