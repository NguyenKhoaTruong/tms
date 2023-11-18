# num=20
# num1=10
# data=[]
# main=[]
# data_Test=[1,2,3,4,5,6,7,8,9,10]
# def fun_A():
#     test=[]
#     for i in range(num1):
#         test.append(i)
#     data.append(test)
        

# for i in range(num):
#     fun_A()
# print('check value main',data,len(data))

data=[
    [[1,2,3,4,5,6],[6,5,4,3,2,1],[11,22,33,44,55,66],[66,55,44,33,22,11]], [[1.2,2,3,4,5,6],[6.2,5,4,3,2,1],[11.2,22,33,44,55,66],[66.2,55,44,33,22,11]]
]
text=""
for item in data:
    tesx="<main>"
    for i,value in enumerate:
        num1=value[0]
        num2=value[1]
        tesx+=f"<div>{num1}</div>"
    text+=f"{tesx}</main>"
print(text)
# print(text)