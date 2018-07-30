# def biggie():
#     t=[-1,3,5,-5]
#     for x in range(0,len(t)):
#         if t[x]>0:
#             t[x]="big"
#     return t
# print(biggie())

# def countpositive(e):
#     count=0
#     for x in range(0,len(e)):
#         if e[x]>0:
#             count+=1
#     e[len(e)-1]=count
#     return e
# e=[-1,1,1,1,1,1]
# print(countpositive(e))

# def sumtotal(a):
#     return sum(a)

# a=[1,5,452,3,234,2,2]

# print(sumtotal(a))

# def avg(a):
#     z=sum(a)
#     y=z/len(a)
#     return y
# a=[1,2,3,4,5,6,7,8,9]

# print(avg(a))

# def cool(c):
#     print(len(c))

# a=[1,2,3,51,3,34,3]

# cool(a)

# def min():
#     a=[10,3,5,2,4,4,4]
#     kek=a[0]
#     for y in a:
#         if y<kek:
#             kek=y
#     return kek

# print(min())

# def min():
#     a=[10,3,5,12,4,4,4]
#     kek=a[0]
#     for y in a:
#         if y>kek:
#             kek=y
#     return kek

# print(min())

# def no(b):
#     total=sum(b)
#     avg=total/len(b)
#     min=b[0]
#     max=b[0]
#     length=len(b)
#     for a in b:
#         if a > max:
#             max=a
#     for a in b:
#         if a < min:
#             min=a
#     c=[total,avg,min,max,length]
#     return c
# print(no([1,2,3,4,5,3,2,4,3,6,1,10,299]))

def back(y):
    for x in range(0,len(y)//2):
        temp = y[x]
        y[x]=y[len(y)-1-x]
        y[len(y)-1-x]=temp
    return y

z=[1,2,3,4,5,6,7,8,9]
print(back(z))
