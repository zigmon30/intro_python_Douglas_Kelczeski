weekdays = ['mon','tues','wed','thurs','fri']
all_days = weekdays + ['sat','sun']
days_list = all_days
list = ['a', 1, 3.14159265359]
print(list)
print(type(list))
list.insert(1,'zero')
print(list)

ultimo_elemento = list.pop()


print(ultimo_elemento)
print(list)
del list
print(list)

days = weekdays[0]      
days = weekdays[0:3]      
days = weekdays[:3]   
days = weekdays[-1]
print(days)


#########
# Exercicios - Listas
# Faca sem usar loops
#########

'''# Como selecionar 'wed' pelo indice?
    print(weekdays[2])
'''
    
'''# Como verificar o tipo de 'mon'?
    print (type (weekdays[0]))
'''

'''# Como separar 'wed' até 'fri'?
    print(weekdays[2:5])
'''

'''# Quais as maneiras de selecionar 'fri' por indice?
    print(weekdays[4])
    print(weekdays[-1])
'''

'''# Qual eh o tamanho dos dias e days_list?
    print(len(days))
    print(len(days_list))
'''

'''# Como inverter a ordem dos dias?
    days_list.reverse()
'''

'''# Como inserir a palavra 'zero' entre 'a' e 1 de list?
    list.insert(1,'zero')
'''

'''# Como limpar list?
    list.clear()
'''

'''# Como deletar list?
    del (list)
'''

'''# Como atribuir o ultimo elemento de list na variavel ultimo_elemento e remove-lo de list?
    ultimo_elemento = list.pop()
'''