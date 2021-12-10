# Calculo das transformações


class Transformar:

    @classmethod
    def world_to_ndcx(self, x_value, x_tela):
        """  Função responsável por converter o valor de X no mundo para NDCX  """
        
        self.ndcx = (((x_value)/(x_tela)) * 2) - 1
        
        return self.ndcx

    @classmethod
    def world_to_ndcy(self, y_value, y_tela):
        """  Função responsável por converter o valor de Y no mundo para NDCY  """

        self.ndcy = (((y_value)/(y_tela)) * 2) - 1
        self.ndcy = self.ndcy * (-1)
        
        return self.ndcy
       
    @classmethod 
    def ndcx_to_dcx(self, ndcx, ndh):
        """  Função responsável por converter o valor de NDCX para DCX  """
        self.dcx = round((ndcx + 1) * (ndh - 1))
        
        return self.dcx

    @classmethod
    def ndcy_to_dcy(self, ndcy, ndv):
        """  Função responsável por converter o valor de NDCY para DCY  """
        self.dcy = round(((ndcy *-1) + 1) * (ndv - 1))
        
        return self.dcy
    
   
