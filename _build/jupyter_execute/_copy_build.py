#!/usr/bin/env python
# coding: utf-8

# In[1]:


import shutil
import os


# In[2]:


source = r'_build'
source = r'_build/html'
destination = r'../Website_built/docs'


# In[3]:


shutil.rmtree(destination)


# In[4]:


shutil.copytree(source, destination)


# In[5]:


# Specify the file name
file = '.nojekyll'
# Creating a file at specified location
with open(os.path.join(destination, file), 'w') as fp:
    pass


# In[ ]:




