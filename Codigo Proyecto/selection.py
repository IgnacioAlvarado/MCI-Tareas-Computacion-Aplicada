import random
import numpy as np

def selection(fit):
    off_set = abs(np.min(fit))
  
    total_fit = (len(fit) * off_set) + sum(fit)
  
    pick = random.random()
    
    # Obtener la proporción inversa. Esto ya que queremos que el MSE mas probable sea el mas pequeño.
    proporcion_inversa = []
    for i in range(len(fit)):
        proporcion_inversa.append(1 / ((fit[i] + off_set) / total_fit))     
    
    # Se normaliza para pick   
    sum_inverse = sum(proporcion_inversa)
    normalized_inverse_proportions = []
    for inv_prop in proporcion_inversa:
        normalized_inverse_proportions.append(inv_prop / sum_inverse) 
        
    # Ruleta. Se escoge el fit index a partir de el pick random escogido
    fit_accumulative = 0
    for i in range(len(fit)):
        fit_accumulative += normalized_inverse_proportions[i]
        if fit_accumulative >= pick:
            fit_index = i
            break
  
    return fit_index
