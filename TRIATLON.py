#TRIATLON

#Importamos modulos
import os
import rich
from rich.console import Console
from datetime import timedelta
console = Console()
#Clase participante donde estan los datos de cada uno
class participante:
    def __init__(self, nombre, apellidos, dni, fecha_nac):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.fecha_nac = fecha_nac
#Clase triatlon donde estan los resultados y las funciones
class triatlon:
    def __init__(self):
        self.participantes = {}
        self.resultados = {}
           
    #PARTICIPANTE----------------------------------------------------------------
    def agregar_part(self, nombre, apellidos, dni, fecha_nac):#Esta funcion nos permite agregar a los participantes
        if dni in self.participantes:
            console.print('[red]Usuario ya registrado, recuerda que un usuario tiene un DNI único[/]')
            print('')
            input('Pulsa ENTER para continuar')
            return
        else:
            self.participantes[dni] = participante(nombre, apellidos, dni, fecha_nac)
            console.print(f'[green3]{nombre} ha sido añadido correctamente como participante[/]')
            print('')
            input('Pulsa ENTER para continuar')

    def mostrar_part(self):#Esta funcion muestra los participantes segun el usuario quiera ordenarlos
        if not self.participantes:
            console.print('[red]No hay participantes registrados[/]')
            print('')
            input('Pulsa ENTER para continuar')
            return

        os.system('cls')
        console.print('[blue]VISUALIZACIÓN DE PARTICIPANTES[/]')
        print('-------------------------------------------------------------------')
        print('')
        print('¿Cómo quieres ordenar los participantes? (nombre/apellidos/dni/fecha)')
        orden = input('Introduce el criterio: ').lower()

        # Crear lista de participantes para ordenar
        lista_participantes = list(self.participantes.values())

        if orden == 'nombre':
            lista_participantes.sort(key=lambda x: x.nombre)
        elif orden == 'apellidos':
            lista_participantes.sort(key=lambda x: x.apellidos)
        elif orden == 'dni':
            lista_participantes.sort(key=lambda x: x.dni)
        elif orden == 'fecha':
            lista_participantes.sort(key=lambda x: x.fecha_nac)
        else:
            console.print('[red]Criterio no válido. Mostrando sin ordenar.[/]')
            print('')

        os.system('cls')
        console.print(f'[blue]PARTICIPANTES ORDENADOS POR {orden.upper()}[/]')
        print('-------------------------------------------------------------------')
        print('')
        
        for participante in lista_participantes:
            console.print(f'[green3]Nombre: {participante.nombre}[/]')
            console.print(f'[green3]Apellidos: {participante.apellidos}[/]')
            console.print(f'[green3]DNI: {participante.dni}[/]')
            console.print(f'[green3]Fecha de nacimiento: {participante.fecha_nac}[/]')
            print('')
            print('-------------------------------------------------------------------')
            print('')

        input('Pulsa ENTER para continuar')

    def modificar_part(self, dni): #Esta funcion permite modificar los datos de los participantes
        if dni not in self.participantes:
            console.print("[red]Participante no encontrado.[/]")
            print('')
            input('Pulsa ENTER para continuar')           
            return

        print('')
        p = self.participantes[dni]
        nombre = input(f"Nuevo nombre ({p.nombre}): ") or p.nombre
        apellidos = input(f"Nuevos apellidos ({p.apellidos}): ") or p.apellidos
        fecha_nac = input(f"Nueva fecha de nacimiento ({p.fecha_nac}): ") or p.fecha_nac
        
        self.participantes[dni] = participante(nombre, apellidos, dni, fecha_nac)
        
        console.print("[green3]Participante actualizado correctamente.[/]")
        print('')
        input('Pulsa ENTER para continuar')
        return True

    def eliminar_part(self, dni): #Con esta funcion eliminamos particantes
        if dni in self.participantes:
            del self.participantes[dni]
            console.print('[green3]Participante eliminado correctamente[/]')
            print('')
            input('Pulsa ENTER para continuar')
        else:
            console.print('[red]Participante no añadido o no econtrado')
            print('')
            input('Pulsa ENTER para continuar')

    #TRIATLON-----------------------------------------------------------------------
    def registrar_resul(self): #Registramos resultados para cada participante
        if not self.participantes: #Comprobamos si no hay participantes registrados
            console.print('[red]No hay participantes registrados[/]')
            print('')
            input('Pulsa ENTER para continuar')
            return

        dni = int(input('Introduce el DNI del participante: '))

        if dni not in self.participantes: #No ha introducido un dni correcto
            console.print('[red]Participante no encontrado[/]')
            print('')
            input('Pulsa ENTER para continuar')
            return

        # Función auxiliar para validar y convertir tiempo
        def validar_tiempo(tiempo_str):
            if len(tiempo_str.split(':')) != 3:
                return None
            horas, minutos, segundos = tiempo_str.split(':')
            if not (horas.isdigit() and minutos.isdigit() and segundos.isdigit()):
                return None
            horas = int(horas)
            minutos = int(minutos)
            segundos = int(segundos)
            if minutos >= 60 or segundos >= 60:
                return None
            return timedelta(hours=horas, minutes=minutos, seconds=segundos)

        # Mostrar tiempos actuales si existen
        if dni in self.resultados:
            print('')
            console.print('[blue]Tiempos actuales del participante:[/]')
            print('-------------------------------------------------------------------')
            print('')
            print(f'Natación: {self.resultados[dni]["natacion"]}')
            print(f'Ciclismo: {self.resultados[dni]["ciclismo"]}')
            print(f'Carrera: {self.resultados[dni]["carrera"]}')
            print('')
            console.print('[yellow]Introduce los nuevos tiempos (deja en blanco para mantener el actual)[/]')
            print('')
        os.system('cls')
        console.print('[blue]Registro de tiempos (formato HH:MM:SS)[/]')
        print('-------------------------------------------------------------------')
        print('')

        # Natación
        tiempo_natacion = input('Tiempo de natación (HH:MM:SS): ')
        if tiempo_natacion.strip():  # Si se introduce un nuevo tiempo
            tiempo_natacion_delta = validar_tiempo(tiempo_natacion)
            if tiempo_natacion_delta is None:
                console.print('[red]Formato de tiempo incorrecto para natación. Usa el formato HH:MM:SS[/]')
                print('')
                input('Pulsa ENTER para continuar')
                return
        else:  # Si no se introduce tiempo nuevo
            if dni in self.resultados:
                tiempo_natacion_delta = self.resultados[dni]['natacion']
            else:
                console.print('[red]Debes introducir un tiempo para natación[/]')
                print('')
                input('Pulsa ENTER para continuar')
                return

        # Ciclismo
        tiempo_ciclismo = input('Tiempo de ciclismo (HH:MM:SS): ')
        if tiempo_ciclismo.strip():
            tiempo_ciclismo_delta = validar_tiempo(tiempo_ciclismo)
            if tiempo_ciclismo_delta is None:
                console.print('[red]Formato de tiempo incorrecto para ciclismo. Usa el formato HH:MM:SS[/]')
                print('')
                input('Pulsa ENTER para continuar')
                return
        else:
            if dni in self.resultados:
                tiempo_ciclismo_delta = self.resultados[dni]['ciclismo']
            else:
                console.print('[red]Debes introducir un tiempo para ciclismo[/]')
                print('')
                input('Pulsa ENTER para continuar')
                return

        # Carrera
        tiempo_carrera = input('Tiempo de carrera a pie (HH:MM:SS): ')
        if tiempo_carrera.strip():
            tiempo_carrera_delta = validar_tiempo(tiempo_carrera)
            if tiempo_carrera_delta is None:
                console.print('[red]Formato de tiempo incorrecto para carrera. Usa el formato HH:MM:SS[/]')
                print('')
                input('Pulsa ENTER para continuar')
                return
        else:
            if dni in self.resultados:
                tiempo_carrera_delta = self.resultados[dni]['carrera']
            else:
                console.print('[red]Debes introducir un tiempo para carrera[/]')
                print('')
                input('Pulsa ENTER para continuar')
                return

        # Tiempo total
        tiempo_total = tiempo_natacion_delta + tiempo_ciclismo_delta + tiempo_carrera_delta

        # Guardar o actualizar resultados
        self.resultados[dni] = {
            'natacion': tiempo_natacion_delta,
            'ciclismo': tiempo_ciclismo_delta,
            'carrera': tiempo_carrera_delta,
            'total': tiempo_total
        }

        
        console.print('[green3]Resultados registrados correctamente[/]')
        print('')
        input('Pulsa ENTER para continuar')

    def ver_resul(self): #Ponemos clasificacion de resultados
        if not self.resultados: #Comprobamos si hay resultados registrados
            console.print('[red]No hay resultados registrados[/]')
            print('')
            input('Pulsa ENTER para continuar')
            return
        #Tabla
        while True:
            os.system('cls')
            console.print('[blue]VISUALIZACIÓN DE RESULTADOS[/]')
            print('-------------------------------------------------------------------')
            print('')
            print('1. Ver resultados individuales')
            print('2. Ver clasificación por natación')
            print('3. Ver clasificación por ciclismo')
            print('4. Ver clasificación por carrera')
            print('5. Ver clasificación general')
            print('6. Volver al menú anterior')
            print('')
            print('-------------------------------------------------------------------')
            opcion = int(input('Introduce una opción válida: '))

            if opcion == 1:
                os.system('cls')
                console.print('[blue]RESULTADOS INDIVIDUALES[/]')
                print('-------------------------------------------------------------------')
                print('')
                for dni, resultado in self.resultados.items():
                    participante = self.participantes[dni]
                    console.print(f'[green3]Participante: {participante.nombre} {participante.apellidos} (DNI: {dni})[/]')
                    print('')
                    print(f'Natación: {resultado["natacion"]}')
                    print(f'Ciclismo: {resultado["ciclismo"]}')
                    print(f'Carrera: {resultado["carrera"]}')
                    print(f'Tiempo Total: {resultado["total"]}')
                    print('')
                    print('-------------------------------------------------------------------')
                    print('')

            elif opcion == 2:
                os.system('cls')
                console.print('[blue]CLASIFICACIÓN POR NATACIÓN[/]')
                print('-------------------------------------------------------------------')
                print('')
                # Ordenar por tiempo de natación
                clasificacion = sorted(self.resultados.items(), 
                                    key=lambda x: x[1]['natacion'])
                for pos, (dni, resultado) in enumerate(clasificacion, 1):
                    participante = self.participantes[dni]
                    if pos == 1:
                        console.print(f'[gold1]{pos}º - {participante.nombre} {participante.apellidos}: {resultado["natacion"]}[/]')
                    elif pos == 2:
                        console.print(f'[silver]{pos}º - {participante.nombre} {participante.apellidos}: {resultado["natacion"]}[/]')
                    elif pos == 3:
                        console.print(f'[brown]{pos}º - {participante.nombre} {participante.apellidos}: {resultado["natacion"]}[/]')
                    else:
                        print(f'{pos}º - {participante.nombre} {participante.apellidos}: {resultado["natacion"]}')

            elif opcion == 3:
                os.system('cls')
                console.print('[blue]CLASIFICACIÓN POR CICLISMO[/]')
                print('-------------------------------------------------------------------')
                print('')
                # Ordenar por tiempo de ciclismo
                clasificacion = sorted(self.resultados.items(), 
                                    key=lambda x: x[1]['ciclismo'])
                for pos, (dni, resultado) in enumerate(clasificacion, 1):
                    participante = self.participantes[dni]
                    if pos == 1:
                        console.print(f'[gold1]{pos}º - {participante.nombre} {participante.apellidos}: {resultado["ciclismo"]}[/]')
                    elif pos == 2:
                        console.print(f'[silver]{pos}º - {participante.nombre} {participante.apellidos}: {resultado["ciclismo"]}[/]')
                    elif pos == 3:
                        console.print(f'[brown]{pos}º - {participante.nombre} {participante.apellidos}: {resultado["ciclismo"]}[/]')
                    else:
                        print(f'{pos}º - {participante.nombre} {participante.apellidos}: {resultado["ciclismo"]}')

            elif opcion == 4:
                os.system('cls')
                console.print('[blue]CLASIFICACIÓN POR CARRERA[/]')
                print('-------------------------------------------------------------------')
                print('')
                # Ordenar por tiempo de carrera
                clasificacion = sorted(self.resultados.items(), 
                                    key=lambda x: x[1]['carrera'])
                for pos, (dni, resultado) in enumerate(clasificacion, 1):
                    participante = self.participantes[dni]
                    if pos == 1:
                        console.print(f'[gold1]{pos}º - {participante.nombre} {participante.apellidos}: {resultado["carrera"]}[/]')
                    elif pos == 2:
                        console.print(f'[silver]{pos}º - {participante.nombre} {participante.apellidos}: {resultado["carrera"]}[/]')
                    elif pos == 3:
                        console.print(f'[brown]{pos}º - {participante.nombre} {participante.apellidos}: {resultado["carrera"]}[/]')
                    else:
                        print(f'{pos}º - {participante.nombre} {participante.apellidos}: {resultado["carrera"]}')

            elif opcion == 5:
                os.system('cls')
                console.print('[blue]CLASIFICACIÓN GENERAL[/]')
                print('-------------------------------------------------------------------')
                print('')
                # Ordenar por tiempo total
                clasificacion = sorted(self.resultados.items(), 
                                    key=lambda x: x[1]['total'])
                for pos, (dni, resultado) in enumerate(clasificacion, 1):
                    participante = self.participantes[dni]
                    if pos == 1:
                        console.print(f'[gold1]{pos}º - {participante.nombre} {participante.apellidos}: {resultado["total"]}[/]')
                    elif pos == 2:
                        console.print(f'[silver]{pos}º - {participante.nombre} {participante.apellidos}: {resultado["total"]}[/]')
                    elif pos == 3:
                        console.print(f'[brown]{pos}º - {participante.nombre} {participante.apellidos}: {resultado["total"]}[/]')
                    else:
                        print(f'{pos}º - {participante.nombre} {participante.apellidos}: {resultado["total"]}')

            elif opcion == 6:
                return

            else:
                console.print('[red]Opción no válida[/]')
                print('')
            
            print('')
            input('Pulsa ENTER para continuar')



def menu():

    triatlon_menu = triatlon()

    while True:
        os.system('cls')
        console.print('[blue]MENÚ PRINCIPAL[/]')
        print('-------------------------------------------------------------------')
        print('')
        print('1. Participantes')
        print('2. Triatlón')
        print('3. Salir')
        print('')
        print('-------------------------------------------------------------------')
        opcion1 = int(input('Introduce una opción válida: '))
        #PARTICIPANTES---------------------------------------------------------------------------------------
        if opcion1 == 1:
            os.system('cls')
            console.print('[blue]MENÚ DE PARTICIPANTES[/]')
            print('-------------------------------------------------------------------')
            print('')
            print('1. Agregar Participantes')
            print('2. Mostrar Participantes')
            print('3. Modificar Participantes')
            print('4. Eliminar Participantes')
            print('5. Salir')
            print('')
            print('-------------------------------------------------------------------')
            opcion_part = int(input('Introduce una opción válida: '))

            if opcion_part == 1:
                os.system('cls')
                console.print('[blue]Agregar Participantes[/]')
                print('-------------------------------------------------------------------')
                print('')
                nombre = input('Introduce el nombre del participante: ')
                apellidos = input('Introduce los apellidos del participante: ')
                dni = int(input('Introduce el DNI del participante: '))
                fecha_nac = input('Introduce la fecha de nacimiento del participante(DD/MM/AAAA): ')
                print('')
                print('-------------------------------------------------------------------')
                triatlon_menu.agregar_part(nombre, apellidos, dni, fecha_nac)

            elif opcion_part == 2:
                os.system('cls')
                console.print('[blue]Mostrar Participantes[/]')
                print('-------------------------------------------------------------------')
                print('')
                triatlon_menu.mostrar_part()
                
            elif opcion_part == 3:
                os.system('cls')
                console.print('[blue]Modificar Participantes[/]')
                print('-------------------------------------------------------------------')
                print('')
                dni = int(input('Introduce el DNI del participante que quiere modificar: '))
                print('')
                print('-------------------------------------------------------------------')
                if triatlon_menu.modificar_part(dni):
                    continue

            elif opcion_part == 4:
                os.system('cls')
                console.print('[blue]Eliminar Participantes[/]')
                print('-------------------------------------------------------------------')
                print('')
                dni = int(input('Introduce el DNI del participante que desea eliminar: '))
                print('')
                print('-------------------------------------------------------------------')
                triatlon_menu.eliminar_part(dni)
            
            elif opcion_part == 5:
                os.system('cls')
                print('Saliendo')
                
            else:
                os.system('cls')
                print('Introduce una opción válida, por favor')
                input('Pulsa ENTER para continuar')    
        #Triatlon.............................................................................................................
        elif opcion1 == 2:
            os.system('cls')
            console.print('[blue]MENÚ DE TRIATLÓN[/]')
            print('-------------------------------------------------------------------')
            print('')
            print('1. Registrar Resultados')
            print('2. Ver Resultados')
            print('3. Salir')
            print('')
            print('-------------------------------------------------------------------')
            opcion_triat = int(input('Introduce una opción válida: '))

            if opcion_triat == 1:
                os.system('cls')
                console.print('[blue]Registrar Resultados[/]')
                print('-------------------------------------------------------------------')
                print('')
                triatlon_menu.registrar_resul()
            
            elif opcion_triat == 2:
                os.system('cls')
                console.print('[blue]Ver Resultados[/]')
                print('-------------------------------------------------------------------')
                print('')
                triatlon_menu.ver_resul()
            
            elif opcion_triat == 3:
                os.system('cls')
                print('Saliendo')
            
            else:
                os.system('cls')
                print('Introduce una opción válida, por favor')
                input('Pulsa ENTER para continuar')
        
        elif opcion1 == 3:
            os.system('cls')
            print('Saliendo')
            break
    
menu()