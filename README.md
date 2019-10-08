# TeoriaCuanticaBasica

**Sistemas Clasicos Deterministicos:**
Muestra el estado de un sistema clasico, despues de ciertos clicks de tiempo.

**Sistema Probabilistco:**

Muestra la probabilidad de que un elemento se encuentre en algun estado del sistema, despues de determinados clicks de tiempo.

**Sistema Cuantico:**

Muestra la probabilidad de que una particula,foton,electron se encuentre en algun estado del sistema, despues de determinados clicks de tiempo.





# Pre-requisitos 📋
![GitHub Logo](https://www.python.org/static/img/python-logo@2x.png)

Para poder usar esta libreria es necesario tener instalado python, si no se tiene, la descarga e instalación es como sigue:
Primero descargamos el programa de la página oficial:

![GitHub Logo](https://www.wikihow.com/images_en/thumb/1/14/Install-Python-Step-1-Version-2.jpg/v4-760px-Install-Python-Step-1-Version-2.jpg)
![GitHub Logo](https://www.wikihow.com/images_en/thumb/4/45/Install-Python-Step-2-Version-2.jpg/v4-760px-Install-Python-Step-2-Version-2.jpg)

Cuando termine de descargar hay que proceder a instalarlo:

![GitHub Logo](https://www.wikihow.com/images_en/thumb/f/fb/Install-Python-Step-4-Version-2.jpg/v4-760px-Install-Python-Step-4-Version-2.jpg)

 # Instalación de Operaciones Con Vectores y Matrices 🔧
Primero: 
![myimage-alt-tag](https://scontent-bog1-1.xx.fbcdn.net/v/t1.15752-9/69874998_750459472059681_3913524228170711040_n.png?_nc_cat=109&_nc_oc=AQnAHS7ixOACxFw9VZIuFwoJKytHypC0c9lCVCRXGIho84rLNJiPg55F4K2wzo2JtM4&_nc_ht=scontent-bog1-1.xx&oh=a5c49974e0f359c923370686c6d86f6e&oe=5DC80CBF) 


Segundo:
 
![myimage-alt-tag](https://scontent-bog1-1.xx.fbcdn.net/v/t1.15752-9/70678769_2608600409202096_5609513835909087232_n.png?_nc_cat=101&_nc_oc=AQk5bpFi6zdMwJygs22sr6bhKf6P0KFDBJcOLnnaSZ9jYS3D6cWzyF1gNewZOjFT8VI&_nc_ht=scontent-bog1-1.xx&oh=e2d320ca92637cf344136875a2d80a61&oe=5E031292) 


Luego abrimos el IDLE de python
![myimage-alt-tag](https://scontent-bog1-1.xx.fbcdn.net/v/t1.15752-9/69689175_475682319649824_1117122535582859264_n.jpg?_nc_cat=109&_nc_oc=AQncBZgHUk5xJWCUqEApXR0Jd2E_1hWuW4OYr4XiwiEsvhj0uYlr9-O6NLlb4Zkrjjs&_nc_ht=scontent-bog1-1.xx&oh=cebd69f85b23f8abab07548473591ce2&oe=5E03C862) 


Buscamos el archivo y lo abrimos

![myimage-alt-tag](https://scontent-bog1-1.xx.fbcdn.net/v/t1.15752-9/70778647_472135196670206_3245147181413302272_n.png?_nc_cat=100&_nc_oc=AQnxgrcF3EZL88MTpAI2jwDLclRoa72WBttNAznDA6vnFR88UHvB2M_Z9St3VWkMFoQ&_nc_ht=scontent-bog1-1.xx&oh=c41b02ea85e3f01c83da8b696a565ec9&oe=5DF5DC77) 

y listo!.


# Uso 
Para poder usar esta libreria es necesario:
Si lo prefiere puede usar el codigo depruebas y modificar los valores a su necesidad, o puede importar las librerias a su  archivo creado o crear uno nuevo.

![myimage-alt-tag](https://scontent.fbog2-2.fna.fbcdn.net/v/t1.15752-9/71401851_1707362362728247_8866192136928755712_n.png?_nc_cat=104&_nc_oc=AQnHpdESvbgt-YHXoK6oIFEnzznj87EjTA2eoR6ITt30Z7oUdbAKptUBxJgJyfZOHzw&_nc_ht=scontent.fbog2-2.fna&oh=32bf12334222607895f0b99eb322ab5d&oe=5E2D3CF3) 


# Ejecutando las pruebas ⚙️
![myimage-alt-tag](https://scontent.fbog2-1.fna.fbcdn.net/v/t1.15752-9/72209269_405494757032656_6677285436324315136_n.png?_nc_cat=102&_nc_oc=AQnVwvVIiYBZMvdC36vzXQBbPOlU08I_gG8fUtb6hg1cKT28KXZxqWZFePFH30lPtKM&_nc_ht=scontent.fbog2-1.fna&oh=d7db3c9444cfd3bc255f93fd8541a848&oe=5E32CD46) 


![myimage-alt-tag](https://scontent.fbog2-3.fna.fbcdn.net/v/t1.15752-9/71701890_410168889646315_9105454847909429248_n.png?_nc_cat=111&_nc_oc=AQkvYinrQkJsb6tuEsK_HcIN8xvbKrUN-ZDq9yp8-KmtE_MGRNA7o32IXQAt2md7EBg&_nc_ht=scontent.fbog2-3.fna&oh=97ac30abd292aa080936b6249b527ec1&oe=5E2DEE06) 
# ...Expliacion:
**position**
Al simulador se le ingresa un un vector, el cual es el primer argumento de la funcion "position" y la posicion cuyo lugar es como segundo argumento de la funcion. La respuesta correcta a la consulta de: 
      "la probabilidad de estar en una posicion particular", se muestra antes de la llamada a la funcion.

     def test1(self):
         self.assertEqual(0.05263157894736842,

                          position([(-3,-1),
                                    (0,-2),
                                    (0,1),
                                    (2,0)],     2))
**transition**

Al simulador se le ingresa dos ket, siendo los dos argumentos de la funcion "transition" la respuesta correcta a la consulta de:  
"la probabilidad de transitar del primer vector al segundo", se muestra antes de la llamada a la funcion.
    
        def test2(self):
            self.assertEqual((0,-0.9999999999999998),

                             transition([(0,-1),
                                         (1,0)],    [(1,0),
                                                     (0,-1)]))

# Ejemplo1:

    def position(V,p):
        raiz=0

        for i in V:
            raiz+=(i[0]**2)+(i[1]**2)

        prob =((V[p][0]**2)+(V[p][1]**2))/raiz

        return prob

# Ejemplo2:

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
  





# Autor ✒️
Andres Felipe Cubillos Hurtado


