clear all;
clc;
%funzione per la creazione del dataset 
vDisponibile = [0.135, 0.155, 0.11, 0.0025, 0.12, 0.002, 0.01, 0.79, 0.18, 0.16];
mu = 0.1664 %gaussiana centrata sul valor medio 
R = [0.067, 0.044, 0.032, 0.06, 0.067, 0.024, 0.011, 0.056,0.054, 0.043];
dataSet = zeros(2,1000);
for i = 1:1000
    var = R(ceil(i/100));
    csi = mvnrnd(mu,var,10);
    
    for j = 1:10
        if(csi(j)< 0)
            csi(j) = -csi(j);
        end
        dataSet(1,floor((i)*10)+ j) = csi(j);
        dataSet(2,floor((i)*10)+ j) = 0;
        if(csi(j) > 0.65)
            randomN = int32(randi([0, 1]));
            dataSet(2,floor((i)*10)+ j) = randomN;
        end
     end
end
dataSet = dataSet(:,11:10010)';
filename = 'DataSet.xlsx';
writematrix(dataSet,filename);
