### create calcultator ###
### here we define the things you can do with the calculator ###
def añadir (a, b):
    return a + b
def resta (a, b):
    return a - b
def multiplicacion (a, b):
    return a * b
def division (a, b):
    return a / b
### here we ask the user to enter type of operation he wants to do, and we store that information in the variable call "operación" ###
print ("BIENVENIDO A LA CALCULADORA DE GUIRAO")
print ("las operaciones que pudes realizar son las siguientes:")
print ("-suma")
print ("-resta")
print ("-multiplicación")
print ("división")
operación = input ("ingresa el tipo de operación que deseas realizar: ")
### here we ask the user to enter two numbers to use in the operation they have chosen, we store the value in the variables "acción" and "acción_1" and then we turn them into an intege ###
acción = int (input ("ingresa el primer número: ")) 
acción_1 = int (input ("ingresa el segundo número: ")) 
### here we check which operation the user wants to do comparing it with the input he gave us in the variable "operation" and we proceed to do the operation he requested ###
if operación == "suma":
    print ("el reultado de la suma es: {}".format(añadir (acción, acción_1)))
if operación == "resta":
    print  ("el reultado de la resta es: {}".format(resta(acción, acción_1)))
if operación == "multiplicación":
    print  ("el reultado de la multiplicación es: {}".format(multiplicacion(acción, acción_1)))
if operación == "division":
    print  ("el reultado de la división es: {}".format(division(acción, acción_1)))