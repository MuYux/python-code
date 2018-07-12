import random
def get_yzm():
    yzm=[]
    for i in range(0,200):
        yz=''
        for j in range(0,10):
            ji=random.randint(97,122)
            yz=yz+chr(ji)
        yzm.append(yz)
    return yzm
print(get_yzm())