book={}
book['tom']={
    'name':'tom',
    'address':'vdfadf',
    'phone': 123444
}
book['bob']={
    'name':'bob',
    'address':'1 green street, NY',
    'phone': 234232
}
import json
s = json.dumps(book)
with open('D:\data science practice\python\hook.txt', 'w')as f:
    f.write(s)
