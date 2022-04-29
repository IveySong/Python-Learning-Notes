# coding = utf-8

import re

p=r'\w+@zhijiketang\.com'
email1='tong_guan588@zhijiketang.com'
m=re.match(p,email1)

type(m)
m

m=re.search(p,email1)
m


# 字符串查找
p=r'Java|java|JAVA'
text='I like Java and java and JAVA'
match_list=re.findall(p,text)
match_list


# ch11.3.3 字符串替换
import re
p=r'\d+'
text='AB12CD34EF'
replace_text=re.sub(p,' ',text)
replace_text
replace_text=re.sub(p,' ',text,1)
replace_text
replace_text=re.sub(p,' ',text,2)
replace_text


# ch11.3.4 字符串分割
import re
p=r'\d+'
text='AB12CD34EF'
clist=re.split(p,text)
clist
clist=re.split(p,text,1)
clist
clist=re.split(p,text,2)
clist









