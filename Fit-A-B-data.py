import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as opt

#import data to fit into a pandas dataframe
name=['A','B']
df=pd.read_csv("A-B",sep=" ",header=0, names=name)

#define an exponential function or any other function of your choice
def exponential(x,a,k,b):
    return  (a*np.exp(x*k) + b)
popt_exponential, pcov_exponential  = opt.curve_fit(exponential, df["A"],df["B"],p0=[1,-0.5,1])
#print the function to stdout
print (str(popt_exponential[0])+" * exp("+str(popt_exponential[1])+" * x) + "+str(popt_exponential[2]))

#save the predictions of the above fitted function and its derivative for A = 0 to 100 in a dataframe 
dfx=pd.DataFrame(columns=['A', 'B'])
for x in range(1,100):
    #print(x,exponential(x,popt_exponential[0],popt_exponential[1],popt_exponential[2]))
    dfx.loc[x,['A']] = x
    dfx.loc[x,['B']] = exponential(x,popt_exponential[0],popt_exponential[1],popt_exponential[2])
#print("derivatives")
dfy=pd.DataFrame(columns=['A', 'B'])
for x in range(1,100):
    #print(x,exponential(x,popt_exponential[0]*popt_exponential[1],popt_exponential[1],0))
    dfy.loc[x,['A']] = x
    dfy.loc[x,['B']] = exponential(x,popt_exponential[0]*popt_exponential[1],popt_exponential[1],0)

#plot the actual data, function and its derivative
plt.figure(figsize=(12,8))
plt.grid(1)
plt.xlabel("A",fontsize=20)
plt.ylabel("B",fontsize=20)
#plt.ylim(0,1)
#plt.xlim(0,1)
plt.scatter(df['A'],df['B'],edgecolors=(0,0,0),lw=1,s=40)
plt.plot(dfx['A'],dfx['B'],lw=2)
plt.plot(dfy['A'],dfy['B'],lw=2)
plt.show()
