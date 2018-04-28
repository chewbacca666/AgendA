from flask import *
from users import User
from groups import Group
from userDAO import *
from groupDAO import *
from connection import *


connection = Connection("AgendA")

userDAO = UserDAO(connection)

groupDAO = GroupDAO(connection)

app = Flask(__name__)

@app.route("/cadastrar")
def Insert():
	pass



@app.route("/user/")
def List():
	users = userDAO.List()
	string = "<p>"
	for x in range(len(users)):
		string = string + users[x].name + " " + users[x].surname + " " + str(users[x].email) + " " + str(users[x].password) + " " + str(users[x].birth) + "<br>"
	print(string)
	return string + "</p>"
@app.route("/sou")
def oi():
	return "<h1> batata </h1>"

@app.route("/xitus")
def ola():
	return"<h2> Hello </h2> "







if(__name__ == "__main__"):
	app.run(debug = True)

'''cond = 0
while(cond != '10'):
	

	print("\n")
	print("		1 - Cadastrar um usuario no banco")
	print("		2 - Cadastrar um grupo no banco")
	print("		3 - Deletar  um usuario no banco")
	print("		4 - Deletar um grupo no banco")
	print("		5 - Mostrar os usuarios cadastrados no banco")
	print("		6 - Mostrar os grupos cadastrados no banco")
	print("		7 - Alterar algum dado do usuario")
	print("  		8 - Cadastrar um usuario no grupo")
	cond = input("			Digite o que voce quer fazer : ")

	
	if(cond == "1"):
		print("\n")


		user_data = []
		name = input("Digite seu nome e seu sobrenome : ").split()
		user_data.append(name[0])
		user_data.append(name[1])
		user_data.append(input("Digite o seu email : "))
		user_data.append(input("Digite a sua senha : "))
		birth = input("Digite a data do seu aniversario por / : ").split("/")
		user_data.append(birth[0])
		user_data.append(birth[1])
		user_data.append(birth[2])
		userDAO.Insert(user_data[0],user_data[1],user_data[2],user_data[3],user_data[4],user_data[5],user_data[6])

	
	if(cond == '2'):
		print("\n")


		group_data = input("Digite o nome do grupo : ")
		groupDAO.Insert(group_data)

	
	if(cond == '3'):
		print("\n")


		delete_user = input("Digite o id : ")
		userDAO.Delet(delete_user[0],delete_user[1])


	if(cond == '4'):
		print("\n")		


		delet_group = input("Digite o id : ")
		groupDAO.Delet(delet_group)
	
	
	if(cond == '5'):
		print("\n")


		userDAO.List()

	
	if(cond == '6'):
		print("\n")
		

		groupDAO.List()



	if(cond == '7'):
		print("\n")


		print("	1 - Desejas alterar o nome")
		print("	2 - Desejas alterar o sobrenome")
		print("	3 - Desejas alterar o senha")
		print("	4 - Desejas alterar a data de nascimento")
		cond_up = input("		O que desejas escolher : ")
		userDAO.Update(cond_up)


	if(cond == '8'):
		print("\n")
		

		#group_add = input("Qual o grupo que vais adicionar um usuario ? ")
		print(groups.name)
		
'''