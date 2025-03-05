# -*- coding: utf-8 -*-
#EJERCICIO EN CLASE
#=======================
#programa: ConvierteTiempo
#proposito:
#=======================
print('Saludo a todo aquel que este viendo esto hoy ')
print('a continuacion el menu de conversiones de tiempo:\n')

def convertir_a_segundos():
    try:
        horas = int(input('ingrese las horas: '))
        minutos = float(input('ingrese los minutos: '))
        segundos = (horas * 3600) + (minutos * 60)
        print(f'{horas} horas y {minutos:.2f} minutos son {segundos:.2f} segundos\n')
    except ValueError:
        print('Error: ingrese valores numericos validos: \n')


def convertir_desde_segundos():
    try:
        segundos= int(input('Ingrese la cantidad de segundos: '))
        horas = segundos // 3600
        minutos = (segundos - (horas*3600)) / 60
        
        print(f'{segundos} segundos son {horas} horas y {minutos:.2f} minutos. \n')
    except ValueError:
        print('Error: ingrese valores numericos validos: \n')
        
def menu():
    finalizacion = True
    while finalizacion == True:
        print('Menu de conversiones de tiempo')
        print('1. Convertir desde horas y minutos a segundos')
        print('2, Convertir dede segundos a horas y minutos')
        print('3. Salir')
        
        opcion = int(input('Ingrese una de estas tres opciones: 1 , 2 o 3: \n'))
        if opcion == 1:
            convertir_a_segundos()
        elif opcion == 2:
            convertir_desde_segundos()  
        elif opcion == 3:
            print('Saliendo del programa, Tenga un gran dia')
            finalizacion = False
        else:
            print('Opcion no valida, Intente de nuevo. \n')
            
#ejecutar el menu
menu()

            
