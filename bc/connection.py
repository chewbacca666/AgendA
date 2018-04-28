import psycopg2


class Connection:

	
	def __init__(self, dbname , host = "localhost", user = "postgres" , password = "postgres" ):
		

		try:
			self.conn = psycopg2.connect("host="+host+" dbname="+dbname+" user="+user+" password="+password)
			self.cur = self.conn.cursor()
		except:
			print("Deu Xabum")
                
				
	
	def close(self):
		

		self.cur.close()
		self.conn.close()		

