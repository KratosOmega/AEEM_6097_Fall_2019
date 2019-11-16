% ###################################################################
% ####                                                            ###
% ####       AEEM 6096: Spring 2015 - Kmeans                      ###
% ####                   Kelly_Kmeans.m                           ###
% ####                                                            ###
% ###################################################################

clc
clf 
clear all

K=2; % Number of clusters
episode = 50;
X = [1.4 8.9; 1.6 8.1; 1.8 7.3; 1.9 8.3];
result = [];


for e = 1 : episode
    [idx, ctrs, SUMD, D] = kmeans(X,K);

    new = [ctrs(1,:) ctrs(2,:) idx(1) idx(2) idx(3) idx(4)];
    
    result = [result; new];    
end

sorted = sortrows(result,1)