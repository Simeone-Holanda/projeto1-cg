# Calculo das transformações

def world_to_ndcx(x_value, x_min, x_max):
    """  Função responsável por converter o valor de X no mundo para NDCX  """
    ndcx = (x_value - x_min) / (x_max - x_min)
    
    return ndcx

def world_to_ndcy(y_value, y_min, y_max):
    """  Função responsável por converter o valor de Y no mundo para NDCY  """
    ndcy = (y_value - y_min) / (y_max - y_min)
    
    return ndcy
    
def ndcx_to_dcx(ndcx, ndh):
    """  Função responsável por converter o valor de NDCX para DCX  """
    dcx = round(ndcx * (ndh - 1))
    
    return dcx

def ndcy_to_dcy(ndcy, ndv):
    """  Função responsável por converter o valor de NDCY para DCY  """
    dcx = round(ndcy * (ndv - 1))
    
    return dcx
