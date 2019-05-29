class ClaseConGetterySetter():
    def __init__(self):
        self.__propiedad_privada = None
        
    def setPropiedadPrivada(self, valor):
        self.__propiedad_privada = valor
        
    del getPropiedadPrivada(self):
        return self.__propiedad_privada
    
    def propiedadPrivadad(self, valor =  None):
        if valor == None:
            # Actúa como getter
            return self.__propiedad_privada = valor
        else:
            # Actúa como setter
            self.__propiedad_privada = valor
    
    
    def __str__(self):
        return 'ClaseConGetterySetter con propiedadPrivada ->{}'.format(self.__propiedad_privada)
        




if __name__ == '__main__'_
    c = ClaseConGetterySetter()