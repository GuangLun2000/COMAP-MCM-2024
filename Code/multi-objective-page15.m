% This is the Matlab calculation for the Multi-objective Optimization Model (Page 15/25).
% Designed by Wenxuan Luo and commented by Hanlin Cai (Team #2316192).
% Github Page: https://github.com/GuangLun2000/MCM-2316192/

clear;clc

a=input("Please input the value of coupling degree a: ");
aa=a/57.3;

c = -[0.58*aa,0.58*sin(aa),0.58*(1-cos(aa)),0.42*cos(aa),0.42*(1-aa),0.42*(1-sin(aa))]';

intcon = [1:6];

Aeq=[0 0 0 0 0 0]; 
beq=0;

A=[1,1,1,0,0,0;
   0,0,0,1,1,1;
   -1,-1,-1,0,0,0;
   0,0,0,-1,-1,-1;
   1 1 1 1 1 1 ;
   -1 -1 -1 -1 -1 -1;];

b=[3;3;-1;-1;4;-2];

lb=zeros(6,1); 
ub=ones(6,1);



% Finlly, call function intlinprog()

[x,fval] = intlinprog(c,intcon,A,b,Aeq,beq,lb,ub)
fval = -fval;
disp("favl+++++++++++++++++++++++")
disp(fval)