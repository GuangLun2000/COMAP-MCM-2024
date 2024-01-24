clear,clc
w=zeros(11,11);
data=xlsread('MatchID1.xlsx');
[m,n]=size(data);

%% Calculate the number of passing balls between each player
for i=1:1:m
    w(data(i,1),data(i,2))=w(data(i,1),data(i,2))+data(i,3);
    w(data(i,2),data(i,1))=w(data(i,2),data(i,1))+data(i,3);
end
for i=1:1:11
    w(i,i)=0;
end
w
%% Calculate the Total Link
L=0;
for i=1:1:11
    for j=1:1:11
        L=L+w(i,j);
    end
end
L=L/2
%% Calculate the density of match
pho=2*L/(n*(n-1))
%% Calculate the topological distance
d=zeros(11,11)-1;
for i=1:1:11
    for j=1:1:11
        if w(i,j)~=0
            d(i,j)=1./w(i,j);
        end
    end
end
d
%% Calculate the matrix of distance
D=0;
for i=1:1:11
    for j=1:1:11
        if d(i,j)>D
            D=d(i,j);
        end
    end
end
D
%% Calculate the cluster coeffient of each player
Cw=zeros(11,1);
for i=1:1:11
    s=0;
    for j=1:1:11
        for k=1:1:11
            if i~=j && j~=k && i~=k
                Cw(i)=Cw(i)+w(i,j)*w(j,k)*w(i,k);
            end
            if i~=j && i~=k
                s=s+w(i,j)*w(i,k);
            end
        end
    end
   Cw(i)=Cw(i)/s;
end
Cw
%% Calculate the cluster coeffient 
C=0;
for i=1:1:11
    C=C+Cw(i);
end
C=C/11
