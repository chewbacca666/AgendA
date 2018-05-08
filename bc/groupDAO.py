import psycopg2
import sys
from groups import Group



class GroupDAO(object):


	
	def __init__ (self, connection):
		

		self.connection = connection


	def List(self):
		

		self.connection.cur.execute("SELECT * FROM groups ORDER BY id")
		results = self.connection.cur.fetchall()
		#print(results)
			#for i in range(len(results)):
			#	print(results[i][1])
		if(results == []):
			print("Não tem grupo cadastrado")
		else:
			print(results)


	def Insert(self, Name):


		data = []
		data.append(Name)
		self.connection.cur.execute("INSERT INTO groups(name) VALUES (%s)", data)
		self.connection.conn.commit()
		

	def Delet(self, Name,):


		self.connection.cur.execute("DELETE FROM groups WHERE name = '{}'".format(Name))
		self.connection.conn.commit()