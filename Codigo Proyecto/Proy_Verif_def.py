#Importar Librerias
import matplotlib.pyplot as plt

def Proy_Verif_def(solution):
    #Resistor voltage measured/simulated data
    VR_data = [1.00E-07, 2.50E-02, 1.00E-01, 2.25E-01, 4.00E-01, 6.25E-01, 9.00E-01, 1.23E+00, 1.57E+00, 1.84E+00, 2.07E+00]
    
    #gate-to-source voltage sweep  
    VGS_graph = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]

    #fixed parameters
    VDS = 5         #drain-to-source voltage  
    VT = 0.69       #treshold voltage (for silicon)
    beta = 4.5e-6   #transistor's beta 
    rsq = 25        #sheet resistance, ohms per square
    gamma = 0.01

    #transistor variables
    W = solution[0]        #gate width
    L = solution[1]        #gate length
    print('W: '+str(round(1e6*W,1))+'μm\t'+'L: '+str(round(1e6*L,1))+'μm')

    #resistor
    m = solution[2]          #resistor squares per line
    n = solution[3]          #resistor lines

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
    Resistencia_total = rsq*cuadros_con_esquinas
    print("R:", Resistencia_total, 'Ω')

    #transistor's drain current I_D (for each V_GS value)
    #resistor voltage V_R = I_D * R
    VR = []
    for VGS in range(0, 55, 5):
        VGS = VGS / 10.0
        if VGS <= VT:
            ID = 0.0
            VR.append(Resistencia_total*ID)
        else:
            ID = (beta/2)*(W/L)*((VGS - VT)**2)*(1+(gamma*VDS))
            VR.append(Resistencia_total*ID)
    
    # mean square error
    total_sum  = 0
    for i in range(0,len(VR_data)-1):
        total_sum  = total_sum  + ((VR_data[i]-VR[i])**2)
        
    MSE = total_sum/len(VR_data)

    print("Mean Sq Error: ", round(MSE, 7)*100, '%')

    plt.figure(2)
    plt.plot(VGS_graph,VR_data)
    plt.plot(VGS_graph,VR)
    plt.grid()
    plt.legend(['data','calculated'])
    plt.title('$V_R$ vs $V_{GS}$')
    plt.ylabel('resistor voltage (V)')
    plt.xlabel('gate-to-source voltage (V)')

    plt.show()