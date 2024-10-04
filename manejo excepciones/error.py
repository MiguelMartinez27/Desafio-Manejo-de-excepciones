class DimensionError(Exception):
    """
    Excepción personalizada para errores relacionados con dimensiones fuera de los límites permitidos.

    Atributos:
    -----------
    mensaje : str
        El mensaje descriptivo del error.
    dimension : str, opcional
        La dimensión que causó el error (por ejemplo, 'ancho' o 'alto').
    maximo : int, opcional
        El valor máximo permitido para la dimensión.

    Métodos:
    --------
    __init__(mensaje, dimension=None, maximo=None)
        Inicializa una instancia de DimensionError con un mensaje y opcionalmente 
        la dimensión que falló y el valor máximo permitido.
    
    __str__()
        Retorna una representación en cadena de la excepción. Si se proporciona solo 
        el mensaje, se usa el comportamiento de la clase base. Si se proporciona la 
        dimensión y/o el máximo, retorna un mensaje detallado.
    """
    
    def __init__(self, mensaje, dimension=None, maximo=None):
        """
        Inicializa una nueva instancia de DimensionError.

        Parámetros:
        -----------
        mensaje : str
            El mensaje descriptivo del error.
        dimension : str, opcional
            La dimensión que causó el error.
        maximo : int, opcional
            El valor máximo permitido para la dimensión.
        """
        super().__init__(mensaje)
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self):
        """
        Retorna una representación en cadena de la excepción.

        Si solo se proporciona el mensaje, se utiliza el comportamiento de la clase base.
        Si se proporciona la dimensión y el máximo, retorna un mensaje personalizado.

        Retorna:
        --------
        str
            El mensaje de error, con detalles adicionales si están disponibles.
        """
        if self.dimension is None and self.maximo is None:
            return super().__str__()
        else:
            return f"{self.mensaje}. Dimensión: {self.dimension}, Máximo permitido: {self.maximo}"
