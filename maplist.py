a=[1,2,3,4,6]
b= [20,10,34,3,3,7]

c=list(map(lambda x:x*2,a))
print(c)

d=list(map(lambda x,y:(x-y)*2,b,a))
print(d)