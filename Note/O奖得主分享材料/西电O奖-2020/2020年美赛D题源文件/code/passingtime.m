clear,clc
time=xlsread('passingtime.xlsx');
t=[];t_s=[];
i=1;k=0;

%% Calculate the time of 50 passing ball
[m,n]=size(time);
while time(i,1)==1
    k=k+1;
    t(k)=time(i+49,2)-time(i,2);
    t_s(k,1)=time(i,2);t_s(k,2)=time(i+49,2);
    i=i+50;
    if time(i+49,1)~=1
        break
    end
end
% Judge the half part of the match
while time(i,1)==1
    i=i+1;
end
while time(i,1)==2
    k=k+1;
    t(k)=time(i+49,2)-time(i,2);
    t_s(k,1)=time(i,2);t_s(k,2)=time(i+49,2);
    i=i+50;
    if i+49>m 
        break
    end
end

%% Calculate the number of passing balls in 10 minutes of the overall match 
% [n,q]=size(time);
% t=10;
% i=1;p=[];k=0;
% while time(i,1)==1
%     if time(i,2)-time(1,2)>(k+1)*t*60
%         k=k+1;
%         if k==1
%             p(k)=i;
%         else
%             p(k)=i-sum(p);
%         end
%     end
%     i=i+1;
% end
% j=i;m=k;
% while time(i,1)==2
%     if time(i,2)-time(j,2)>(k-m+1)*60*t
%         k=k+1;
%         p(k)=i-sum(p);
%     end
%     i=i+1;
%     if i>n
%         break
%     end
% end