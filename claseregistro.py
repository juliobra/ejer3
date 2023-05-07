class Registro:
    def __init__(self, temperatura, humedad, presion):
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presion = presion
    
    def __str__ (self):
      return "%f %f %f " % (self.__temperatura, self.__humedad, self.__presion)
    
    def getTemperatura (self):
      return self.__temperatura
    
    def getHumedad (self):
      return self.__humedad

    def getPresion (self):
      return self.__presion

    