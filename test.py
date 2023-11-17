num=20
num1=10
data=[]
main=[]
data_Test=[1,2,3,4,5,6,7,8,9,10]
def fun_A():
    test=[]
    for i in range(num1):
        test.append(i)
    data.append(test)
        

for i in range(num):
    fun_A()
print('check value main',data,len(data))