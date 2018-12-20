
# coding: utf-8

# Il est suposer que la coque est un cylindre, d'un rayon de 16m avec un épaisseur de 1m

# In[22]:


import math
from decimal import Decimal


# In[29]:


p = 12304.586*1000
t=1
r=16
l =154


# In[30]:


sigmax = p*r/t


# In[31]:


sigmay=p*r/2*t


# In[32]:


print('sigmax: '+'%.3E' % Decimal(str(sigmax)))
print('sigmay: '+'%.3E' % Decimal(str(sigmay)))


# In[33]:


von_mises = (1/math.sqrt(2))*((((sigmax-sigmay)**2)+(sigmay**2)+(sigmax**2))**(1/2))
print('Von mises : '+'%.3E' % Decimal(str(von_mises)))


# In[34]:


materiaux = [['acier',200*10**9,0.25],['titane',113.8*10**9,0.342],['aluminum',68.9*10**9,0.33]]
for materiau in materiaux:
    delta_r = (von_mises/materiau[1])*r
    delta_l = delta_r*materiau[2]*l
    print('le déplacement radial du {} est de {} m et le déplacement longétudinal est de {} m'.format(materiau[0]
                                                                                                      ,delta_r,delta_l))
    

