  
def main():
  
  numero_variables = 4
  variables = {}
  for g in range(1,numero_variables):
    variable_name = f"g_{g}"
    # Generar el valor de la variable
    variable_value = g*1
    
    # Almacenar la variable en el diccionario
    variables[variable_name] = variable_value
    
    for variable_name, variable_value in variables.items():
        print(f"{variable_name} = {variable_value}")
    
main()