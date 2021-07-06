#Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big". Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]
def biggie_size(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = 'big'
    return list

list = [-1,3,5,-5]
print(biggie_size(list))
print ('*'*50)

#2. Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos. (Tenga en cuenta que cero no se considera un número positivo).Ejemplo: count_positives([- 1, 1, 1,1 ]) cambia la lista original a [-1, 1, 1, 3] y la devuelve
def count_positives(list):
    count = 0
    for i in range (len(list)):
        if list[i] > 0:
            count += 1
            list[(len(list)-1)] = count
    return list

list = [-1,1,1,1]
print(count_positives(list))
print ('*'*50)

#3. Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz. Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
def sum_total(list):
    sum = 0
    for i in range (len(list)):
        sum += list[i]
    return sum

list = [1,2,3,4]
print(sum_total(list))
print('*'*50)

#4. Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5
def promedio(list):
    sum = 0
    promedio = 0
    for i in range (len(list)):
        sum += list[i]
        promedio = (sum/(len(list)))
    return promedio

list = [1,2,3,4]
print(promedio(list))
print('*'*50)

#5. Longitud : crea una función que toma una lista y devuelve la longitud de la lista. Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
def longitud(list):
    for i in range (len(list)):
        return len(list)

list = [37,2,1,-9]
print(longitud(list))
print('*'*50)
 
#6. Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista. Si la lista está vacía, haga que la función devuelva False. Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9 
def minimo(list):
    if len(list) == 0 :
        return False
    else:
        min = list[0]
        for i in range (len(list)):
             if list[i] < min:
                  min = list[i]
    return min

list = [37,2,1,-9]
print(minimo(list))
print('*'*50)
 
#7. Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. Si la lista está vacía, haga que la función devuelva False. Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
def maximo(list):
    if len(list) == 0 :
        return False
    else:
        max = list[0]
        for i in range (len(list)):
             if list[i] > max:
                  max = list[i]
    return max

list = [37,2,1,-9]
print(maximo(list))
print('*'*50)

#8. Análisis final : crea una función que tome una lista y devuelva un diccionario que tenga la suma total, promedio, mínimo, máximo y longitud de la lista. Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver {'total': 31, 'promedio': 7.75, 'minimo': -9, 'maximo': 37, 'longitud': 4}
def ultimate_analysis(list):
    analisis = {'total':sum_total(list),'promedio':promedio(list),'minimo': minimo(list),'maximo':maximo(list),'longitud':longitud(list) }
    return analisis

list = [37,2,1,-9]
print(ultimate_analysis(list))
print('*'*50)

#9. Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos. Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas). Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]
def reverse_list(list):
    for i in range (int(len(list)/2)):     
        list[i], list[(len(list))-i-1] = list[(len(list))-i-1], list[i]
    return list

list = [37,2,1,-9]
print(reverse_list(list))
print('*'*50)

        