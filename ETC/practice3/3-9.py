
# coding: utf-8

# In[12]:


def sort_by_word_length(words):
    word_list = []
    sort_list = []
    for word in words:
        word_list.append((len(word), word))
    word_list.sort(reverse=True)
    for i in range(len(word_list)):
        sort_list.append(word_list[i][1])
    return(sort_list)


# In[13]:


colors = ['red','blue','green','brown','gray']
sort_by_word_length(colors)


# In[14]:


instruments = ['피아노','바이올린','첼로','기타', '드럼']
sort_by_word_length(instruments)

