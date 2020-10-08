size=int(input())
count=1
mtrx=[]

def mat_build(mtrx,size):
    if size%2==1:
        print(size)
    else:
        m1=[]
        m2=[]
        m3=[]
        m4=[]
        
        for i in range(0,int(size/2)):
            m1.append(mtrx[i][0:int(size/2)])
            m2.append(mtrx[i][int(size/2):size])
           
        for i in range(int(size/2),size):
            m3.append(mtrx[i][0:int(size/2)])
            m4.append(mtrx[i][int(size/2):size])
           
        if m1==trans(m2) and m2 == m3 and m1 == m4 :
            size=int(size/2)
            mtrx=m1
            mat_build(mtrx,size)
        else:
            print(int(size))
            return (int(size))
def trans(m):
    trans = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return trans

for i in range(size):
    line=input().split()
    line=list(map(int,line))
    mtrx.append(line)
#for i in range(len(mtrx)):
    #if mtrx[i]==mtrx[1]:
        #continue
    #else:
        #mat_build(mtrx,size)
        #break
#else:
    #print(count)

mat_build(mtrx,size)

    

    

