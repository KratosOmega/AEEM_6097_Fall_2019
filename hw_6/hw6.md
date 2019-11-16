

## a - FCM

### i.

The coordinates of the two cluster centers:

centers =

    1.7919    7.3441
    1.6344    8.4553



### ii.

The membership grades for each of the data points 

membership grades =

    0.0894    0.1732    0.9985    0.0928
    0.9106    0.8268    0.0015    0.9072



### iii.

Plot the history of the objective function across the iterations 

![a_iii](/Users/xinli/Documents/_share/_fall_2019/AEEM7010_special_topics/_homework/AEEM_6097_Fall_2019/hw_6/a_iii.jpg)

### iv.

Plot the clusters including the cluster centers  

![a_iv](/Users/xinli/Documents/_share/_fall_2019/AEEM7010_special_topics/_homework/AEEM_6097_Fall_2019/hw_6/a_iv.jpg)

## b - K-MEANS

The centers are

ctrs =

    1.4000    8.9000
    1.7667    7.9000


![b](/Users/xinli/Documents/_share/_fall_2019/AEEM7010_special_topics/_homework/AEEM_6097_Fall_2019/hw_6/b.jpg)



## c

### 

|             | $C_{1}[\Delta_{y}]$ | $C_{1}[\sigma_{y}]$ | $C_{2}[\Delta_{y}]$ | $C_{2}[\sigma_{y}]$ | $m_{1}$ | $m_{2}$ | $m_{3}$ | $m_{4}$ |
| :---------: | :-----------------: | :-----------------: | :-----------------: | :-----------------: | :-----: | :-----: | :-----: | :-----: |
|  *fcm #1*   |       1.6342        |       8.4560        |       1.7919        |       7.3446        |    1    |    1    |    2    |    1    |
|  *fcm #2*   |       1.6344        |       8.4554        |       1.7919        |       7.3441        |    1    |    1    |    2    |    1    |
|  *fcm #3*   |       1.6346        |       8.4549        |       1.7920        |       7.3438        |    1    |    1    |    2    |    1    |
|  *fcm #4*   |       1.7919        |       7.3446        |       1.6342        |       8.4561        |    2    |    2    |    1    |    2    |
|  *fcm #5*   |       1.7920        |       7.3437        |       1.6346        |       8.4548        |    2    |    2    |    1    |    2    |
| *Kmeans #1* |       1.4000        |       8.9000        |       1.7667        |       7.9000        |    1    |    2    |    2    |    2    |
| *Kmeans #2* |       1.6333        |       8.4333        |       1.8000        |       7.3000        |    1    |    1    |    2    |    1    |
| *Kmeans #3* |       1.6500        |       8.6000        |       1.7000        |       7.7000        |    1    |    2    |    2    |    1    |
| *Kmeans #4* |       1.7000        |       7.7000        |       1.6500        |       8.6000        |    2    |    1    |    1    |    2    |
| *Kmeans #5* |       1.7667        |       7.9000        |       1.4000        |       8.9000        |    2    |    1    |    1    |    1    |



## d

### 

The most obvious observation is FCM is much more stable than KMEANS. Although we try to come up with 5 the most different cluster centers from both FCM and KMEANS, it is clear to see that FCM's cluster centers are very similar to each other. FCM#1, FCM#2, and FCM#3 are different from FCM#4 and FCM#5 base on the table, but actually the $C_{2}$ and $C_{1}$ of FCM #1, FCM#2, and FCM#3 is the same point as $C_{1}$ and $C_{2}$ of FCM#4 and FCM#5. This is because FCM and KMEANS are both unsupervised learning algorithms, so that there are no labels to be assigned, but only cluster to tell the difference. As a result, 5 the most different cluster centers of FCM are actually the same which approve its stableness.

On the other hand, KMEANS has shown that it have at least 3 different cluster centers combinations. Kmeans#1 and Kmeans#5 are actually the same for having 1222 (or 2111). Kmeans#3 and Kmeans#4 are actually the same for having 1221 (or 2112). Kmeans#2 is the third different cluster centers for having 1121. Thus, 5 the most different cluster centers of KMEANS show there are at least 3 different results.

As a result, this table shows that FCM seems to be able to provide must stabler cluster results than KMEANS.



## e

###

In the perspective of sensitivity of noise, FCM will definitely outperform KMEANS. This is due to the nature of being "fuzzy" for FCM. KMEANS takes all the Euclidean distances from the current data point to all other data points in the same cluster into account for determining the cluster center. This leads to a good prediction only if the cluster's noise level is relatively low. However, if the cluster has too much noises, or few but very significant noises, the cluster center prediction can be greatly affected.

On the other hand, instead using the idea of "to be or not to be", FCM assigns membership to each data point. As a result, each data point distributes its membership degrees according to different clusters. The noises will not affect the cluster centers as much as it did to KMEANS.

In conclusion, both algorithms can do well if the data points are well separated into clusters regardless of having stress and strain +/- 10%. This is because no noises are introduced since clusters are well separated. However, if the clusters are overlapping each other which is introducing noises to the clustering process, then FCM will outperform KMEANS for sure.



## f

### 

Attached m-file in same folder.