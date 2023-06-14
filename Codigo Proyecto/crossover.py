import random
#Programa para realizar la cruza
def crossover(parent_0,parent_1):
  if random.random() < 0.75:                      #Posibilidad de que no se cruzen de 75%
    cut = random.randint(0, len(parent_0)-1)
    #print("cut: ", cut)
    offspring_0 = []
    offspring_1 = []
    for i in range (len(parent_0)):
      if i <= cut:
        offspring_0.append(parent_0[i])
        offspring_1.append(parent_1[i])
      else:
        offspring_0.append(parent_1[i])
        offspring_1.append(parent_0[i])
  else:
    offspring_0=parent_0
    offspring_1=parent_1

  #print("off_0: ", offspring_0)
  #print("off_1: ", offspring_1)

  return offspring_0, offspring_1