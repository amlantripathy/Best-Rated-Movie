from array import *
def task32():
 x=int(input('enter the no of films you want to choose from'))
 l=array('i',[])
 r=array('i',[])
 pro=[]
 smr=[]
 sm=[]
 c1=[]
 c2=[]
 c3=[]
 for i in range(x):
  y=int(input('input the length of the film serially'))
  l.append(y)
  z=int(input('input the ratings of the corresponding film'))
  r.append(z)
  pro.append(y*z)
  c1.append(y*z)
 print(pro)
 pro.sort()
 m=0
 a=pro[x-1]
 b=pro[x-2]
 if str(a) in str(b):
  for k in range(x):
   if str(a) in str(c1[k]):
    sm.append(k)
    c2.append(r[k])
    smr.append(r[k])
    m+=1
    c2.sort()
    if str(c2[m-1]) in str(c2[m-2]):
           for i in range(x):
            if str(c2[m-1]) in str(r[i]):
             print(str(i+1)+'is the best movie to watch')
             break
    else:
       for i in range(x):
        if str(c2[m-1]) in str(r[i]):
         print('with respect to all movies in this list'+str(i+1)+'is the best movie to watch')
         break
 else:
  for i in range(x):
   if str(a) in str(c1[i]):
    print('finally'+str(i+1)+'is the best movie to watch')

def task33():
  arr=[]
  x=int(input('enter the size of the array'))
  cost=0
  for i in range(x):
   y=int(input('enter the no serially'))
   arr.append(y)
   arr.sort()
  for i in range(x-1):  
       if arr[0] > arr[1]:
        arr[0]=arr[1]
        cost+=arr[0]
        arr.pop(1)
           
        
       else:
        cost+=arr[0]
        arr.pop(1)
        
  
  print(str(cost))
   
  
   
  

    
  

