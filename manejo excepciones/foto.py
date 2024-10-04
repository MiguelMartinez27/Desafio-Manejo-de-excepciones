from error import DimensionError

class Foto:
    """
    Clase que representa una foto con dimensiones de ancho y alto. 
    Controla que las dimensiones se mantengan dentro de un rango permitido.

    Atributos:
    -----------
    MAX : int
        Valor máximo permitido para el ancho y alto de la foto (2500 por defecto).
    
    Métodos:
    --------
    __init__(ancho: int, alto: int, ruta: str)
        Inicializa una instancia de Foto con las dimensiones y la ruta proporcionadas.
    
    ancho : int
        Propiedad que obtiene el valor actual del ancho de la foto.
    
    ancho(ancho: int) -> None
        Setter que establece un nuevo valor para el ancho, lanzando una excepción 
        DimensionError si el valor está fuera del rango permitido.
    
    alto : int
        Propiedad que obtiene el valor actual del alto de la foto.
    
    alto(alto: int) -> None
        Setter que establece un nuevo valor para el alto, lanzando una excepción 
        DimensionError si el valor está fuera del rango permitido.
    """
    
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        """
        Inicializa una nueva instancia de Foto.

        Parámetros:
        -----------
        ancho : int
            El valor inicial del ancho de la foto.
        alto : int
            El valor inicial del alto de la foto.
        ruta : str
            La ruta donde se almacena la foto.
        """
        self.__ancho = ancho
        self.__alto = alto
        self.ruta = ruta

    @property
    def ancho(self) -> int:
        """
        Retorna el valor actual del ancho de la foto.

        Retorna:
        --------
        int
            El valor del ancho de la foto.
        """
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho: int) -> None:
        """
        Establece un nuevo valor para el ancho de la foto.

        Parámetros:
        -----------
        ancho : int
            El nuevo valor para el ancho de la foto.

        Lanza:
        ------
        DimensionError:
            Si el ancho está fuera de los límites permitidos (menor a 1 o mayor a MAX).
        """
        if ancho < 1 or ancho > self.MAX:
            raise DimensionError("Ancho fuera de los límites permitidos", "ancho", self.MAX)
        self.__ancho = ancho

    @property
    def alto(self) -> int:
        """
        Retorna el valor actual del alto de la foto.

        Retorna:
        --------
        int
            El valor del alto de la foto.
        """
        return self.__alto

    @alto.setter
    def alto(self, alto: int) -> None:
        """
        Establece un nuevo valor para el alto de la foto.

        Parámetros:
        -----------
        alto : int
            El nuevo valor para el alto de la foto.

        Lanza:
        ------
        DimensionError:
            Si el alto está fuera de los límites permitidos (menor a 1 o mayor a MAX).
        """
        if alto < 1 or alto > self.MAX:
            raise DimensionError("Alto fuera de los límites permitidos", "alto", self.MAX)
        self.__alto = alto
