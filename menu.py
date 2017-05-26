from tkinter import *
import random 
import time
from math import *
#Despues de importar la libreria y otros modulos para el mejoramiento del funcionamiento del juego, lo primero que se hace es crear la ventana y darle las
#caracteristicas segun lo que se desee, en mi caso le di las dimensiones que son y le puse un titulo, el cual lleva el nombre del videojuego.
ventana= Tk()
ventana.geometry("1800x1800")
ventana.title("ROCKET FIGHT")
guardado = open("guardado.txt","r+")
#Por consiguiente importé  una imagen y la estalecí de fondo en mi menu, de la siguiente forma:Primero importo la imagen asegurandome que se encuentre en la misma
#carpeta donde se encuentra el archivo de python, despues creo una etiqueta y establezco esa imagen en la ventana antes creada.
fondo=PhotoImage(file="nuevo4.png")
etiqueta= Label(ventana, image=fondo).place(x=0,y=0)


#En esta seccion importo toda las imagenes que seran utilizadas en el primer nivel, como los son los mapas, los jugadores, enemigos, el combustible, y los obstaculos
#del juego, siempre y cuando se tenga en cuenta que las imagenes importadas deben estar en la misma carpeta donde se encuentra el archivo de python asi:

#En esta parte estan las imagenes de los mapas y la imagen de la parte de la mitad donde lleva los datos y el estado de los jugadores
mapa1=PhotoImage(file="nivelunico2.png")
mapa2=PhotoImage(file="nivelunico2.png")
mapaMedio=PhotoImage(file="medio.png")

#En esta parte estan las imagenes de los jugadores
jug1=PhotoImage(file="jugador1.png")
jug2=PhotoImage(file="jugador2.png")

#En esta parte se encuentran las imagenes de los enemigos que tendrán ambos jugadores
enem1=PhotoImage(file="enemigo1.png")
enem11=PhotoImage(file="enemigo1.png")


enem2=PhotoImage(file="enemigo2.png")
enem22= PhotoImage(file="enemigo2.png")

enem3=PhotoImage(file="enemigo3.png")
enem33=PhotoImage(file="enemigo3.png")

#En esta parte se encuentran las imagenes de los combustibles a los podrán acceder los jugadores
combu1=PhotoImage(file="combustible.png")
combu2=PhotoImage(file="combustible.png")

Pelo=PhotoImage(file="pelo.png")
Pelo2=PhotoImage(file="pelo.png")



#En esta seccion primero se crea la ventana que se desplegará al momento de oprimir en el menu nivel uno, para ello se utiliza el comando Toplevel, así mismo tambien
#se le da las caracteristicas segun como se desee, por ello le di el titulo nivel uno y tambien le di las dimensiones.
ventana2 = Toplevel()
ventana2.title("NIVEL 1")
ventana2.geometry("1800x1800")

#Despues se utiliza un comando, se llama canvas, funciona como un lienzo donde podre dibujar y poneer lo que desee, para ello se necesita la combinacion correcta
#de los demas comandos, pero siempre sobre este, ademas tambien se especifica las dimensiones que tendrá.
pantalla_1 = Canvas(ventana2, width=1800,height=1800)


#En esta parte se definen una variables que serán utilizadas mas adelante en una funcion, entre ellas hay unas que son especiales porque tienen una asignacion que
#se llama (StringVar()) la cual permite la visibilidad del valor que contenga en la ventana que se desee

combustible=1000
combustible2=1000
posCohe1=1125
posCohe2=275

#Esta es una de las variables que contiene la asignacion que permite la visibilidad en este caso se utilizará para el contador del combustible
Tvar=StringVar()
Tvar2=StringVar()

#En este caso estan las variables que tambien contienen la asignacion especial que permite la visibiladad de los nombres de los jugadores para ello es necesario despues
# de definir la variable de los jugadores, la variable que hace posible la existencia de la caja, donde se la enlaza con la variable anterior para que cada vez que
#ingrese un nombre este se guarde en la variable de visibilidad y se pueda exponer en el juego. Tambien ahi mismo en las cajas de los nombres se le da las
#caracteristicas que se  desean

velocidad = StringVar()

StringJugador1= StringVar()
cajaJugador1= Entry(ventana, textvariable= StringJugador1).place(x=390,y=200)

StringJugador2= StringVar()
cajaJugador2= Entry(ventana, textvariable=StringJugador2).place(x=730,y=200)

velocidad2= StringVar()


#Esta funcion fue creada con la funcion de poderla utilizar las veces que sea necesaria mas abajo para las distintas colisiones
def colision(cohete,enemigo):
        a=pantalla_1.coords(cohete)[0]>=pantalla_1.coords(enemigo)[0]

        #respecto al ejex en las posiciones del jugador2 en que sea menor a las posiciones del  enemigo1 mas 103
        b=pantalla_1.coords(cohete)[0]<=pantalla_1.coords(enemigo)[0]+103

        #respecto al ejex en las posiciones del jugador2 mas 103 en que sea menor a las posiciones del enemigo1
        c=pantalla_1.coords(cohete)[0]+103>=pantalla_1.coords(enemigo)[0]

        #respecto al ejey en las posiciones del jugador2 en que sea mayor a las posiciones del enemigo1 
        d=pantalla_1.coords(cohete)[1]>=pantalla_1.coords(enemigo)[1]

        #respecto al ejey en las posiciones del jugador2 en que sea menor a las posiciones del enemigo1 mas 114
        e=pantalla_1.coords(cohete)[1]<=pantalla_1.coords(enemigo)[1]+114

        #respecto al ejey en las posiciones del jugador2 mas 114 en que sea menor a las posiciones del enemigo1
        f=pantalla_1.coords(cohete)[1]<=pantalla_1.coords(enemigo)[1]+114
        return (a and b and d and e ) or (c and b and d and e)

#En esta parte se define una funcion que permite que el jugador que gane se deslise en la llegada, esta funcion sera utilizada para ambos cohetes por ello no se
#especifica el cohete que se quiere
def gano(cohete):
    pantalla_1.move(cohete,0,-.1)
    pantalla_1.after(1,gano,cohete)

#funcion utilizada para hacer el guardado de los elementos del juego
vel=0
distancia=0
vel2=0
distancia2=0
def cargar():
        global distancia,vel,posCohe2, vel2, distancia2, posCohe1
        m=[]
        for i in range(10):
                C=guardado.readline()
                C.split()
                m.append(C)
                
                
        
        combustible= int((m[0]))
        vel=int((m[2]))
        distancia=int((m[1]))
        posCohe2=int((m[3]))

        combustible2= int((m[4]))
        vel2=int((m[5]))
        distancia2=int((m[6]))
        posCohe1=int((m[7]))


#En esta parte se crea una funcion llamada primero, la cual tiene como variables globales las descritas a continuacion con el fin de poderle dar el uso correspondiente,
# en donde se hace lo siguiente:       
def primero():
    global primerNivel, pantalla_1, posCohe1, posCohe2,distancia,vel, cohete1, cohete2,combustible,Tvar2,Tvar,StringJugador1, StringJugador2,enemigo1,enemigo2,enemigo3,combustible2, distancia2, vel2
    
    
    #Despues de definir las variables globales se hace:

    #Primero se crean las variables que harán posible la creacion del  los mapas del primer nivel y su imagen que va en la mitad (la cual contiene el estado que llevan
    # los jugadores durante el juego) dentro del canvas anteriormente creado
   
    imgset= pantalla_1.create_image(250,300, image= mapa1)
    imgset1= pantalla_1.create_image(1110,300, image= mapa2)
    imgset2= pantalla_1.create_image(680,365, image= mapaMedio)
    
    #En esta parte se crean los jugadores dentro del canvas y se les da las posiciones correspondientes
    cohete1=pantalla_1.create_image(posCohe1,650,image=jug1)
    cohete2=pantalla_1.create_image(posCohe2,650,image=jug2)
    
    pelito=pantalla_1.create_image(200,-30,image=Pelo)
    pelito2=pantalla_1.create_image(1200,-30,image=Pelo2)
    
    #En esta parte se crean las imagen de los enemigos que tendran ambos jugadores dentro del canvas, pero esta vez la posicion que se les da es utilizando el modulo
    # que en un principio se importó llamado random, el cual da un valor aleatorio segun el rango que se establezca

    enemigo1=pantalla_1.create_image(random.randrange(143,395),-30,image=enem1)
    enemigo11=pantalla_1.create_image(random.randrange(1000,1300),-30,image=enem11)
    
    enemigo2=pantalla_1.create_image(random.randrange(143,395),-30,image=enem2)
    enemigo22=pantalla_1.create_image(random.randrange(1000,1300),-30, image=enem22)
                                                                                                
    enemigo3=pantalla_1.create_image(random.randrange(143,395),-30,image=enem3)
    enemigo33= pantalla_1.create_image(random.randrange(1000,1300),-30, image=enem33)

    combustible1=pantalla_1.create_image(random.randrange(143,395),-39,image=combu1)
    combustible22=pantalla_1.create_image(random.randrange(1000,1300),-39,image=combu2)
    cargar()# Se llama la funcion para el guardado
    #En esta parte lo que se hace es que con la ayuda de las variables que antes de la funcion fueron definidas, las cuales tenian las asignacion especial (StringVar())
    # se crea una etiqueta que las contengan para que se pueda hacer visible en el nivel uno, ademas tambien se definen las posiciones que se desean

    #Estas son las etiquetas del combustible
    labelCombustible=Label(ventana2,textvariable=Tvar, bg="red").place(x=740,y=540)
    labelCombustible2=Label(ventana2,textvariable=Tvar2, bg="red").place(x=540,y=540)
    #Estas son las etiquetas para la velocidad
    LabelVelocidad=Label(ventana2,textvariable=velocidad,bg="red").place(x=640,y=600)
    LabelVelocidad2=Label(ventana2,textvariable=velocidad2,bg="red").place(x=640,y=300)
    #Estas son las etiquetas de los nombres de los jugadores
    labelJujador1=Label(ventana2, textvariable=StringJugador1, bg="red").place(x=740,y=100)
    labelJujador2=Label(ventana2,textvariable=StringJugador2, bg="red").place(x=740,y=480)
    
    #Se utiliza para hacer visible lo que se haya hecho en la ventana
    pantalla_1.pack()



#se definen unas variables que seran de utilidad en el ciclo que se creará a continuacion.

    m=1
    i=0
    l=1
    velfondo=[5,0.5]
    velfondo2=[5,0.5]
    x=0
    M=0
    N=0
    k=0
    L=0
    V=0
    #Se crea un ciclo infinito y despues se crean unas variables globales que se utilizaran durante el ciclo
    while True:                             
        global Jugador2,combu

        #En esta parte lo que se hace es crear una variable que contenga una lita de las coordenadas que puede tomar los enemigos y los jugadores, para ello se
        #pone primero el nombre del canvas seguido de la palabra (coords) que hace posible la creacion de la lista

        #En esta parte se encuentran las variables que contienen la lista de las posiciones de los enemigos para ambos jugadores
        coordsEnemy1 = pantalla_1.coords(enemigo1)
        coordsEnemy11 = pantalla_1.coords(enemigo11)
        
        coordsEnemy2 = pantalla_1.coords(enemigo2)
        coordsEnemy22= pantalla_1.coords(enemigo22)
        
        coordsEnemy3= pantalla_1.coords(enemigo3)
        coordsEnemy33= pantalla_1.coords(enemigo33)

        #En esta parte se encuentran las variables que contienen la lista de las pocisiones de los jugadores
        coordsJugador2= pantalla_1.coords(cohete2)
        coordsJugador1= pantalla_1.coords(cohete1)
        
        #En esta parte se encuentra la variable que contiene la lista de las posiciones del combustible
        coordsCombustible1= pantalla_1.coords(combustible1)
        coordsCombustible2= pantalla_1.coords(combustible22)



        #Este condicional anidado es utilizado para que cuando el jugador llegue a la meta se deslice hacia arriba, por ello se dice que mientras la distancia sea
        #mayor a un valor preestablecido entonces se llame a la funcion gano que es la engarda del deslizamiento y por ultimo se establece que cuando su posicion
        #respecto a y sea menor a 0 se termine todo
        distancia+=int(vel/10)
        if(distancia>=200000):
            gano(cohete2)
            if(pantalla_1.coords(cohete2)[1]<0):
                break
        
        distancia2+=int(vel2/10)
        if(distancia2>=200000):
            gano(cohete1)
            if(pantalla_1.coords(cohete1)[1]<0):
                break
        
        #En esta parte se define como va disminuyendo el combustible y como este vuelve a regresar para salir de la parte superior con el fin de su aparecimiento
        #nuevamente, por ello primero se define una variable llamada combustible que determine que disminuye cierta cantidad, despues se crea un condicional que
        #establezca que si las coordenadas del combustible son mayores a 700 vuelva a parecer desde la parte superior
        
        combustible=combustible-0.1
        combustible2=combustible2-0.1
        if(coordsCombustible1[1]>700):
            pantalla_1.move(combustible1,0,-2000)

        #combustible2=combustible2-0.1
        if(coordsCombustible2[1]>700):
                pantalla_1.move(combustible22,0,-2000)
        
        Tvar2.set(round(combustible2)) 
        Tvar.set(round(combustible))#En esta parte redondeo el valor de combustible para que no vaya a quedar en decimales
        
        #Se establece el limite de velocidad para determinar el tiempo que durara el videojuego y para que apartir de este dato se establezca la velocidad    
        if(vel<1500):
            vel+=1
            
        if(vel2<1500):
            vel2+=1
        
        #Este condicional indica que en el momento en que el jugador se quede sin gasolina entonces no podra terminar el juego porque todo se para.
        if(combustible<=0):
            break
        if(combustible2<=0):
            break
        #En el mismo label de velocidad decidi añadir la distancia ademas gracias al comando set que permite la asignacion deseada
        velocidad.set(str(vel)+" km/h  "+str(distancia))
        velocidad2.set(str(vel2)+ "km/h "+ str(distancia2))
        
        #En esta parte se llama a la funcion para darle el movimiento a los cohetes
        movCohetes()

        #En esta parte se le da movimiento a los mapas y otros elementos que hacen parte del nivel
        pantalla_1.move(imgset,0,velfondo[x])#mapa1
        if(pantalla_1.coords(imgset)[1]>3000):
            pantalla_1.move(imgset,0,-3000)
        pantalla_1.update_idletasks()

        pantalla_1.move(imgset1,0,velfondo2[k])#mapa2
        if(pantalla_1.coords(imgset1)[1]>3000):
            pantalla_1.move(imgset1,0,-3000)
        pantalla_1.update_idletasks()
        
       
                                                       
        pantalla_1.move(pelito,0,1)
        pantalla_1.move(pelito2,0,1)
        pantalla_1.move(combustible1,0,2)
        pantalla_1.move(combustible22,0,2)
        pantalla_1.move(enemigo1,0,3)#enemigo1
        pantalla_1.move(enemigo11,0,3)#enemigo11

        
        
        #ENEMIGO2
        #En esta parte lo que se hace es establacer una variable que va a tomar un valor aleatorio segun el rango que se ha establecido.

        xx= random.randrange(800, 10000)

        #Este condicional establece que si ejex la posicion del enemigo es menor a 135 se mueva hacia la derecha un poquito y el m que estaba definida fuera del ciclo
        #se multiplicará por -1 
        if(coordsEnemy2[0]<135 ):
            pantalla_1.move(enemigo2,20,0)
            m*=-1

        #Este condicional establece que si en ejex la posicion del enemigo es mayor a 395 se mueva hacia la  izquierda  un poquito y la variable m se multiplique por
        #-1
        elif coordsEnemy2[0]>395:
            pantalla_1.move(enemigo2,-20,0)
            m*=-1

        #De lo contrario se mueva el enemigo en x tal como lo indique la variable m
        else:
            pantalla_1.move(enemigo2,m,2)

        #Por ultimo establece que si la posicion del enemigo en y es mayor a 800 entonces el enemigo se mueva en y tal como lo indique la variable xx hacia arriba
        if (coordsEnemy2[1]>800):
            pantalla_1.move(enemigo2,0,-xx)

        

        #ENEMIGO 22
        #En esta parte lo que se hace es establacer una variable que va a tomar un valor aleatorio segun el rango que se ha establecido.
        yy= random.randrange(800,10000)

        #Este condicional establece que si ejex la posicion del enemigo es menor a 1005 se mueva hacia la derecha un poquito y el l que estaba definida fuera del ciclo
        #se multiplicará por -1 
        if (coordsEnemy22[0]<1005):
            pantalla_1.move(enemigo22,20,0)
            l*=-1

        #Este condicional establece que si en ejex la posicion del enemigo es mayor a 1255 se mueva hacia la  izquierda  un poquito y la variable l se multiplique por
        #-1
        elif (coordsEnemy22[0]>1255):
            pantalla_1.move(enemigo22,-20,0)
            l*=-1

        #De lo contrario se mueva el enemigo en x tal como lo indique la variable l
        else:
            pantalla_1.move(enemigo22,l,2)

        #Por ultimo establece que si la posicion del enemigo en y es mayor a 800 entonces el enemigo se mueva en y tal como lo indique la variable yy hacia arriba
        if (coordsEnemy2[1]>800):    
            pantalla_1.move(enemigo22,0,-yy)
       
        pantalla_1.update_idletasks()
        ventana2.update()
        pantalla_1.update()
        if(pantalla_1.coords(pelito2)[1]>800):
                pantalla_1.move(pelito2,0,-800)

        #En esta parte se le da movimiento al enemigo 3 de la siguiente forma:
        #Primero se establece un condicional que diga si la posicion que tome el enemigo 3 respecto al ejex es menor a la poscion que tiene el jugador 2 respecto a
        #al ejex entonces se el enemigo 3 que fue creado sobre el canvas se mueva en "x" un 1 y en "y" un dos, de lo contrario que se mueva el enemigo 3 en el ejex
        #-2 y en el "y" 1. Ademas se establece que si la posicion que tome el enemigo 3 en el ejey es mayor a 800, entonces se mueva hacia arriba dicho enemigo solo
        #en y, cualquier valor que este comprendido en el rango de 800 a 2000, tal como lo describe la variable xx
        
        if(coordsEnemy3[0]<coordsJugador2[0]):
            pantalla_1.move(enemigo3,0.5,1)
        else:
            pantalla_1.move(enemigo3,-0.5,1) 

        if (coordsEnemy3[1]>800):
            pantalla_1.move(enemigo3,0,-xx)

       

        #En esta parte se le da movimiento al enemigo 3 pero del segundo mapa de la siguiente forma:
        #Primero se establece un condicional que diga si la posicion que tome el enemigo 3 respecto al ejex es menor a la poscion que tiene el jugador 1 respecto a
        #al ejex entonces se el enemigo 3 que fue creado sobre el canvas se mueva en "x" un 1 y en "y" un dos, de lo contrario que se mueva el enemigo 3 en el ejex
        #-2 y en el "y" 1. Ademas se establece que si la posicion que tome el enemigo 3 en el ejey es mayor a 800, entonces se mueva hacia arriba dicho enemigo solo
        #en y, cualquier valor que este comprendido en el rango de 800 a 2000, tal como lo describe la variable xx
            
        if (coordsEnemy33[0]<coordsJugador1[0]):
            pantalla_1.move(enemigo33,1,2)
        else:
            pantalla_1.move(enemigo33,-2,1)

        if(coordsEnemy33[1]>800):
            pantalla_1.move(enemigo33,0,-yy)
            
            
        #En esta parte lo que se hace es dar las ordenes de como y de que manera se pueden mover los enemigos 1 en los dos mapas del nivel 1 para ello se hace 
        #que los mapas se dividan en tres partes respecto al ejex con el objetivo de establecer en que parte se debe mover y sus limites así:

            #El primer condicional establece que si las posiciones que puede tomar el enemigo 1 respecto al eje x es mayor a 330 y las  posiciones que puede tomar el
            #enemigo 1 respecto al eje x es menor a 395 y ademas repecto al eje y el mismo enemigo toma posiciones mayores a 1000 entonces suceda que el enemigo
            #1 sobre el canvas se mueva en x entre un rango de -80 y 0 asi de igual forma se establece que en y se mueva entre un valor que este entre el rango de
            # -2000 y -1000
            
        if (coordsEnemy1[0] > 330) and (coordsEnemy1[0] < 395) and (coordsEnemy1[1] > 1000):
            pantalla_1.move(enemigo1,(random.randrange(-80,0)),(random.randrange(-2000, -1000)))

            
        
            #El segundo condicional establece que si las posiciones que puede tomar el enemigo 1 respecto al eje x es mayor a 230 y las  posiciones que puede tomar el
            #enemigo 1 respecto al eje x es menor a 330 y ademas repecto al eje y el mismo enemigo toma posiciones mayores a 1000 entonces suceda que el enemigo
            #1 sobre el canvas se mueva en x entre un rango de -90 y 90 asi de igual forma se establece que en y se mueva entre un valor que este entre el rango de
            # -2000 y -1000
            
        elif(coordsEnemy1[0] > 230) and (coordsEnemy1[0] < 330)and (coordsEnemy1[1] > 1000):
            pantalla_1.move(enemigo1,(random.randrange(-90,90)),(random.randrange(-2000, -1000)))

            

            #El tercer condicional establece que si las posiciones que puede tomar el enemigo 1 respecto al eje x es mayor a 143 y las  posiciones que puede tomar el
            #enemigo 1 respecto al eje x es menor a 230 y ademas repecto al eje y el mismo enemigo toma posiciones mayores a 1000 entonces suceda que el enemigo
            #1 sobre el canvas se mueva en x entre un rango de 0 y 80 asi de igual forma se establece que en y se mueva entre un valor que este entre el rango de
            # -2000 y -1000
            
        elif (coordsEnemy1[0] > 143) and (coordsEnemy1[0] < 230)and (coordsEnemy1[1] > 1000):
            pantalla_1.move(enemigo1,(random.randrange(0,80)),(random.randrange(-2000, -1000)))


            

        #De la misma forma se hace con el enemigo 1 del mapa 2:


            #El primer condicional establece que si las posiciones que puede tomar el enemigo 1 respecto al eje x es mayor a 1200 y las  posiciones que puede tomar el
            #enemigo 1 respecto al eje x es menor a 1300 y ademas repecto al eje y el mismo enemigo toma posiciones mayores a 1000 entonces suceda que el enemigo
            #1 sobre el canvas se mueva en x entre un rango de -80 y 0 asi de igual forma se establece que en y se mueva entre un valor que este entre el rango de
            # -2000 y -1000
        
        if (coordsEnemy11[0] > 1200) and (coordsEnemy11[0] < 1300) and (coordsEnemy11[1] > 1000):
            pantalla_1.move(enemigo11,(random.randrange(-80,0)),(random.randrange(-2000, -1000)))



            #El segundo condicional establece que si las posiciones que puede tomar el enemigo 1 respecto al eje x es mayor a 1150 y las  posiciones que puede tomar el
            #enemigo 1 respecto al eje x es menor a 1200 y ademas repecto al eje y el mismo enemigo toma posiciones mayores a 1000 entonces suceda que el enemigo
            #1 sobre el canvas se mueva en x entre un rango de -90 y 90 asi de igual forma se establece que en y se mueva entre un valor que este entre el rango de
            # -2000 y -1000
            
        elif(coordsEnemy11[0] > 1150) and (coordsEnemy11[0] < 1200)and (coordsEnemy11[1] > 1000):
            pantalla_1.move(enemigo11,(random.randrange(-90,90)),(random.randrange(-2000, -1000)))


            #El tercer condicional establece que si las posiciones que puede tomar el enemigo 1 respecto al eje x es mayor a 1000 y las  posiciones que puede tomar el
            #enemigo 1 respecto al eje x es menor a 1150 y ademas repecto al eje y el mismo enemigo toma posiciones mayores a 1000 entonces suceda que el enemigo
            #1 sobre el canvas se mueva en x entre un rango de 0 y 80 asi de igual forma se establece que en y se mueva entre un valor que este entre el rango de
            # -2000 y -1000
            
        elif (coordsEnemy11[0] > 1000) and (coordsEnemy11[0] < 1150)and (coordsEnemy11[1] > 1000):
            pantalla_1.move(enemigo11,(random.randrange(0,80)),(random.randrange(-2000, -1000)))


        #si las coordenadas de las rocas espaciales son mayores a 700 respecto al ejey entonces: Se mueva -700 hacia arriba para que vuelva a parecer
        if(pantalla_1.coords(pelito)[1]>700):
            pantalla_1.move(pelito,0,-700)
        
        #si en la colision que se da entre cohete2 y pelito(rocas espaciales)se da que:
            #*Se presiona 65(A) la cual apareceria en movimientos entonces se mueva -10, si se presiona 68(D) entonces se mueva 10 hacia la derecha y de lo contrario
            #entonces se mueve 10 hacia la derecha lo direcciona hacia otro lado
            
        if(colision(cohete2,pelito)):
            if(65 in movimientos):
                pantalla_1.move(cohete2,-10,0)
            elif( 68 in movimientos):
                   pantalla_1.move(cohete2,10,0)
            else:
                pantalla_1.move(cohete2,10,0)
                
        if(colision(cohete1,pelito2)):
            if(65 in movimientos):
                pantalla_1.move(cohete1,-10,0)
            elif( 68 in movimientos):
                   pantalla_1.move(cohete1,10,0)
            else:
                pantalla_1.move(cohete1,10,0)    

        #Se establece que si la funcion colision es verdadera con cohete2 y combustible entonces a esta variable se le sume 39 y desparezca para que vuelva aparecer
        #desde la parte superior
        if(colision(cohete2,combustible1)):
            combustible+=30
            pantalla_1.move(combustible1,0,-700)

        if(colision(cohete1,combustible22)):
            combustible2+=30
            pantalla_1.move(combustible22,0,-700)
        #Se establece que si la funcion colision entre cohete2 y enemigo3 es verdadera entoces:
            #*Se crea un ciclo con el for en un rango 10 y utilizando las variables antes utilizadas se hace que x sea igual a 1, si M es igual a cero que es cierto
            # entonces utilizando time.clock calculo el tiempo y le asigno a M un uno para asegurarnos de que no pueda volver a entrar, por consiguiente el cohete
            #se movera en x la tercera parte de i, se mueva el cohete y el enemigo segun las asignaciones hechas, tambien detro el mismo if se establece que si la
            #diferencia de C y L es mayor a 1.5 entonces las variables tomaran nuevamente el valor de 0
        if (colision(cohete2,enemigo3) ) :
            
            for i in range(10):
                
                x=1
                if(M==0):
                    L= time.clock()
                    M=1
                pantalla_1.move(cohete2,i/3,0)
                pantalla_1.move(enemigo3,0,-pantalla_1.coords(enemigo3)[1])
        C=time.clock()
        
        if(C-L>=1.5):
                x=0
                M=0
                L=C
                C=0

        #En esta parte sucede lo mismo que lo anterior        
        if (colision(cohete2,enemigo2) ) :
            n=1
            for i in range(10):
                n*=-1
                x=1
                if(M==0):
                    L= time.clock()
                    M=1
                pantalla_1.move(cohete2,i,0)
                vel=50
                pantalla_1.move(enemigo2,0,-pantalla_1.coords(enemigo2)[1])
        
        C=time.clock()
        
        if(C-L>=1.5):
                x=0
                M=0
                L=C
                C=0

        #En esta parte sucede lo mismo que lo anterior         
        if (colision(cohete2,enemigo1) ) :
            n=1
            for i in range(10):
                n*=-1
                x=1
                if(M==0):
                    L= time.clock()
                    M=1
                pantalla_1.move(cohete2,i,0)
                vel=50
                pantalla_1.move(enemigo1,0,-pantalla_1.coords(enemigo1)[1])
        C=time.clock()
        
        if(C-L>=1.5):
                x=0
                
                M=0
                L=C
                C=0
            
        if (colision(cohete1,enemigo11) ) :
            
            for i in range(10):
                
                k=1
                if(N==0):
                    V= time.clock()
                    print(k)
                    N=1
                pantalla_1.move(cohete1,i/3,0)
                pantalla_1.move(enemigo11,0,-pantalla_1.coords(enemigo11)[1])
        B=time.clock()
        if(B-V>=1.5):
                k=0
                
                N=0
                V=B
                B=0
        if (colision(cohete1,enemigo22) ) :
            
            for i in range(10):
                
                k=1
                if(N==0):
                    V= time.clock()
                    N=1
                pantalla_1.move(cohete1,i/3,0)
                pantalla_1.move(enemigo22,0,-pantalla_1.coords(enemigo22)[1])
        B=time.clock()
        if(B-V>=1.5):
                k=0
                
                N=0
                V=B
                B=0
        if (colision(cohete1,enemigo33) ) :
            
            for i in range(10):
                
                k=1
                if(N==0):
                    V= time.clock()
                    N=1
                pantalla_1.move(cohete1,i/3,0)
                pantalla_1.move(enemigo33,0,-pantalla_1.coords(enemigo33)[1])
        B=time.clock()
        if(B-V>=1.5):
                k=0
                
                N=0
                V=B
                B=0
#Movimiento de los jugadores con las teclas
movimientos=[]
def moverArriba(e):
    global movimientos
    if (e.keycode in movimientos):
        movimientos.pop(movimientos.index(e.keycode)) #si esta en movimiento la quita cuando se libera la tecla

def moverAbajo(e):
    global movimientos
    if not (e.keycode in movimientos):#si esta en movimiento la añade cuando la detecta
        movimientos.append(e.keycode)            
            
            
#Se define la funcion llamada movCohetes y se establecen ademas unas variables globales que mas adelante seran utilizadas.        
def movCohetes():
    global movimientos,cohete2,distancia,vel,combustible,enemigo1,enemigo2,enemigo3,vel2, distancia2, cohete1,combustible2

    #Se establece que si las posiciones del jugador dos en el canvas respecto al ejex es menor o igual a 135 entonces se mueve el cohete respecto a x 20 
    if(pantalla_1.coords(cohete2)[0]<=135):
     pantalla_1.move(cohete2,20,0)

    #Se establece que si las posiciones del jugador dos en el canvas respecto al ejex es mayor o igual a 395 entonces se mueve el cohete respecto a x -20 
    if(pantalla_1.coords(cohete2)[0]>=395):
     pantalla_1.move(cohete2,-20,0)

    
    else:
        if (65 in movimientos):
            pantalla_1.move(cohete2, -10,0)
        if (68 in movimientos):
            pantalla_1.move(cohete2, 10,0)
        if (83 in movimientos):

            guardado.seek(0)
            
            w=[combustible,distancia,vel,pantalla_1.coords(cohete2)[0],combustible2,vel2, distancia2, pantalla_1.coords(cohete1)[0]]
            for i in w:
                guardado.write(str(int(i))+"\n")
    
    #Se establece que si las posiciones del jugador dos en el canvas respecto al ejex es menor o igual a 1005 entonces se mueve el cohete respecto a x 20        
    if(pantalla_1.coords(cohete1)[0]<=1005):
     pantalla_1.move(cohete1,20,0)

    #Se establece que si las posiciones del jugador dos en el canvas respecto al ejex es mayor o igual a 1255 entonces se mueve el cohete respecto a x -20 
    if(pantalla_1.coords(cohete1)[0]>=1255):
     pantalla_1.move(cohete1,-20,0)

    #De lo contrario  se maneja que si se presiona alguna de las teclas menciondas se mueva segun corresponda 
    else:
        if (74 in movimientos):
            pantalla_1.move(cohete1, -10,0)
        if (76 in movimientos):
            pantalla_1.move(cohete1, 10,0)
        
    
            
    
pantalla_1.bind("<KeyRelease>",moverArriba)

pantalla_1.bind("<KeyPress>", moverAbajo)
pantalla_1.focus_set()

#Se carggan las imagaenes de los botones de los niveles y se les crea la etiqueta para su funcionamiento   
primerNivel=PhotoImage(file="nivel1.png")
segundoNivel=PhotoImage(file="nivel2.png")
tercerNivel=PhotoImage(file="nivel3.png")
cuartoNivel=PhotoImage(file="nivel4.png")
quintoNivel=PhotoImage(file="nivel5.png")

nivelone=Button(ventana, image= primerNivel,command = primero).place(x=580, y=230)       
niveltwo=Button(ventana, image= segundoNivel).place(x=580, y=280)
nivelthree=Button(ventana, image= tercerNivel).place(x=580, y=330)
nivelfour=Button(ventana, image= cuartoNivel).place(x=580, y=380)
nivelfive=Button(ventana, image= quintoNivel).place(x=580, y=430)

