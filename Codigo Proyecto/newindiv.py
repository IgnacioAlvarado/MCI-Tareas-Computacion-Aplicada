import random

def newindiv(cromosoma_leng):
  indiv = []
  for i in range (0,cromosoma_leng):
    if random.random() > 0.5:
      indiv.append(1)
    else:
      indiv.append(0)
  return indiv