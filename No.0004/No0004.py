with open('data.txt','r',encoding = 'utf8') as f:
    data = f.read()
    data = data.replace('\n',' ')
    print(data.split(' '))