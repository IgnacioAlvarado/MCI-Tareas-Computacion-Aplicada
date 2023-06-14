def gray2real(indiv,gen_leng):
  
  #Vamos a generar 4 cadenas.
  #Segmento de bits de 0 a 15. 15=16-1
  g1 = indiv[0*gen_leng:(1*gen_leng)+1]       # W = de 0 a 16. Se le puso un bit mas a la W.                 Tiene 17 elementos
  g2 = indiv[(1*gen_leng)+1:(2*gen_leng)]     # L = de 17 a 31. Se le quito un bit para que fuera menor a W. Tiene 15 elementos           
  g3 = indiv[2*gen_leng:3*gen_leng]           # m = de 32 a 47.                                              Tiene 16 elementos
  g4 = indiv[3*gen_leng:4*gen_leng]           # n = de 48 a 63.                                              Tiene 16 elementos

  #Paso 1) Transformar de Gary a Bianrio. Bajar el primer digito.
  b1 = [g1[0]]
  b2 = [g2[0]]
  b3 = [g3[0]]
  b4 = [g4[0]]

  #Paso 2) Obtener toda la cadena en binario
  for i in range(0,gen_leng):
    b1.append(int(b1[i]^g1[i+1]))
    
  for i in range(0,gen_leng-2):
    b2.append(int(b2[i]^g2[i+1]))
    
  for i in range(0,gen_leng-1):
    b3.append(int(b3[i]^g3[i+1]))
    b4.append(int(b4[i]^g4[i+1]))

  #Paso 3)Convertir de binario a decimal
  d1 = 0
  d2 = 0
  d3 = 0
  d4 = 0
  
  for i in range(len(b1)):
    d1 += b1[i]*(2**(gen_leng-i))
    
  for i in range(len(b2)):
    d2 += b2[i]*(2**((gen_leng-2)-i))
    
  for i in range(len(b3)):
    d3 += b3[i]*(2**((gen_leng-1)-i))
    d4 += b4[i]*(2**((gen_leng-1)-i))

  #Paso 4)Obtener los valores reales. En el rango.
  comb_bits_17 = (2**(gen_leng+1))-1
  comb_bits_15 = (2**(gen_leng-1))-1
  comb_bits_16 = (2**gen_leng)-1
  
  #Transistor
  diff_total_t = (50e-6) - (2e-6)                                 # Rango de salida de los valores. En este caso, 48 [um].
  off_set_inicio_t = 2e-6                                         # Rango va de 2 [um] a 50 [um]
  r1 = (d1*diff_total_t/comb_bits_17) + off_set_inicio_t             # W
  r2 = (d2*diff_total_t/comb_bits_15) + off_set_inicio_t             # L
  
  #Resistencia
  diff_total = 50-2                                       # Rango de salida de los valores. En este caso, 48.
  off_set_inicio = 2                                      # Rango va de 2 a 50
  r3 = (d3*diff_total/comb_bits_16) +off_set_inicio          # m
  r4 = (d4*diff_total/comb_bits_16) +off_set_inicio          # n

  R = [r1,r2,r3,r4]          #Mandar un solo paquete de regreso con los 4 numeros reales
  
  return R
  