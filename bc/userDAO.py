import psycopg2
import sys
from users import User
#sys.path.append("./")



class UserDAO(object):
	


	def __init__ (self, connection):
		
	
		self.connection = connection

	
	def List(self):
		

		self.connection.cur.execute("SELECT * FROM users ORDER BY id")
		
		users = []
		rows = self.connection.cur.rowcount
		results = self.connection.cur.fetchall()
		#print(results)
		for i in range(rows):
			users.append(User(results[i][0], results[i][1], results[i][2], results[i][3], results[i][4]))
			print("\n")
		return (users)


	def Insert(self, Name, Surname, Email, Password, Birth):


		data = []
		data.append(Name)  
		data.append(Email) 
		data.append(Password)
		data.append(Birth)
		self.connection.cur.execute("INSERT INTO users (name,surname,email,password,birth) VALUES (%s,%s,%s,%s,%s)", data)
		self.connection.conn.commit()


	def Delet(self, Id):


		self.connection.cur.execute("DELETE FROM users WHERE id = '{}'".format(Id))
		self.connection.conn.commit()
		

	def Update(self, Cond_up):


		if(Cond_up == '1'):
		

			up_id = input("Id : ")
			up_name = input("Novo nome : ")
			self.connection.cur.execute("UPDATE users SET name = '{}' WHERE id = '{}'".format(up_name,up_id))
			self.connection.conn.commit()
		

		if(Cond_up == '3'):
		
			up_id = input("Id : ")
			up_password = input("Nova senha : ")
			self.connection.cur.execute("UPDATE users SET password = '{}' WHERE id = '{}'".format(up_password,up_id))
			self.connection.conn.commit()
		

		if(Cond_up == '4'):
		
			up_id = input("Id : ")
			up_birth = input("Digite a nova data : ").split("/")
			self.connection.cur.execute("UPDATE users SET birth = '{}' WHERE id = '{}'".format(up_birth	,up_id))
			self.connection.conn.commit()


	def Login(self, Email, Password):
		self.connection.cur.execute("SELECT email,password FROM users WHERE email = '{}' and password = '{}'".format(Email, Password))
		rows = self.connection.cur.rowcount
		results = self.connection.cur.fetchall()
		return (rows)
