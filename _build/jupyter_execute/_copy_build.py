#!/usr/bin/env python
# coding: utf-8

# # Notebook "Script" to copy over the built notebooks

# In[1]:


import shutil
import os


# In[2]:


source = r'_build'
source = r'_build/html'
destination = r'../Website_built/docs'


# In[3]:


# delete old docs
shutil.rmtree(destination)


# In[4]:


# copy over html
shutil.copytree(source, destination)


# In[5]:


# Create that weird nojekyll file
file = '.nojekyll'
with open(os.path.join(destination, file), 'w') as fp:
    pass


# In[ ]:




