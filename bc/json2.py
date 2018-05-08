import json
book = {}
book["tom"] = { 
	

	"name": "tom", 	
	"address": "1 red street, NY", 	
	"phone": 989898 


	}


book["bob"] = {
	

	"name": "bob",
	"address": "1 green street, NY",
	"phone": 23232323


}
'''name = input("")
rua = input("")
fone = input("")


book[name] = {

	
	"name": name,
	"address": rua,
	"phone": fone	

}'''
'''print(len(book))
print(book["tom"]["name"])
print(type(book))'''
s = json.dumps(book)
print(type(s))
#print(len(s))
si = s.split()
print(len(si))
for i in range(len(si)):
	print(si[i])