# Importar Librerias
import numpy as np

def fitness(R):
  
  W = R[0]
  L = R[1]
  m = R[2]
  n = R[3]
  
  beta = 4.5e-6
  gamma = 0.01
  Tech_Poly = 0.000001
  
  V_Th = 0.69                                   #Voltaje Umbral
  V_DS = 5                                      #Voltaje Drain Source
  
  Res_sheet = 25
  
  VR_data = [1.00E-07, 2.50E-02, 1.00E-01, 2.25E-01, 4.00E-01, 6.25E-01, 9.00E-01, 1.23E+00, 1.57E+00, 1.84E+00, 2.07E+00]
  
  #Calculo de la resistencia
  n_round = round(n)
  m_round = round(m)
  
  if n_round % 2 == 0:
    n_round = n_round
  else:
    if n_round > m_round:
      n_round = n_round-1
    else:
      n_round = n_round+1
    
  equinas = n_round-1
  
  cuadros = ((n_round*m_round)-(m_round-1))-equinas
  cuadros_con_esquinas = cuadros + (equinas*(2/3))
  Resistencia_total = Res_sheet*cuadros_con_esquinas
  
  #Calculo de la corriente
  VR_e = []
  for VGS in range(0, 50, 5):
    VGS = VGS / 10.0
    if VGS <= V_Th:
      Id = 0.0
      VR_e.append(Resistencia_total*Id)
    else:
      Id = (beta/2)*(W/L)*((VGS - V_Th)**2)*(1+(gamma*V_DS))
      VR_e.append(Resistencia_total*Id)

  total_sum  = 0
  for i in range(0,len(VR_data)-1):
    total_sum  = total_sum  + ((VR_data[i]-VR_e[i])**2)
  
  mse = total_sum/len(VR_data)
   
  return mse