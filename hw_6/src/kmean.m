% ###################################################################
% ####                                                            ###
% ####       AEEM 6096: Spring 2015 - Kmeans                      ###
% ####                   Kelly_Kmeans.m                           ###
% ####                                                            ###
% ###################################################################

clc
clf 
clear all

N=100;
X = [1.4 8.9; 1.6 8.1; 1.8 7.3; 1.9 8.3];

K=2; % Number of clusters
[idx, ctrs, SUMD, D] = kmeans(X,K); 

% ------------------------------------------ print centers
ctrs

plot(X(idx==1,1),X(idx==1,2),'r.','MarkerSize',14)
hold on
plot(X(idx==2,1),X(idx==2,2),'b.','MarkerSize',14)
hold on
plot(X(idx==3,1),X(idx==3,2),'g.','MarkerSize',14)
hold on
plot(X(idx==4,1),X(idx==4,2),'m.','MarkerSize',14)
hold on
plot(ctrs(:,1),ctrs(:,2),'kx',...
     'MarkerSize',12,'LineWidth',2)
plot(ctrs(:,1),ctrs(:,2),'ko',...
     'MarkerSize',12,'LineWidth',2)
legend('Cluster 1','Cluster 2','Cluster 3','Cluster 4','Centroids','Location','Best')
title('Geographically distributed targets normalized on interval(0,1)')
xlabel('x coordinate of the target')
ylabel('y coordinate of the target')