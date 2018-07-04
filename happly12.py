
# coding: utf-8

# In[1]:


from requests_html import HTMLSession
import pandas as pd


# In[2]:


class Fish(object):
    def __init__(self, page_num):
        session = HTMLSession()
        self.page_num = page_num
        self.url = f'https://www.km28.com/gp_chart/zjklse/0/{self.page_num}.html'
        self.r = session.get(self.url)
    def get_valid(self, tr):
        try:
            if tr.attrs['id'].startswith('20') or tr.attrs['id']=='menuitem':
                return True
        except:
            return False
    def get_table(self):
        tr = self.r.html.find('#chartsTable',first=True).find('tr')
        tr_text = [_.text.split()[:6] for _ in tr if self.get_valid(_)]
        head = tr_text[0]
        head_text = [head[0]] + [head[1]+str(_) for _ in range(1,6)]
        df = pd.DataFrame(data=tr_text[1:], columns=head_text)
        return df


# In[3]:


foo = Fish(20)


# In[4]:


foo.get_table()

