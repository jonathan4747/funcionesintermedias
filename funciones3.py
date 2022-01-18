#1
x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
x[1][0]=15
print(x)
estudiantes[0]['last_name']='Bryant'
print(estudiantes)
directorio_deportes['fútbol'][0]='Andrés'
print(directorio_deportes)
########################################################
estudiantes1 = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
#2
def iterateDictionary(dict):
    for i in range (0,len(dict)):
        for key in dict[i]:
            print(f"{key}-{dict[i][key]}")
            
              
iterateDictionary(estudiantes1)

#3
def iterateDictionary2(keys, dict):
    for i in range(0,len(dict)):
        llave=dict[i][keys]
        print(llave)
iterateDictionary2('first_name', estudiantes1)
iterateDictionary2('last_name', estudiantes1)     

dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
#4   
def printInfo(dict):
    for key in dict:
        print (len(dict[key]),key)
        for i in range(len(dict[key])):
            print(dict[key][i])        
printInfo(dojo)


