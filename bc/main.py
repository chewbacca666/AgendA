from flask import *
from users import User
from groups import Group
from userDAO import *
from groupDAO import *
from connection import *
import hashlib
import json
connection = Connection("AgendA")

userDAO = UserDAO(connection)

groupDAO = GroupDAO(connection)

app = Flask(__name__)





@app.route("/list")
def list():
	users = userDAO.List()
	users_str = json.dumps({"users": [user.__dict__ for user in users]})
	return str(users_str) + '''<p> <a href="/home">Voltar</a>'''  


@app.route("/home", methods = ['GET', 'POST'])
def home():
	return render_template("main.html")
	


#@app.route("/deletar" , methods = ['GET', 'POST'])
#def deletar():





@app.route("/register")
def register():
	return render_template("register.html")



@app.route("/join" , methods = ['GET', 'POST'])
def join():
	return render_template("join.html")

	#return "404" '''<a href="/home">Voltar</a>'''


@app.route("/joins", methods = ['GET', 'POST'])
def joins():
	#campo = request.json['campo']
	
	#users_str = json.dumps({"users": [user.__dict__ for user in users]})
	email = request.form.get("email")
	password_h = request.form.get("senha")
	passwordUtf8 = password_h.encode("utf-8")
	hash = hashlib.md5(passwordUtf8)
	password = hash.hexdigest()
	login = userDAO.Login(email, password)
	print(str(login))
	if(int(login) > 0):
		return render_template("login.html")
	else:
		return "VOCE NÃO ESTA LOGADO" '''<p> <a href="/home">Voltar</a>'''
	


@app.route("/registers" , methods = ['GET', 'POST'])
def registers():
	

	if(request.method == "POST"):
		

		name = request.form.get("nome")
		surname = request.form.get("sobrenome")
		email = request.form.get("email")
		password_h = request.form.get("senha")
		passwordUtf8 = password_h.encode("utf-8")
		hash = hashlib.md5(passwordUtf8)
		password = hash.hexdigest()
		password_h2 = request.form.get("senha2")
		passwordUtf82 = password_h2.encode("utf-8")
		hash2 = hashlib.md5(passwordUtf82)
		password2 = hash2.hexdigest()
		birth = request.form.get("birth")
		if(password == password2):

			if(name and surname and email and password and birth):
				userDAO.Insert(name, surname, email, password, birth)

		else:
			return render_template("register2.html")


	return redirect(url_for("home"))		




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
		#user_data.append(input("Digite a sua senha : "))
		password = input("Digite sua senha : ")
		passwordUtf8 = password.encode("utf-8")
		hash = hashlib.md5(passwordUtf8)
		hexa = hash.hexdigest()
		user_data.append(hexa)
		user_data.append(input("Digite a data do seu aniversario por - : "))
		#user_data.append(birth[0])
		#user_data.append(birth[1])
		#user_data.append(birth[2])
		userDAO.Insert(user_data[0],user_data[1],user_data[2],user_data[3],user_data[4])

	
	if(cond == '2'):
		print("\n")


		group_data = input("Digite o nome do grupo : ")
		groupDAO.Insert(group_data)

	
	if(cond == '3'):
		print("\n")


		delete_user = input("Digite o id : ")
		userDAO.Delet(delete_user)


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
		password = input("")
		passwordUtf8 = password.encode("utf-8")
		hash = hashlib.md5(passwordUtf8)
		hexa = hash.hexdigest() 

		#group_add = input("Qual o grupo que vais adicionar um usuario ? ")
		#print(groups.name)
	if(cond == '9'):
		password2 = input("")
		passwordUtf82 = password2.encode("utf-8")
		hash2 = hashlib.md5(passwordUtf82)
		hexa2 = hash2.hexdigest()
		print(hexa)
		print(hexa2)
		if(hexa == hexa2):
			print("Eu consegui")
		else:
			print("Eu sou um bosta")
	'''