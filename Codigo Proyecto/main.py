# Proyecto Final: Algoritmos Genéticos
# Computación Aplicada
# Alvarado Reyes Ignacio
# Rangel García Frida Berenice
# José Rubén Villicaña Ibargüengoytia

#GA_4v3f -> 4 variables a 3 funciones

# Importar Librerias
import numpy as np
import matplotlib.pyplot as plt

# Importar Códigos Externos
from population import *
from newindiv import *
from fitness import *
from gray2real import *
from selection import *
from crossover import *
from mutation import *
from Proy_Verif_def import *


def main():
    # Crear a la pobalción inicial
    n = 32                                                                  # Es el tamaño de la población. Arbitrario
    
    # Tamaño del gen y del cromosoma
    gen_leng = 16                                                           #16 bits por variable
    numero_variables = 4                                                    #Numero de variables a encontrar
    cromosoma_leng = numero_variables*gen_leng                              #4 variables de 16 bits. 64 bits.
    
    # Crear a la pobalción
    pop = population(n,cromosoma_leng)
    
    #Veces a iterar para obtener el resultado.
    total_generaciones = int(input("Cantidad total de generaciones: "))     #Veces a iterar para obtener el resultado.
    
    #Proceso de valor de aptitud. 
    # Para cada individuo se debe saber el valor de su aptitud.
    bestfitg = []
    for g in range(0,total_generaciones):
        fit = []                                                            #Almacena las aptitudes de los individuos
        
        for indiv in pop:
            fit.append(fitness(gray2real(indiv,gen_leng)))
        
        #Proceso de selección de individuos
        #fit_index es un apuntador en la lista de los fits.
        
        #Creación de parten 0
        fit_index = selection(fit)
        parent_0 = pop[fit_index]
        
        #Creación de parten 1
        fit_index = selection(fit)
        parent_1 = pop[fit_index]
        
        # Verificar que W sea mas del doble que L y que m o n no sea mayor que el doble de la otra
        P0_dec = gray2real(parent_0,gen_leng)
        while P0_dec[0] < 2*(P0_dec[1]) or P0_dec[2] > 2*P0_dec[3] or P0_dec[3] > 2*P0_dec[2]:          
            fit_index = selection(fit)
            parent_0 = pop[fit_index]
            P0_dec = gray2real(parent_0,gen_leng)
     
        #Se agrega la condicion de que ambos padres sean el mismo
        P1_dec = gray2real(parent_1,gen_leng)
        while P1_dec[0] < 2*(P1_dec[1]) or P1_dec[2] > 2*P1_dec[3] or P1_dec[3] > 2*P1_dec[2] or parent_1 == parent_0:
            fit_index = selection(fit)
            parent_1 = pop[fit_index]
            P1_dec = gray2real(parent_1,gen_leng)
            
        #Realizar la cruza entre padres
        offspring_0, offspring_1 = crossover(parent_0,parent_1)
        
        #Realizar la mutacion
        offspring_0 = mutation(offspring_0)
        offspring_1 = mutation(offspring_1)
        
        #Valuar en fitness
        fitp0 = fitness(gray2real(parent_0,gen_leng))
        fitp1 = fitness(gray2real(parent_1,gen_leng))
        fito0 = fitness(gray2real(offspring_0,gen_leng))
        fito1 = fitness(gray2real(offspring_1,gen_leng))
        
        #Nueva población
        newpop = []
        #Si el hijo 0 es menor que alguno de los padres -> Pasa
        if fito0 <= fitp0 or fito0 <= fitp1: 
            newpop.append(offspring_0)
        #Si el hijo 1 es menor que alguno de los padres -> Pasa
        if fito1 <= fitp0 or fito1 <= fitp1: 
            newpop.append(offspring_1)
        if fitp0 <= fito0 and fitp0 <= fito1: 
            newpop.append(parent_0)
        if fitp1 <= fito0 and fitp1 <= fito1: 
            newpop.append(parent_1)
            
        #Fillers (Relleno)
        while len(newpop) < n:
            filler = newindiv(cromosoma_leng)
            filler_real = gray2real(filler,gen_leng)
            if filler_real[0] > 2*(filler_real[1]) and filler_real[2] < 2*filler_real[3] and filler_real[3] < 2*filler_real[2]:
                newpop.append(filler)
                
        pop = newpop
        
        bestfit = np.min(fit)
        bestfitg.append(bestfit*100)

    fit = []
    for indiv in pop:
        fit.append(fitness(gray2real(indiv,gen_leng)))
        
    bestfit = np.min(fit)
    print("Best: ", bestfit*100)                        #Se multiplica por 100 por que es porcentaje
    
    bestindex = fit.index(bestfit)
    solution = gray2real(pop[bestindex],gen_leng)
    print("Solution[W,L,m,n]", [round(num, 7) for num in solution])
    
    plt.figure(1)
    plt.plot(range(total_generaciones), bestfitg)
    plt.grid()
    plt.title('MSE mínimo por generación')
    plt.ylabel('MSE (%)')
    plt.xlabel('Número de Generación')
    plt.show()
    
    Proy_Verif_def(solution)
            
        
main()


