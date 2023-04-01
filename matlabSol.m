%%matlabSol

syms x y
A = x + 3*y  == 300;
B = 1.5*x + 2*y == 350;


soluciones = solve([A,B], [x, y]);

compX = double(soluciones.x)
compY = double(soluciones.y)

