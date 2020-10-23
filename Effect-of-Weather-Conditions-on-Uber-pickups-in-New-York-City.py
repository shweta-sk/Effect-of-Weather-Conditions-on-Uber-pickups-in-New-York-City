#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_csv('uber_nyc_enriched.csv')


# In[3]:


df['pickup_dt'] = pd.to_datetime(df.pickup_dt)


# In[4]:


df.pickup_dt.dt.weekday_name


# In[5]:


df.pickup_dt.dt.dayofyear


# In[6]:


#Data of 181 days in the population


# In[7]:


import datetime


# In[8]:


weekdaytest=df[df.pickup_dt.dt.weekday_name=='Tuesday']


# In[9]:


weekdaytest


# In[10]:


blanks=df.borough.replace(np.nan,'Long Island',regex=True)


# In[11]:


blanks


# In[12]:


df.borough=blanks


# In[13]:


df


# In[14]:


weekdayneed=df[df.pickup_dt.dt.weekday_name=='Tuesday']


# In[15]:


weekdayneed


# In[16]:


#weekdayneed is what we need for weekdays


# In[17]:


df.borough.value_counts()


# In[18]:


df.pickup_dt.dt.dayofweek


# In[19]:


jangroup=df[(df.pickup_dt.dt.date == '2015-01-01')]


# In[20]:


jantest=df[(df.pickup_dt.dt.month == 1) & (df.pickup_dt.dt.day.isin([1,10,13,22,])) & (df.pickup_dt.dt.hour.isin([8,9,10,18,19,20,1,2,3]))]


# In[21]:


from datetime import time


# In[22]:


jantest


# In[23]:


jantesting=jantest


# In[24]:


jantestings=jantesting[jantesting.borough != 'Long Island']


# In[25]:


jantestings


# In[26]:


jantestingss=jantestings[jantestings.borough != 'EWR']


# In[27]:


jantestingss


# In[28]:


jantestingss.borough.value_counts()


# In[29]:


jantestings.borough.value_counts()


# In[30]:


janbronx=jantestings[jantestings.borough == 'Bronx']


# In[31]:


janbronx.borough.value_counts()


# In[32]:


janqueens=jantestings[jantestings.borough == 'Queens']


# In[33]:


janstat=jantestings[jantestings.borough == 'Staten Island']


# In[34]:


janman=jantestings[jantestings.borough == 'Manhattan']


# In[35]:


janewr=jantestings[jantestings.borough == 'EWR']


# In[36]:


janbro=jantestings[jantestings.borough == 'Brooklyn']


# In[37]:


df=df[df.borough != 'Long Island']


# In[38]:


df.borough.value_counts()


# In[39]:


janbronx=janbronx[janbronx.pickup_dt.dt.hour != 10]


# In[40]:


janbronx.pickup_dt.dt.hour.value_counts()


# In[41]:


janbronx=janbronx[janbronx.pickup_dt.dt.hour != 20]


# In[42]:


janbronx=janbronx[janbronx.pickup_dt.dt.hour != 3]


# In[43]:


janqueens=janqueens[janqueens.pickup_dt.dt.hour != 10]


# In[44]:


janqueens=janqueens[janqueens.pickup_dt.dt.hour != 20]


# In[45]:


janqueens=janqueens[janqueens.pickup_dt.dt.hour != 3]


# In[46]:


janstat=janstat[janstat.pickup_dt.dt.hour != 10]


# In[47]:


janstat=janstat[janstat.pickup_dt.dt.hour != 20]


# In[48]:


janstat=janstat[janstat.pickup_dt.dt.hour != 3]


# In[49]:


janman=janman[janman.pickup_dt.dt.hour != 3]


# In[50]:


janman=janman[janman.pickup_dt.dt.hour != 10]


# In[51]:


janman=janman[janman.pickup_dt.dt.hour !=20]


# In[52]:


janewr=janewr[janewr.pickup_dt.dt.hour != 3]


# In[53]:


janewr=janewr[janewr.pickup_dt.dt.hour != 10]


# In[54]:


janewr=janewr[janewr.pickup_dt.dt.hour != 20]


# In[55]:


janbro=janbro[janbro.pickup_dt.dt.hour != 3]


# In[56]:


janbro=janbro[janbro.pickup_dt.dt.hour != 10]


# In[57]:


janbro=janbro[janbro.pickup_dt.dt.hour != 20]


# In[58]:


febtest=df[(df.pickup_dt.dt.month == 2) & (df.pickup_dt.dt.day.isin([10,15,16,19])) & (df.pickup_dt.dt.hour.isin([8,9,18,19,1,2]))]


# In[59]:


febtest


# In[60]:


febbronx=febtest[febtest.borough == 'Bronx']


# In[61]:


febqueens=febtest[febtest.borough == 'Queens']


# In[62]:


febstat=febtest[febtest.borough == 'Staten Island']


# In[63]:


febman=febtest[febtest.borough == 'Manhattan']


# In[64]:


febewr=febtest[febtest.borough == 'EWR']


# In[65]:


febbro=febtest[febtest.borough == 'Brooklyn']


# In[66]:


martest=df[(df.pickup_dt.dt.month == 3) & (df.pickup_dt.dt.day.isin([6,14,16,22])) & (df.pickup_dt.dt.hour.isin([8,9,18,19,1,2]))]


# In[67]:


marbronx=martest[martest.borough == 'Bronx']


# In[68]:


marqueens=martest[martest.borough == 'Queens']


# In[69]:


marstat=martest[martest.borough == 'Staten Island']


# In[70]:


marman=martest[martest.borough == 'Manhattan']


# In[71]:


marewr=martest[martest.borough == 'EWR']


# In[72]:


marbro=martest[martest.borough == 'Brooklyn']


# In[73]:


aprtest=df[(df.pickup_dt.dt.month == 4) & (df.pickup_dt.dt.day.isin([5,12,9,29])) & (df.pickup_dt.dt.hour.isin([8,9,18,19,1,2]))]


# In[74]:


aprbronx=aprtest[aprtest.borough == 'Bronx']


# In[75]:


aprqueens=aprtest[aprtest.borough == 'Queens']


# In[76]:


aprstat=aprtest[aprtest.borough == 'Staten Island']


# In[77]:


aprman=aprtest[aprtest.borough == 'Manhattan']


# In[78]:


aprewr=aprtest[aprtest.borough == 'EWR']


# In[79]:


aprbro=aprtest[aprtest.borough == 'Brooklyn']


# In[80]:


maytest=df[(df.pickup_dt.dt.month == 5) & (df.pickup_dt.dt.day.isin([5,14,23,25])) & (df.pickup_dt.dt.hour.isin([8,9,18,19,1,2]))]


# In[81]:


maybronx=maytest[maytest.borough == 'Bronx']


# In[82]:


mayqueens=maytest[maytest.borough == 'Queens']


# In[83]:


maystat=maytest[maytest.borough == 'Staten Island']


# In[84]:


mayman=maytest[maytest.borough == 'Manhattan']


# In[85]:


mayewr=maytest[maytest.borough == 'EWR']


# In[86]:


maybro=maytest[maytest.borough == 'Brooklyn']


# In[87]:


juntest=df[(df.pickup_dt.dt.month == 6) & (df.pickup_dt.dt.day.isin([3,11,28,30])) & (df.pickup_dt.dt.hour.isin([8,9,18,19,1,2]))]


# In[88]:


junbronx=juntest[juntest.borough == 'Bronx']


# In[89]:


junqueens=juntest[juntest.borough == 'Queens']


# In[90]:


junstat=juntest[juntest.borough == 'Staten Island']


# In[91]:


junman=juntest[juntest.borough == 'Manhattan']


# In[92]:


junewr=juntest[juntest.borough == 'EWR']


# In[93]:


junbro=juntest[juntest.borough == 'Brooklyn']


# In[94]:


bronxall=pd.concat([janbronx,febbronx,marbronx,aprbronx,maybronx,junbronx])


# In[95]:


bronxall


# In[96]:


queensall=pd.concat([janqueens,febqueens,marqueens,aprqueens,mayqueens,junqueens])


# In[97]:


statall=pd.concat([janstat,febstat,marstat,aprstat,maystat,junstat])


# In[98]:


manall=pd.concat([janman,febman,marman,aprman,mayman,junman])


# In[99]:


ewrall=pd.concat([janewr,febewr,marewr,aprewr,mayewr,junewr])


# In[100]:


broall=pd.concat([janbro,febbro,marbro,aprbro,maybro,junbro])


# In[101]:


#bronx.to_csv(r'Path where you want to store the exported CSV file\File Name.csv')


# In[102]:


allmallb=pd.concat([bronxall,queensall,statall,manall,ewrall,broall])


# In[103]:


allmallb


# In[105]:


bronxall.to_csv(r'C:\Desktop\bronxall.csv')


# In[106]:


queensall.to_csv(r'C:\Desktop\queensall.csv')


# In[107]:


statall.to_csv(r'C:\Desktop\statall.csv')


# In[108]:


manall.to_csv(r'C:\Desktop\manall.csv')


# In[109]:


ewrall.to_csv(r'C:\Desktop\ewrall.csv')


# In[110]:


broall.to_csv(r'C:\Desktop\broall.csv')


# In[111]:


jantestings.to_csv(r'C:\Desktop\jantestings.csv')


# In[112]:


febtest.to_csv(r'C:\Desktop\febtest.csv')


# In[113]:


martest.to_csv(r'C:\Desktop\martest.csv')


# In[114]:


aprtest.to_csv(r'C:\Desktop\aprtest.csv')


# In[115]:


maytest.to_csv(r'C:\Desktop\maytest.csv')


# In[116]:


juntest.to_csv(r'C:\Desktop\juntest.csv')


# In[117]:


import matplotlib.pyplot as plt


# In[118]:


ax = plt.gca()


# In[119]:


# print(bronxall)
allmallb = allmallb.sort_values(by=['temp'])

#All in one
ax = 'initial'
for key, grp in allmallb.groupby(['borough']):
    if ax != "initial":
        ax = grp.plot(x='temp', y='pickups', ax = ax, label = key)
    else:
        ax = grp.plot(x='temp', y='pickups', label = key)
        
#All seperate
# for key, grp in allmallb.groupby(['borough']):
#     grp.plot(x='temp', y='pickups',label = key)
    ax.set_ylabel("Number of Pickups")
    ax.set_xlabel("Temperature (in degrees fahrenheit)")    
        
# ax.set_ylabel("Temperature")
# ax.set_xlabel("Pickups")
# queensall.plot(kind='line', x='pickups', y='temp', ax=ax)
# broall.plot(kind='line', x='pickups', y='temp', ax=ax)
# statall.plot(kind='line', x='pickups', y='temp', ax=ax)
# manall.plot(kind='line', x='pickups', y='temp', ax=ax)
# ewrall.plot(kind='line', x='pickups', y='temp', ax=ax)


# In[120]:


plt.show()


# In[121]:


statall.pickups.value_counts()


# In[122]:


df


# In[123]:


allmallb=allmallb[allmallb.borough != 'EWR']


# In[124]:


allmallb.borough.value_counts()


# In[137]:


allmallb.to_csv(r'C:\Desktop\allmallb.csv')


# In[130]:


jantestings=jantestings[jantestings.borough != 'EWR']
jantestings.to_csv(r'C:\Desktop\jantest.csv')


# In[131]:


febtest=febtest[febtest.borough != 'EWR']
febtest.to_csv(r'C:\Desktop\febtest.csv')


# In[132]:


martest=martest[martest.borough != 'EWR']
martest.to_csv(r'C:\Desktop\martest.csv')


# In[133]:


aprtest=aprtest[aprtest.borough != 'EWR']
aprtest.to_csv(r'C:\Desktop\aprtest.csv')


# In[134]:


maytest=maytest[maytest.borough != 'EWR']
maytest.to_csv(r'C:\Desktop\maytest.csv')


# In[135]:


juntest=juntest[juntest.borough != 'EWR']
juntest.to_csv(r'C:\Desktop\juntest.csv')


# In[ ]:

