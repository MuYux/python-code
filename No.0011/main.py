words =[]
with open('filtered_words.txt','r+',encoding='utf8') as f:
    for i in f.readlines():
        if i[-1]=='\n':
            i = i[:-1]
        words.append(i)
input_key = input('请输入词')
if input_key in words:
    print('Freedom')
else:
    print('Human Rights')