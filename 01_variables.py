# Variables
# snake_case es la práctica correcta de nombrar variables

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de mi variable:", my_bool_variable )

# Variables en una sola línea
# ¡No abusar de esta sintaxis!
name, surname, alias, age = "Daniel", "Alvarez", "Dan", 28
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)

# Inputs
name = input("¿Cuál es tu nombre? ")
age = input("¿Cuántos años tienes? ")
print(name)
print(age)

# Cambio de tipo de variables
name = 28
age = "Dan"
print(name)
print(age)

# Forzamos el tipo
address: str = "Mi dirección"

# Funciones del sistema

# Longitud de la variable
print(len(my_string_variable)) # Imprime el largo de mi variable: 18