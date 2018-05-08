class User(object):
	

	def __init__(self, id, name, surname, email, password, birth):
		

		self.id = id
		self.name = name
		self.surname = surname
		self.email = email
		self.password = password
		self.birth = str(birth)