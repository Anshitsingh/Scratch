
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import math 
from sklearn import datasets

d=pd.read_csv("/home/jash/Desktop/ASS1/winequality-red.csv",delimiter=';')
da=pd.DataFrame(d)
da.shape
x=da.iloc[:,:-1]
data=pd.DataFrame(x)
q=da.iloc[:,-1:]
target=pd.DataFrame(q)
i=(len(da))
x.loc[:]['b_values']=np.ones((i,1))
x.shape


# In[2]:


def train_test_split(data,target,train_fraction):
    x=math.ceil(train_fraction*len(target))
    train_data=pd.DataFrame(data.iloc[:x,:])
    train_target=pd.DataFrame(target.iloc[:x,:])
    test_data=pd.DataFrame(data.iloc[x:,:])
    test_target=pd.DataFrame(target.iloc[x:,:])
    return train_data,train_target,test_data,test_target
    


# In[3]:


train_data,train_target,test_data,test_target=train_test_split(data,target,.8)


# In[32]:


features=len(train_data.columns)
weights=np.ones((1,features))
weights.shape


# In[43]:


def stochastic_grad_descent_linear(data,target,weights,alpha,numiterations):
    m=len(target)
    
    for k in range(numiterations):
        f=weights.T
        predicted=(data.dot(f))
        diff=np.subtract(target,predicted)
        mse=np.sum((diff)**2)/(2*m)
        delta=1e-1
        
        
        
        if(mse>delta):
            for i in range(m):            
                for j in range(features):
                    gradient=(data.iloc[i][j])*(np.subtract(target.iloc[i],predicted.iloc[i]))/m
                    weights[0][j]=weights[0][j]+alpha*gradient
                gradient_b=(target.iloc[i]-predicted.iloc[i])/m
                weights[0][features]=weights[0][features]+alpha*gradient_b
                    
                predicted=(data.dot((weights).T))
                
                print(data.iloc[i][j])
                diff=np.subtract(target,predicted)
                mse=np.sum((diff)**2)/(2*m)
        alpha=alpha/2
        print(k)
        
        
        
     
    return weights


# In[44]:


def batch_gradient_descent_linear(data,target,weights,alpha,numiterations):
    m=len(target)
    
    for i in range(numiterations):
        predicted=(data.dot(np.transpose(weights)))
        
        diff=np.subtract(target,predicted)
        mse=np.sum((diff)**2)/(2*m)
        
        delta=1e-3
        if(mse>delta):
            x=np.subtract(target,predicted)
            gradient=np.sum((np.transpose(data)).dot(x))
            trans=np.transpose(weights)
            trans=trans-alpha*gradient/m
            weights=np.transpose(trans)
            predicted=(data.dot(np.transpose(weights)))
            diff=target-predicted
            mse=np.sum((diff)**2)/(2*m)
        
        alpha=alpha/2
        
            
    return weights


# In[45]:


def linear_regression_fit(data_train,target_train):
    data=data_train
    target=target_train
    
    x=len(data.columns)
    weights=np.ones((1,x))
    alpha=1
    numiterations=10
    m=weights.T
    predicted=(data_train.dot(m))
    
    
    weights=stochastic_grad_descent_linear(data,target,weights,alpha,numiterations)
    predicted=(data_train.dot(np.transpose(weights)))
    m=len(target)
    diff=np.subtract(target,predicted)
    mse=np.sum((diff)**2)/(2*m)
    return mse,weights



def linear_regression_predict(data_test,target_test,weights):
    predicted=(data_test.dot(np.transpose(weights)))
    diff=np.subtract(target_test,predicted)
    mse=np.sum((diff)**2)/(2*m)
    return predicted,mse

mse,weights=linear_regression_fit(train_data,train_target)

   
        

