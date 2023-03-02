%% Tarea 1
% Computación Aplicada
% José Rubén Villicaña Ibargüengoytia   |A01654347
% Frida Berenice Rangel Garcia          |A01651385
% Ignacio Alvarado Reyes                |A01656149

%% Clear the enviroment
clear all
close all
clc

%% Generar la matriz
mapa_Voronoi = zeros(256);

%% Generar
x = [];
y = [];
for i = 1:16
    x(i) = randi(256);
    y(i) = randi(256);
    mapa_Voronoi(x,y)=i;
end

%% Revisar distancias Ecleudianas pixel por pixel
Distancias = [];
for i = 1:256
    for j = 1:256
        for k = 1:16
            punto_actual(1) = i;
            punto_actual(2) = j;
            punto_random(1) = x(k);
            punto_random(2) = y(k);
            Distancias(k) = pdist2(punto_actual,punto_random,'euclidean');
        end
        [distancia_minima Indice] = min(Distancias);
        mapa_Voronoi(i,j)= Indice;
    end
end

figure(1)
imagesc(mapa_Voronoi); colorbar
title('Mapa de Voronoi')

figure(2)
imagesc(mapa_Voronoi); colormap('gray'); colorbar
title('Mapa de Voronoi en Gris')

