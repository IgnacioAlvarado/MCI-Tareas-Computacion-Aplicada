%% Tarea 2
% Computación Aplicada
% Alvarado Reyes, Ignacio               |A01656149
% Rangel García, Frida Berenice         |A01651385
% Villicaña Ibargüengoytia, José Rubén  |A01654347

%% Clear the enviroment
clear all
close all
clc

% Cargar los datos
Tiempo  = xlsread('Data3.xlsx',1,'A2:A302');
x       = xlsread('Data3.xlsx',1,'B2:B302');
y       = xlsread('Data3.xlsx',1,'C2:C302');
z       = xlsread('Data3.xlsx',1,'D2:D302');

% Obtener las curvas a partir de los datos
x_fit = createFit_x(Tiempo, x)
y_fit = createFit_y(Tiempo, y)
z_fit = createFit_z(Tiempo, z)

% Obtener los coeficientes
coeficientes_x = coeffvalues(x_fit)
coeficientes_y = coeffvalues(y_fit)
coeficientes_z = coeffvalues(z_fit)

% Calculo de gravedad 
Gravedad = -2*coeficientes_z(1)

% Calculo de velocidad inicial en magnitud
velocidad_magnitud = sqrt(((coeficientes_x(1))^2)+((coeficientes_y(1))^2)+((coeficientes_z(2))^2))

% Representacion de la velocidad inicial en vector
fprintf('|v| = %s x + %d y + %c z',coeficientes_x(1),coeficientes_y(1),coeficientes_z(2))

%% Funciones Utilizadas

%%%%%%%%%%%%%%%%%%%%%%%%%%% Funcion para x %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [fitresult, gof] = createFit_x(tiempo, x)
%% Fit: 'x'.
[xData, yData] = prepareCurveData( tiempo, x );

% Set up fittype and options.
ft = fittype( 'poly1' );

% Fit model to data.
[fitresult, gof] = fit( xData, yData, ft );

% Plot fit with data.
figure( 'Name', 'x' );
h = plot( fitresult, xData, yData );
legend( h, 'x vs. tiempo', 'x', 'Location', 'NorthEast', 'Interpreter', 'none' );
% Label axes
xlabel( 'Tiempo [s]', 'Interpreter', 'none' );
ylabel( 'x [m]', 'Interpreter', 'none' );
grid on
end

%%%%%%%%%%%%%%%%%%%%%%%%%%% Funcion para y %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [fitresult, gof] = createFit_y(tiempo, y)
%% Fit: 'y'.
[xData, yData] = prepareCurveData( tiempo, y );

% Set up fittype and options.
ft = fittype( 'poly1' );

% Fit model to data.
[fitresult, gof] = fit( xData, yData, ft );

% Plot fit with data.
figure( 'Name', 'y' );
h = plot( fitresult, xData, yData );
legend( h, 'y vs. tiempo', 'y', 'Location', 'NorthEast', 'Interpreter', 'none' );
% Label axes
xlabel( 'Tiempo [s]', 'Interpreter', 'none' );
ylabel( 'y [m]', 'Interpreter', 'none' );
grid on
end

%%%%%%%%%%%%%%%%%%%%%%%%%%% Funcion para z %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [fitresult, gof] = createFit_z(tiempo, z)
%% Fit: 'z'.
[xData, yData] = prepareCurveData( tiempo, z );

% Set up fittype and options.
ft = fittype( 'poly2' );

% Fit model to data.
[fitresult, gof] = fit( xData, yData, ft );

% Plot fit with data.
figure( 'Name', 'z' );
h = plot( fitresult, xData, yData );
legend( h, 'z vs. tiempo', 'z', 'Location', 'NorthEast', 'Interpreter', 'none' );
% Label axes
xlabel( 'Tiempo [s]', 'Interpreter', 'none' );
ylabel( 'z [m]', 'Interpreter', 'none' );
grid on
end