s = "I work in bloomberg founded by bloomberg work work"
tokens=  s.split(' ')
d= {} #making empty dictionary 
for token in tokens:
    if token in d:
        d[token]+=1 #if the word is repeated the count is increased
    else:
        d[token]=1 #entering the words in list token into the dictionary and seetting their initial count to 1
print(d)