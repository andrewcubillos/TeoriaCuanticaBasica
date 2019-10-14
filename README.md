# TeoriaCuanticaBasica

**Estados Cuanticos**
Muestra la probabilidad de que una particula se encuentre en una posicion, y calcula la amplitud de transicion de un vector ket a otro.

**Observable**

Muestra la media y la varianza de un observable.

**Propios**

Muestra los valores y vectores propios de un vector y muestra la probabilidad de transicion de un vector a un vector propio.




# Pre-requisitos 📋
![GitHub Logo](https://www.python.org/static/img/python-logo@2x.png)

Para poder usar esta libreria es necesario tener instalado python, si no se tiene, la descarga e instalación es como sigue:
Primero descargamos el programa de la página oficial:

![GitHub Logo](https://www.wikihow.com/images_en/thumb/1/14/Install-Python-Step-1-Version-2.jpg/v4-760px-Install-Python-Step-1-Version-2.jpg)
![GitHub Logo](https://www.wikihow.com/images_en/thumb/4/45/Install-Python-Step-2-Version-2.jpg/v4-760px-Install-Python-Step-2-Version-2.jpg)

Cuando termine de descargar hay que proceder a instalarlo:

![GitHub Logo](https://www.wikihow.com/images_en/thumb/f/fb/Install-Python-Step-4-Version-2.jpg/v4-760px-Install-Python-Step-4-Version-2.jpg)

 # Instalación de Teoriacuanticabasica  🔧
Primero: 
![myimage-alt-tag](https://scontent-bog1-1.xx.fbcdn.net/v/t1.15752-9/69874998_750459472059681_3913524228170711040_n.png?_nc_cat=109&_nc_oc=AQnAHS7ixOACxFw9VZIuFwoJKytHypC0c9lCVCRXGIho84rLNJiPg55F4K2wzo2JtM4&_nc_ht=scontent-bog1-1.xx&oh=a5c49974e0f359c923370686c6d86f6e&oe=5DC80CBF) 


Segundo:
 
![myimage-alt-tag](https://scontent.fbog2-2.fna.fbcdn.net/v/t1.15752-9/73027169_1232838573555361_8251104875421630464_n.png?_nc_cat=103&_nc_oc=AQlGn5RRjS4RsqY5WRBAX4W2bGlpzGxTFLhZooh33KeMJ_jxbRe17jg6cyle5GBeMQM&_nc_ht=scontent.fbog2-2.fna&oh=cde8bb57580b271ee78405a2f25d9bbf&oe=5E2568B7) 


Luego abrimos el IDLE de python
![myimage-alt-tag](https://scontent-bog1-1.xx.fbcdn.net/v/t1.15752-9/69689175_475682319649824_1117122535582859264_n.jpg?_nc_cat=109&_nc_oc=AQncBZgHUk5xJWCUqEApXR0Jd2E_1hWuW4OYr4XiwiEsvhj0uYlr9-O6NLlb4Zkrjjs&_nc_ht=scontent-bog1-1.xx&oh=cebd69f85b23f8abab07548473591ce2&oe=5E03C862) 


Buscamos el archivo y lo abrimos

![myimage-alt-tag](https://scontent-bog1-1.xx.fbcdn.net/v/t1.15752-9/70778647_472135196670206_3245147181413302272_n.png?_nc_cat=100&_nc_oc=AQnxgrcF3EZL88MTpAI2jwDLclRoa72WBttNAznDA6vnFR88UHvB2M_Z9St3VWkMFoQ&_nc_ht=scontent-bog1-1.xx&oh=c41b02ea85e3f01c83da8b696a565ec9&oe=5DF5DC77) 

y listo!.


# Uso 
Para poder usar esta libreria es necesario:
Si lo prefiere puede usar el codigo depruebas y modificar los valores a su necesidad, o puede importar las librerias a su  archivo creado o crear uno nuevo.

![myimage-alt-tag](https://scontent.fbog2-3.fna.fbcdn.net/v/t1.15752-9/72169565_925751381140054_1140033531817230336_n.png?_nc_cat=109&_nc_oc=AQmp8FvKBqaEXI6P89Bb6PO0DPuvHLap73kyCKvcxEmRu1w-uBSfO9L3yKqJ_kFWbB8&_nc_ht=scontent.fbog2-3.fna&oh=2997503a42cfd6855c012a9ed2fcc4e8&oe=5E2BDE8B) 


# Ejecutando las pruebas ⚙️
![myimage-alt-tag](https://scontent.fbog2-1.fna.fbcdn.net/v/t1.15752-9/72301970_554213588668160_3379115990288695296_n.png?_nc_cat=106&_nc_oc=AQnICTcFSlZnph5skiM1vVl8PKn75bHipRwgzEs0qYMZdSjgIwwL1NAT_AHjqCuRB7M&_nc_ht=scontent.fbog2-1.fna&oh=103d9fa92019eeb5b5f9587b2c823cd0&oe=5E22FECD) 


![myimage-alt-tag](https://scontent.fbog2-1.fna.fbcdn.net/v/t1.15752-9/73101350_2487198311565634_5226267543240441856_n.png?_nc_cat=102&_nc_oc=AQmx_TDLC9RH_yX2h83ndAScBo7Mq6ijbafCpZ0R7E8Ma_ebAgKuOVXPktv7ajxbii4&_nc_ht=scontent.fbog2-1.fna&oh=4662ce68e1158c2dbb011aa8c37590f3&oe=5E2CCCF4) 

# ...Explicación:
**position_transition**
Usuario especifica el número de puntos posibles y un vector ket y el sistema calcula las probabilidades de encontrar partícula en una posición. El sistema puede recibir dos vectores y calcular la probabilidad de transitar de el uno al otro después de hacer la observación
La funcion tiene como primer argumento un vector ket, el segundo argumento es la posicion a averiguar y por ultimo el tercer argumento es vector ket.
Antes de la llamada a la funcion esta la respuesta correcta la cual es en primer lugar la posicion y en segundo la probabilidad o amplitud de transicion, con todo esto el sistema validara si todo esta en buen funcionamiento.


       def test1(self):
        self.assertEqual(0.05263157894736842   (0.36842105263157887, 0.31578947368421045),
                         Teoriacuanticabasica.position_transition([(-3,-1),
                                                (0,-2),
                                                (0,1),
                                                (2,0)],   2 ,[(-3,-1),
                                                               (0,-2),
                                                               (0,1),
                                                                (2,0)]))

**observable**
Una matriz  describe un observable y un vector ket, el sistema revisa que la matriz sea hermitiana, y si lo es, calcula la media y la varianza del observable en el estado dado.
La funcion recibe dos argumentos,el primero una matriz y el segundo un vector ket. Antes de la llamada a la funcion esta la respuesta correctael primer valor corresponde a la media y el segundo a la varianza, con todo esto el sistema validara si todo esta en buen funcionamiento.

        def test2(self):
        self.assertEqual(2.5,0.25,Teoriacuanticabasica.observable([[(1,0),(0,-1)],
                                  [(0,1),(2,0)]],[((2**(1/2))/2,0),
                                                     (0,(2**(1/2))/2)]))


**propios**
El sistema calcula los valores propios del observable y la probabilidad de que el sistema transite a alguno de los vectores propios después de la observación.
La funcion tiene dos argumentos los cuales son vectores ket.
Antes de la llamada a la funcion esta la respuesta correcta, la cual esta en el siguiente orden: valores propios,vectores propios y la probabilidad o amplitud de transicion a alguno de los vectores propios , con todo esto el sistema validara si todo esta en buen funcionamiento.


        def test3(self):
        self.assertEqual([[-1  ,1] [-1,  1]],[[[-0.70710678,  0.70710678]
                                                                            [ 0.70710678 , 0.70710678]]

                                                                            [[ 0,         1        ]
                                                                            [ 1,          0        ]]],(0,-0.9999999999999998)),
        Teoriacuanticabasica.propios([(0,-1),
                                     (1,0)],    [(1,0),
                                                   (0,-1)],)

**dynamic**
El simulador ahora considera la dinámica del sistema. Ahora con una serie de matrices Un el sistema calcula el estado final a partir de un estado inicial.
La funcion que hace esto recibe 3 argumentos, el primero una matriz,  el segundo un vectory el tercero la cantidad de clicks.
Antes de la llamada a la funcion esta la respuesta correcta la cual es un vector, con todo esto el sistema validara si todo esta en buen funcionamiento.

    #Sistema dinamico
    def test3(self):
        self.assertEqual([[0.0], 
                          [0.0], 
                          [0.0], 
                          [0.16666666666666666],
                          [0.16666666666666666],
                          [0.3333333333333333],
                          [0.16666666666666666],
                          [0.16666666666666666]],

         Teoriacuanticabasica.dynamic(     [[0, 0, 0, 0, 0, 0, 0, 0], 
                                            [0.5, 0, 0, 0, 0, 0, 0, 0], 
                                            [0.5, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0.3333333333333333, 0, 1, 0, 0, 0, 0],
                                            [0, 0.3333333333333333, 0, 0, 1, 0, 0, 0],
                                            [0, 0.3333333333333333, 0.3333333333333333, 0, 0, 1, 0, 0],
                                            [0, 0, 0.3333333333333333, 0, 0, 0, 1, 0],
                                            [0, 0, 0.3333333333333333, 0, 0, 0, 0, 1]],

                                            [[1],[0],[0],[0],[0],[0],[0],[0]],       2))
# Ejemplo1:

    def position_transition(V,p,V2):
        raiz=0

        for i in V:
            raiz+=(i[0]**2)+(i[1]**2)

        prob =((V[p][0]**2)+(V[p][1]**2))/raiz


        total=(0,0)
        norm1=0
        norm2=0
        V1=V
        for z,y in zip(V1,V2):
            total=suma(total,producto(z,y))
            norm1+=(z[0]**2)+(z[1]**2)
            norm2+=(y[0]**2)+(y[1]**2)

        norm1f=norm1**(1/2)

        norm2f=norm2**(1/2)


        deno=norm1f*norm2f


        return (prob," ",((total[0]/deno),(total[1]/deno)))

# Ejemplo2:

    def propios(X,V):
        a = np.array(X)
        w, v = LA.eigh(a)
        prop=v[0]
        total = (0, 0)
        norm1 = 0
        norm2 = 0
        V1 = V
        for z, y in zip(V1, prop):
            total = suma(total, producto(z, y))
            norm1 += (z[0] ** 2) + (z[1] ** 2)
            norm2 += (y[0] ** 2) + (y[1] ** 2)

        norm1f = norm1 ** (1 / 2)

        norm2f = norm2 ** (1 / 2)

        deno = norm1f * norm2f
        return(w,,v,(total[0] / deno), (total[1] / deno))
  





# Autor ✒️
Andres Felipe Cubillos Hurtado


