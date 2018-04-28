import psycopg2
import sys

def main():
	 

	cadeiaConexao = "host ='localhost' dbname = 'postgres' user = 'postgres' password = 'postgres'"
	obj = psycopg2.connect(cadeiaConexao)
	cursor = obj.cursor()
	cursor.execute("SELECT users.id, users.name,users.surname,users.email,users.password, COUNT(*) as Groups FROM public.users INNER JOIN public.participation ON (users.id = public.participation.user_id) INNER JOIN public.groups ON (groups.id = public.participation.group_id) GROUP BY users.id ORDER BY users.id")
	result = cursor.fetchall()
	cursor.execute("SELECT users.id, users.name,groups.name FROM public.groups INNER JOIN public.participation ON (groups.id = public.participation.group_id) INNER JOIN public.users ON (users.id = public.participation.user_id) ORDER BY users.id")
	result2 = cursor.fetchall()
	cursor.execute("SELECT groups.id, groups.name, COUNT(*) AS Usuarios FROM public.groups INNER JOIN participation ON (groups.id = participation.group_id) GROUP BY groups.id")
	result3 = cursor.fetchall()
	name = 'a'
	sql = "SELECT * FROM users WHERE name ILIKE '%" + name +"%';"
	cursor.execute(sql)
	teste = cursor.fetchall()
	print("Nomes")
	print("Primeira tabela [{}]".format(len(result)))
	print("Segunda tabela [{}]".format(len(result2)))
	ajuda = []
	eventos = []
	'''for i in range(len(result)):
		if(i == 0):
			ajuda.append(result[i][1])
		else:	
			if(result[i][0] != result[i-1][0]):
				ajuda.append(result[i][1])
	for i in range(len(ajuda)):
		for j in range(len(result2)):
			if(ajuda[i] == result2[j][1]):
				eventos.append(result2[j][2])

	print(eventos)''' 

	print(teste)
if __name__ == "__main__":
	main()