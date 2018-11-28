words =[]
with open('filtered_words.txt','r+',encoding='utf8') as f:
    for i in f.readlines():
        if i[-1]=='\n':
            i = i[:-1]
        words.append(i)
input_key = input('请输入词')
for i in words:
    input_key = input_key.replace(i,'**')
print(input_key)