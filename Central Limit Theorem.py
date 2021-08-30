#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

def Standardization(A):
    A[:] = (A[:]- np.mean(A[:]))/np.std(A[:])

#Random variable scope 0~1 - uniform
#Random variable scope -inf ~ +inf Gaussian (central = 0, std = 1.0)
#Random variable scope 0 or 1 Bernoulli distribution

#Sampling elements #N (elements of sample space)
N = 50
#Sampling numbers
M = 500

data = np.zeros([N, 3], dtype =np.float64)
sample_average = np.zeros([M,3], dtype = np.float64)

for j in range (M):

    #from each pdf sampling data
    for i in range (N):
        data[i,0] = np.random.uniform(low = 0, high = 1, size = None)
        data[i,1] = np.random.normal(loc=0.0, scale=1.0, size=None)
        data[i,2] = np.random.binomial(1, 0.5, size = None) #확률로 표기하도록 하였다.

    #check of data_array
    #print(data[:,0]) #form uniform data
    #print(data[:,1]) #from Gaussian data
    #print(data[:,2]) #from Bernoulli data
    
    #Ensemble average part
    mean_uniform_sample = np.mean(data[:,0])
    mean_normal_sample = np.mean(data[:,1])
    mean_bernoulli_sample = np.mean(data[:,2])
    
    #print(mean_uniform_sample) #form uniform data
    #print(mean_normal_sample) #from Gaussian data
    #print(mean_bernoulli_sample) #from Bernoulli data
    
    #collection of ensemble average (sample_mean) each sampling
    sample_average[j,0] = mean_uniform_sample
    sample_average[j,1] = mean_normal_sample
    sample_average[j,2] = mean_bernoulli_sample

#check of sample_mean (표본병균) distribution (M times)
#print(sample_average[:,0]) #form uniform data
#print(sample_average[:,1]) #from Gaussian data
#print(sample_average[:,2]) #from Bernoulli data

#Standardization of each sample_mean dataset
Standardization(sample_average[:,0])
Standardization(sample_average[:,1])
Standardization(sample_average[:,2])

#uniform distribution plot
plt.title('Uniform distribution')
plt.hist(sample_average[:,0], range=(-5, 5), histtype='bar', orientation='vertical',color=('orange'),          bins=50, alpha=0.4, density=False, rwidth=0.8)
plt.savefig('uniform histogram.png')
plt.show()

#Gaussian distribution plot
plt.title('Gaussian distribution')
plt.hist(sample_average[:,1], range=(-5, 5), histtype='bar', orientation='vertical',color=('blue'),          bins=50, alpha=0.4, density=False, rwidth=0.8)
plt.savefig('gaussian histogram.png')
plt.show()

#Bernoulli distribution plot
plt.title('Bernoulli distribution')
plt.hist(sample_average[:,2], range=(-5, 5), histtype='bar', orientation='vertical',color=('green'),          bins=50, alpha=0.4, density=False, rwidth=0.8)
plt.savefig('bernoulli histogram.png')
plt.show()

