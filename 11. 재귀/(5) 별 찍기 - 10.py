# mapping = []
# def square (n : int):
#     global mapping
#     if (n==3):
#         print("***\n* *\n***\n")
#     for i in range(0,n):
#         for j in range(0,n):
#             if((n-2*n/3)<=i<(n-n/3) and (n-2*n/3)<=j<(n-n/3)):
#                 mapping[i].append(" ")
#             else:
#                 mapping[i].append("*") 
#     return mapping
# print(square(9))

# def mapping (n):
#     return [[' ']*n]*n
# def square (n):
#     if (n==3):
#         return [['*','*','*'],['*',' ','*'],['*','*','*']]
#     else:
#         map = mapping(n)
#         point = []
#         for i in range(0,3):
#             for j in range(0,3):
#                 point.append([0+(n/3)*i,0+(n/3)*j])
        
#         for i in range(0,8):
#             x= point[i][0]
#             y= point[i][1]

lst = [['0']*3]*3
print(lst[0:2][0:2])
lst[0:1][0:1] = [['1','1'],['1','1']]
print(lst)