
'''TIPOS DE DATOS
<class 'int'>:identifica que la variable es un entero 
<class 'float'>: identifica la variable es un numero dicimal
<class 'bool'>: identifica que la variablees un valor true o false (boolean)
<class 'str'>: identifica que es una variable de texto



'''

x=True# True y false son palabras reservadas 
print(type(x))

autor='andres'
print(type(autor))

carro="this is andres car:"
modelo='1999'
print(carro + modelo ) # el simbolo + permite textos en python


'''
TIPOS DE ESTRUCTURAS DE DATOS Y METODOS
1. Conjutos+
2.tuplas++
3- listas +++
4. diccionarios

'''
# uso de conjutos
'''Los sets o conjuntos son estructuras especiales que nos ayudan a almacenera un grupo
de elementos. Cuando el orden de los elementos no es relevante podemos utilizar sets
en Python. ademas esta estrutura no permite duplicados 

como se definen

'''
set1 ={"a","b",'d'}
print(type(set1))

set2={"e",'f',"g"}

#metodos para el tratamiento de conjuntos
set1.union
# union de conjuntos

print(set1.union(set2))

set3={"a","b","c","c","d","d"}
print(set3)

set4=set3.union(set1)
print(set4)

#interseccion de conjutos

set5={"f","w","a","b"}
print(set5)
#print(set5.intersection(set1))

set5.remove("w")
print(set5)


set6={"andres", 5, True}
set7={"andres", 5, True,"daniel"}
print(set6.issuperset(set7)) # false
print(set7.issuperset(set6)) #true



'''uso de tuplas 
son estructuras de datos rapidas que no permiten muchos metodos 
se usan cuando queremos resguardar la informacion (inmutable)
si permiten valores duplicados
como se define :(, , , , , , )
<class 'tumple'>

'''
tupla1=(1,1,1,1,1,1,1,1,1,2,3,4,5)
print(type(tupla1))
conteo=tupla1.count(1)

print(conteo)

# index

indice=tupla1.index(1)
print(indice)

'''python es un leguaje indexado en cero 
siempre el primer elemento es una estructura de datos tiene
el indice 0 , en otras palabras , la posicion inicial siempre 
'''


'''USO DE LISTAS
Las listas en python son estructuras de datos que almacenan 
elementos de manera ordenada y mutable 
son tipo de datos nativo del lenguaje de programcion python
como se define  
si permiten valores duplicados

<class 'list>
puede contener cualquier tipo datos numero letrass o incluso otras listas



'''
list1=[8,9,7,5,4,10]
print(type(list1))
#metodo count
list2=[["jon","alejo","lwein",]["isabel","juan","cami"]]
print(list1.count(14))

# reverse 
list3=list1.reverse() # invertigar
list1.reverse()
print(list1)

#prit list 1

#investigar el reverse, sort

# como acceder a los elementos 

list2=[["jon","alejo","lwein",]["isabel","juan","cami"]]
print(list2[0][0][1])



'''diccionarios
 classcdict'''




estudiantes={'diana :25','juan',:20,'ana':29}
print(type(estudiantes ))

printe(estudiantes.key())
print(estudiantes.value())



#diccionarios involucren otras estructuras 

instituto={
'robotica':["diana", "juan", "pedro"],'programacionm':["andre", "luis","miguel"]
}

print(instituto.value)()

colegio={'quimica':{"luisa",:15,"jose",:14},
'fisica':{"lina":14,"mario":17}
print(colegio.values)()

distancias=('palmira','cali',):22
            ('palmira','pradera'):15


#actulizar el diccinarios agregando una clave valor
estudiantes['luisa']=45

print(estudiantes)
estudiantes['juan']=18

print(eestudiantes)
