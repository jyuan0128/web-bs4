
# coding: utf-8

# In[1]:

import json


# In[19]:

file = open('get_json_5.json','r',encoding='utf8') #
data_dict = json.load(file) #
#data_str = json.dumps(data_dict) #



# In[23]:

for line in data:
   
    user = line['user']
    print(line['title'])  
    print(user['id'])
    line_str = json.dumps(line)
    #print(line['body'])
    
    


# In[ ]:




# In[ ]:



