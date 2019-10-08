from numeroscomplejos import *
from Operacionesconvectoresymatrices import *
def position(V,p):
    raiz=0
    
    for i in V:
        raiz+=(i[0]**2)+(i[1]**2)
        
    prob =((V[p][0]**2)+(V[p][1]**2))/raiz
    
    return prob

def transition(V1,V2):
    total=(0,0)
    norm1=0
    norm2=0
    for z,y in zip(V1,V2):
        total=suma(total,producto(z,y))
        norm1+=(z[0]**2)+(z[1]**2)
        norm2+=(y[0]**2)+(y[1]**2)
        
    norm1f=norm1**(1/2)
  
    norm2f=norm2**(1/2)
    
    
    deno=norm1f*norm2f
  

    return((total[0]/deno),(total[1]/deno))


def observable(X,Y):
    if hermitian(X)=="The matrix is hermitian":
        result =[[0 for x in range(len(Y[0]))] for y in range(len(Y))]
        for i in range(len(X)):
           
           for j in range(len(Y[0])):
               
               for k in range(len(Y)):
            
                   
                   result[i][j] += X[i][k] * Y[k][j]

        bra=conjugada(result)
        media=(0,0)
        for z,y in zip(bra,Y):
            media=suma(media,producto(z,y))
        return total2
    
        identidad=[[(total2[0],0) if j == i else (0,0) for j in range(len(X))] for i in range(len(X[0]))]
        sustra=[[resta(X[i][j],identidad[i][j]) for j in range(len(X[0]))] for i in range(len(identidad))]

        multi=[[0 for x in range(len(sustra[0]))] for y in range(len(sustra))]   
        for i in range(len(sustra)):
           
           for j in range(len(sustra[0])):
               
               for k in range(len(sustra)):
            
                   
                   multi[i][j] += sustra[i][k] * sustra[k][j]



def dynamic(X,V,n):
    Y=X
    result = [[0 for j in range(len(X))] for i in range(len(Y[0]))]
    ssum=(0,0)
    for t in range(n):
        for i in range(len(X)):
            
           for j in range(len(Y[0])):

               for k in range(len(Y)):
                   result[i][j] =suma(ssum,producto(X[i][k],Y[k][j]))
                   ssum=result[i][j]
               ssum =(0,0)
               
        Y=result
    
    result2 = [[0 for j in range(len(X))] for i in range(len(Y[0]))]
    ssum2=(0,0)
    for i in range(len(X)):
        
       for j in range(len(Y[0])):

           for k in range(len(Y)):
               result[i][j] =suma(ssum2,producto(X[i][k],Y[k][j]))
               ssum2=result[i][j]
           ssum2 =(0,0)
           
