% ###################################################################
% ####                                                            ###
% ####       AEEM 6096: Spring 2015 - Kmeans                      ###
% ####                   Kelly_Kmeans.m                           ###
% ####                                                            ###
% ###################################################################

clc
clf 
clear all

options = [NaN 50 0.0001 0];
X = [1.4 8.9; 1.6 8.1; 1.8 7.3; 1.9 8.3];

[centers, U, objFun] = fcm(X, 2, options);

% ------------------------------------------ print centers
centers

% ------------------------------------------ print membership grades
U

% ------------------------------------------ plot objective function
plot(objFun)

maxU = max(U);
index1 = find(U(1,:) == maxU);
index2 = find(U(2,:) == maxU);

% ------------------------------------------ plot the clusters
plot(X(index1,1),X(index1,2),'ob')
hold on
plot(X(index2,1),X(index2,2),'or')
plot(centers(1,1),centers(1,2),'xb','MarkerSize',15,'LineWidth',3)
plot(centers(2,1),centers(2,2),'xr','MarkerSize',15,'LineWidth',3)
hold off