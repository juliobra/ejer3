from claseregistro import Registro
import csv

class Mes:
  def __init__(self,dia,hora) :
    self.__lista_mete = [[0.0 for x in range(dia)] for y in range(hora)]

  def __str__ (self):
    print(self.__lista_mete)
  
  def agregarmes(self, unmes):
    self.__lista_mete.append(unmes)
  
  def testmes(self):
    archivo= open('variables.csv')
    reader= csv.reader (archivo, delimiter = ',')
    for fila in reader:
      dia = int(fila[0])
      hora = int(fila[1])
      temperatura = float(fila[2])
      humedad = float(fila[3])
      presion = float(fila[4])
      registro = Registro(temperatura, humedad, presion)
      self.__lista_mete[dia-1][hora] = registro
      print("dia{} hora {} lista{}".format(dia, hora,self.__lista_mete[dia-1][hora]))
    archivo.close()
    
    # Menú de opciones
    while True:
      print("Seleccione una opción:")
      print("1. Mostrar para cada variable el día y hora de menor y mayor valor.")
      print("2. Indicar la temperatura promedio mensual por cada hora.")
      print("3. Dado un número de día, listar los valores de las tres variables para cada hora del día dado.")
      print("4. Salir")
      
      opcion = int(input())

      if opcion == 1:
     if opcion == 1:
        # Encontrar día y hora de menor y mayor valor para cada variable
        min_temperatura = float("inf")
        max_temperatura = float("-inf")
        min_humedad = float("inf")
        max_humedad = float("-inf")
        min_presion = float("inf")
        max_presion = float("-inf")
        for dia in range(len(listames.__lista_mete)):
            for hora in range(len(listames.__lista_mete[dia])):
                registro = listames.__lista_mete[dia][hora]
                if registro.getTemperatura() < min_temperatura:
                    min_temperatura = registro.getTemperatura()
                    min_temperatura_dia = dia + 1
                    min_temperatura_hora = hora
                if registro.getTemperatura() > max_temperatura:
                    max_temperatura = registro.getTemperatura()
                    max_temperatura_dia = dia + 1
                    max_temperatura_hora = hora
                if registro.getHumedad() < min_humedad:
                    min_humedad = registro.getHumedad()
                    min_humedad_dia = dia + 1
                    min_humedad_hora = hora
                if registro.getHumedad() > max_humedad:
                    max_humedad = registro.getHumedad()
                    max_humedad_dia = dia + 1
                    max_humedad_hora = hora
                if registro.
                    max_humedad_hora = hora
getPresion() < min_presion:
                    min_presion = registro.getPresion()
                    min_presion_dia = dia + 1
                    min_presion_hora = hora
                if registro.getPresion() > max_presion:
                    max_presion = registro.getPresion()
                    max_presion_dia = dia + 1
                    max_presion_hora = hora
        print("Temperatura: Mínimo - Día {} Hora {} / Máximo - Día {} Hora {}".format(min_temperatura_dia, min_temperatura_hora, max_temperatura_dia, max_temperatura_hora))
        print("Humedad: Mínimo - Día {} Hora {} / Máximo - Día {} Hora {}".format(min_humedad_dia, min_humedad_hora, max_humedad_dia, max_humedad_hora))
        print("Presión: Mínimo - Día {} Hora {} / Máximo - Día {} Hora {}".format(min_presion_dia, min_presion_hora, max_presion_dia, max_presion_hora))
 
      elif opcion == 2:
        for hora in range(len(self.__lista_mete[0])):
        sum_temperatura = 0.0
        count = 0
        for dia in range(len(self.__lista_mete)):
          if self.__lista_mete[dia][hora] != 0.0:
            sum_temperatura += self.__lista_mete[dia][hora].getTemperatura()
            count += 1
        if count > 0:
          temperatura_promedio = sum_temperatura / count
          print("Hora {}: Temperatura promedio mensual = {}".format(hora, temperatura_promedio))
        else:
          print("No hay datos registrados para la hora {}".format(hora))
      
      elif opcion == 3:
  dia = int(input("Ingrese el número de día: "))
        if dia > 0 and dia <= len(self.__lista_mete):
          print("Valores para el día {}:".format(dia))
          for hora in range(len(self.__lista_mete[dia-1])):
            registro = self.__lista_mete[dia-1][hora]
            if registro != 0.0:
              temperatura = registro.getTemperatura()
              humedad = registro.getHumedad()
              presion = registro.getPresion()
              print("Hora {}: Temperatura = {}, Humedad = {}, Presión = {}".format(hora, temperatura, humedad, presion))
            else:
              print("Hora {}: No hay datos registrados".format(hora))
        else:
          print("El número de día ingresado es inválido")
      elif opcion == 4:
          printf("salio")          