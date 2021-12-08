# Calculo das transformações


class Transformar:

    def __init__(self) -> None:
        ...

    def world_to_ndcx(self, x_value, x_tela):
        """  Função responsável por converter o valor de X no mundo para NDCX  """
        
        self.ndcx = (((x_value-(-x_tela))/(x_tela-(-x_tela)))*2)-1
        #self.ndcx = 2 * ((x_value - 0) / (x_tela - 0)) - 1
        
        #self.ndcx = (2 * x_value - x_tela) / (x_tela)
        return self.ndcx

    def world_to_ndcy(self, y_value, y_tela):
        """  Função responsável por converter o valor de Y no mundo para NDCY  """

        self.ndcy = (((y_value-(-y_tela))/(y_tela-(-y_tela)))*2)-1
        #self.ndcy = 2 * ((y_value - 0) / (y_tela - 0)) - 1
        
        #self.ndcy = (2 * y_value - y_tela) / (y_tela)
        return self.ndcy
        
    def ndcx_to_dcx(self, ndcx, ndh):
        """  Função responsável por converter o valor de NDCX para DCX  """
        self.dcx = round(ndcx * (ndh - 1))
        
        return self.dcx

    def ndcy_to_dcy(self, ndcy, ndv):
        """  Função responsável por converter o valor de NDCY para DCY  """
        self.dcx = round(ndcy * (ndv - 1))
        
        return self.dcx
