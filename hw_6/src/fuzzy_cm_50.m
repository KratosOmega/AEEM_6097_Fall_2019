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
options = [NaN 50 0.0001 0];
episode = 50;
X = [1.4 8.9; 1.6 8.1; 1.8 7.3; 1.9 8.3];
result = [];


for e = 1 : episode
    idx = [0;0;0;0]
    [centers, U, objFun] = fcm(X, 2, options);
    
    maxU = max(U);
    index1 = find(U(1,:) == maxU);
    index2 = find(U(2,:) == maxU);
    
    for i = 1 : length(index1)
        idx(index1(i)) = 1
    end
        
    for i = 1 : length(index2)
        idx(index2(i)) = 2
    end

    new = [centers(1,:) centers(2,:) idx(1) idx(2) idx(3) idx(4)];
    
    result = [result; new];    
end

sorted = sortrows(result,1)


