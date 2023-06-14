#Este programa genera las nuevas poblaciones

from newindiv import *

def population(n,cromosoma_leng):
  pop = []                                  #Variable que se le añaden individuos
  
  for i in range(0,n):
    pop.append(newindiv(cromosoma_leng))    #Haz un individuo del tamaño de cromosoma_leng  
  
  return pop