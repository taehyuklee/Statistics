import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.stats import f, chi2

def Standardization(A):
    A[:] = (A[:]- np.mean(A[:]))/np.std(A[:], ddof=1)

#Sampling elements #N (elements of sample space)
N = 1
#Sampling numbers
M = 500

data = np.zeros([N, 5], dtype =np.float64)
sample_average = np.zeros([M, 5], dtype = np.float64)
dfn = 5  # 분자 자유도 f분포
dfd = 2  # 분모 자유도 f분포
df_chi2 = 5  # 자유도

for j in range (M):

    #sampling data from each pdf 
    for i in range (N):
        data[i,0] = np.random.uniform(low = 0, high = 1, size = None)
        #Random variable scope 0~1 - uniform
        data[i,1] = np.random.normal(loc=0.0, scale=0.1, size=None)
        #Random variable scope -inf ~ +inf Gaussian (central = 0, std = 1.0)
        data[i,2] = np.random.binomial(1, 0.5, size = None)
        #Random variable scope 0 or 1 Bernoulli distribution
        data[i,3] = f.rvs(dfn, dfd)
        #Random variable from f distribution
        data[i,4] = chi2.rvs(df_chi2)
        #Random variable scope 0 or 1 Bernoulli distribution
    
    #Ensemble average part
    mean_uniform_sample = np.mean(data[:,0])
    mean_normal_sample = np.mean(data[:,1])
    mean_bernoulli_sample = np.mean(data[:,2])
    mean_f_sample = np.mean(data[:,0])
    mean_chi2_sample = np.mean(data[:,1])
 
    #collection of ensemble average (sample_mean) each sampling
    sample_average[j,0] = mean_uniform_sample
    sample_average[j,1] = mean_normal_sample
    sample_average[j,2] = mean_bernoulli_sample
    sample_average[j,3] = mean_f_sample
    sample_average[j,4] = mean_chi2_sample

#Standardization of each sample_mean dataset
Standardization(sample_average[:,0])
Standardization(sample_average[:,1])
Standardization(sample_average[:,2])
Standardization(sample_average[:,3])
Standardization(sample_average[:,4])

#--- Plotting part ---#
#uniform distribution plot
plt.title('Uniform distribution')
count, bins, ignored = plt.hist(sample_average[:,0], range=(-5, 5), histtype='bar', orientation='vertical',color=('orange'), \
         bins=50, alpha=0.4, density=True, rwidth=0.8)
#reference (normal distribution)
mu=0; sigma =1.0
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), color='r')
plt.savefig('uniform histogram.png')
plt.show()

#Gaussian distribution plot
plt.title('Gaussian distribution')
plt.hist(sample_average[:,1], range=(-5, 5), histtype='bar', orientation='vertical',color=('blue'), \
         bins=50, alpha=0.4, density=True, rwidth=0.8)
#reference (normal distribution)
mu=0; sigma =1.0
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), color='r')
plt.savefig('gaussian histogram.png')
plt.show()

#Bernoulli distribution plot
plt.title('Bernoulli distribution')
plt.hist(sample_average[:,2], range=(-5, 5), histtype='bar', orientation='vertical',color=('green'), \
         bins=50, alpha=0.4, density=True, rwidth=0.8)
#reference (normal distribution)
mu=0; sigma =1.0
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), color='r')
plt.savefig('bernoulli histogram.png')
plt.show()

#Bernoulli distribution plot
plt.title('f distribution')
plt.hist(sample_average[:,3], range=(-5, 5), histtype='bar', orientation='vertical',color=('gray'), \
         bins=50, alpha=0.4, density=True, rwidth=0.8)
#reference (normal distribution)
mu=0; sigma =1.0
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), color='r')
plt.savefig('f histogram.png')
plt.show()

#Bernoulli distribution plot
plt.title('chi2 distribution')
plt.hist(sample_average[:,4], range=(-5, 5), histtype='bar', orientation='vertical',color=('red'), \
         bins=50, alpha=0.4, density=True, rwidth=0.8)
#reference (normal distribution)
mu=0; sigma =1.0
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), color='r')
plt.savefig('chi2 histogram.png')
plt.show()
