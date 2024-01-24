import numpy as np
import pandas as pd

def writeTxt(result1, result2, fileName):
    f = open(fileName,'a')
    for ele in result1:
        f.write(str(ele)+' ')
    f.write(str(result2))
    f.write('\n')

def read_csv(filename):
    read_file = pd.read_csv(filename, header = None)
    read_file = np.array(read_file)
    return read_file
                            
def panduan(w,re,vec_one,vec_two,m):
    flag=1
    for i in range(m):
        if re[i]==1:
            y1=np.dot(vec_one[i],w)
            y2=np.dot(vec_two[i],w)
            if y1<y2:
                flag=0
                break
        elif re[i]==-1:
            y1=np.dot(vec_one[i],w)
            y2=np.dot(vec_two[i],w)
            if y1>y2:
                flag=0
                break
        else:
            y1=np.dot(vec_one[i],w)
            y2=np.dot(vec_two[i],w)
            if abs(y1-y2)>1:
                flag=0
                break
    return flag

def lowestError(w,vec_one,vec_two,m):
    y=[]
    for i in range(m):
        y1=np.dot(vec_one[i],w)
        y.append(y1)
    return np.var(y)
    

vec_one=read_csv('Huskies.csv')
vec_two=read_csv('Opponent.csv')
re=read_csv('result.csv')
fileName = "var_y.txt"
m=vec_one.shape[0]
k=0
for w1 in range(1,10):
        for w2 in range(1,10):
            for w3 in range(1,10):
                for w4 in range(1,10):
                    for w5 in range(1,10):
                        w=np.array([w1,w2,w3,w4,w5])*0.1
                        print(w)
                        if panduan(w,re,vec_one,vec_two,m):
                            s=lowestError(w,vec_one,vec_two,m)
                            k=k+1
                            writeTxt(w,s,fileName)
                        else:
                            w=[]

# for j in range(20):
#     for w1 in range(1,10):
#         for w2 in range(1,10):
#             for w3 in range(1,10):
#                 for w4 in range(1,10):
#                     for w5 in range(1,10):
#                         w=np.array([w1,w2,w3,w4,w5])*0.1
#                         print(w)
#                         if panduan(w,re,vec_one,vec_two,m,j):
#                             s=lowestError(w,vec_one,vec_two,m)
#                             k=k+1
#                             writeTxt(w,s,fileName)
#                         else:
#                             w=[]

print("sum of result:")
print(k)